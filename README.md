## 🧠 RAG Basics with LangChain + OpenAI API

This project introduces the fundamentals of **Retrieval-Augmented Generation (RAG)** by working with your own local markdown documents 📄. It uses the cost-effective `gpt-4o-mini` model 🧑‍💻 and demonstrates how to prepare a knowledge base so that large language models (LLMs) can generate more accurate, context-rich answers 💡.

You'll learn how to load, split, and organize documents, annotate them with metadata, and search through them using LangChain 🔍. The environment is configured using a `.env` file, and the process helps build smart assistants or internal search tools that "understand" your documents 📚.

---

## 🔗 What is LangChain?

[LangChain](https://www.langchain.com/) is an open-source framework that helps developers connect **language models** with **external data sources** such as files, APIs, or databases.

Instead of relying solely on the model’s built-in knowledge, LangChain enables:

- 📄 Loading and reading custom documents
- ✂️ Splitting large content into meaningful chunks
- 🧠 Storing them in vector databases for search and retrieval
- 🔁 Combining search results with user queries to improve responses

It’s ideal for RAG-based systems that need to answer questions using **your own data**.

---

## ⚙️ How LangChain Helps in This Project

In this beginner-friendly RAG setup, LangChain:

- ✅ Loads `.md` files from your `knowledge-base/` folder
- ✅ Splits them into smaller, overlapping chunks
- ✅ Adds metadata to each chunk for easy filtering
- ✅ Allows keyword-based searches (like finding chunks with “CEO”)
- ✅ Prepares the content for retrieval with an OpenAI model

This sets the stage for building AI systems that are both intelligent and aware of your private knowledge 🧠✨.

---

## 🔁 Program Flow

```text
             ┌──────────────────────────────┐
             │  📁 Read Markdown Documents  │
             └────────────┬─────────────────┘
                          │
                          ▼
        ┌────────────────────────────────────┐
        │  ✂️ Split Documents into Chunks     │
        └────────────────┬───────────────────┘
                         │
                         ▼
         ┌─────────────────────────────────┐
         │ 🧠 Annotate Each Chunk w/ Metadata│
         └────────────────┬────────────────┘
                          │
                          ▼
         ┌────────────────────────────────┐
         │ 🔍 Search or Filter Chunks (e.g. CEO)│
         └────────────────┬───────────────┘
                          │
                          ▼
         ┌────────────────────────────────┐
         │ 💡 Ready for Retrieval + LLM Use │
         └────────────────────────────────┘
