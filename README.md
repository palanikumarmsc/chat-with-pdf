# 📄 Chat with PDF Bot using FAISS, LangChain & Hugging Face

This is a Streamlit-based chatbot application that allows users to **ask questions directly from the content of uploaded PDF files**. It uses:

- 🧠 **LangChain** for document processing and chunking  
- 🧠 **Hugging Face** for generating answers using a language model  
- ⚡ **FAISS** for fast semantic search over PDF content  
- 🌐 **Streamlit** for the interactive web UI  



## 🚀 Features

- Upload a PDF and instantly create a searchable knowledge base  
- Ask natural language questions from your PDF  
- Get accurate answers powered by semantic search and language models  
- Simple one-page UI built with Streamlit  



## 📦 Setup Instructions

### 🐍 1. Create and Activate a Python Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate (Windows)
venv\Scripts\activate

# Activate (macOS/Linux)
source venv/bin/activate
```

### 📥 2. Install All Dependencies

Make sure you have a `requirements.txt` file. Then run:

```bash
pip install -r requirements.txt
```

If you don’t have one, you can install manually with:

```bash
pip install streamlit langchain faiss-cpu huggingface_hub python-dotenv pypdf
```

---

## 🔐 3. Setup Hugging Face Token

To use Hugging Face models, you need an API token:

1. Go to [https://huggingface.co](https://huggingface.co)
2. Sign up or log in
3. Go to your profile → **Settings** → **Access Tokens**
4. Create a new token with **"Read"** access
5. In the root of your project, create a `.env` file with:

```env
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_token
MODEL_NAME=mistralai/Mistral-7B-Instruct-v0.3
```

---

## ▶️ How to Run the App

```bash
streamlit run app.py
```

---

## 🔗 Sample PDF URLs & Sample Questions

You can download and upload any of the following PDFs in the chatbot UI:

### 📘 1. Transformer Paper - "Attention Is All You Need"

**URL:** https://arxiv.org/pdf/1706.03762.pdf

**Example Questions:**
- What is the main contribution of the "Attention Is All You Need" paper?
- How does the Transformer model replace recurrence?
- What dataset was used for evaluation in the paper?

---

### 📄 2. Tesla 2022 Annual Report

**URL:** https://www.sec.gov/Archives/edgar/data/1318605/000095017023002289/tsla-20221231.htm  
(Download as PDF from your browser)

**Example Questions:**
- What were Tesla's total revenues in 2022?
- How many Gigafactories does Tesla operate?
- What were the biggest risks mentioned in the report?

---

### 🇺🇸 3. U.S. Constitution

**URL:** https://www.archives.gov/files/founding-docs/constitution_transcript.pdf

**Example Questions:**
- What does the First Amendment say?
- How many articles are there in the U.S. Constitution?
- What powers are granted to Congress?

---

### 🐍 4. Python Basics Cheatsheet

**URL:** https://github.com/DataCamp/DataCamp_Cheat_Sheets/raw/master/Python_Basics_Cheat_Sheet.pdf

**Example Questions:**
- How do you create a list in Python?
- What is the syntax for a for loop in Python?
- How do you import a library?

---

### 🌍 5. WHO COVID-19 Situation Report

**URL:** https://www.who.int/docs/default-source/coronaviruse/situation-reports/20200423-sitrep-94-covid-19.pdf

**Example Questions:**
- How many confirmed COVID-19 cases were there globally on April 23, 2020?
- What regions had the highest number of new cases?
- What public health strategies were recommended?

---

## 🧠 How It Works

1. **PDF Upload**: You upload a PDF file through the UI  
2. **Text Chunking**: The PDF is chunked using LangChain's text splitter  
3. **Embedding**: Each chunk is embedded using Hugging Face embeddings  
4. **FAISS Indexing**: Embeddings are stored and searched with FAISS  
5. **Query**: Your question is embedded and used to retrieve relevant context  
6. **LLM Response**: Context + question is sent to Hugging Face LLM for an answer  

---

## ✨ Future Enhancements

- Multiple PDF uploads  
- Persistent FAISS indexing  
- Chat history memory  
- Option to select different LLMs  

---

## 📧 Contact

For any help or collaboration, feel free to reach out!

---

Enjoy chatting with your PDFs! 🤖📄
