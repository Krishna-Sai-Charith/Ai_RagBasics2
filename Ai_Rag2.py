import os
import glob
from dotenv import load_dotenv
import gradio as gr  # optional, used for interface

# LangChain-related
from langchain.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter

# -----------------------------
# 🛠️ CONFIGURATION
# -----------------------------

MODEL = "gpt-4o-mini"  # cost-efficient OpenAI model
DB_NAME = "vector_db"

# Load environment variables from `.env` file
load_dotenv(override=True)
openai_api_key = os.getenv('OPENAI_API_KEY', 'your-key-if-not-using-env')
os.environ['OPENAI_API_KEY'] = openai_api_key
print(f"✅ Loaded OpenAI API Key: {openai_api_key[:4]}...")

# -----------------------------
# 📂 LOAD DOCUMENTS
# -----------------------------

folders = glob.glob("knowledge-base/*")
print(f"📁 Folders found in knowledge-base/: {folders}")

# Fix encoding issues for some systems
text_loader_kwargs = {'encoding': 'utf-8'}
# Alternative for Windows users if encoding issues occur:
# text_loader_kwargs = {'autodetect_encoding': True}

documents = []
for folder in folders:
    doc_type = os.path.basename(folder)
    loader = DirectoryLoader(
        folder,
        glob="**/*.md",
        loader_cls=TextLoader,
        loader_kwargs=text_loader_kwargs
    )
    folder_docs = loader.load()
    for doc in folder_docs:
        doc.metadata["doc_type"] = doc_type
        documents.append(doc)

print(f"📄 Total documents loaded: {len(documents)}")

# Show a sample document (25th one, index 24)
if len(documents) > 24:
    print("\n📝 Sample document [24]:")
    print(documents[24])
else:
    print("⚠️ Not enough documents to display index 24.")

# -----------------------------
# ✂️ SPLIT DOCUMENTS INTO CHUNKS
# -----------------------------

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunks = text_splitter.split_documents(documents)

print(f"🔖 Total chunks created: {len(chunks)}")

# Show a sample chunk (121st, index 120)
if len(chunks) > 120:
    print("\n🔍 Sample chunk [120]:")
    print(chunks[120])
else:
    print("⚠️ Not enough chunks to display index 120.")

# -----------------------------
# 🗂️ DOCUMENT TYPES
# -----------------------------

doc_types = set(chunk.metadata['doc_type'] for chunk in chunks)
print(f"\n📚 Document types found: {', '.join(doc_types)}")

# -----------------------------
# 🔎 SEARCH CHUNKS FOR 'CEO'
# -----------------------------

print("\n🔎 Chunks containing the word 'CEO':\n")
found = False
for chunk in chunks:
    if 'CEO' in chunk.page_content:
        print(chunk)
        print("_________\n")
        found = True

if not found:
    print("❌ No chunk contained the word 'CEO'.")
