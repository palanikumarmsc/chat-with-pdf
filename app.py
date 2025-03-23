import os
import streamlit as st
import tempfile
import hashlib
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.llms.huggingface_hub import HuggingFaceHub
from dotenv import load_dotenv
import re


st.set_page_config(layout="wide")  # Optional: make layout wide by default

# Inject custom CSS to expand full width
st.markdown("""
    <style>
    .main .block-container {
        max-width: 100% !important;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    </style>
""", unsafe_allow_html=True)




# Load environment variables
load_dotenv()
HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")
MODEL_ID = os.getenv("MODEL_NAME", "mistralai/Mistral-7B-Instruct-v0.3")

# Create index folder
os.makedirs("index", exist_ok=True)

# Initialize models
embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
llm = HuggingFaceHub(
    repo_id=MODEL_ID,
    huggingfacehub_api_token=HUGGINGFACEHUB_API_TOKEN,
    model_kwargs={"temperature": 0.3, "max_new_tokens": 512}
)

# Title
st.markdown("""
    <h1 style='text-align: center;'>📄 Chat with PDF using FAISS + HuggingFace</h1>
""", unsafe_allow_html=True)


# Two-column layout
left_col, right_col = st.columns([3, 5])

# Left column: File upload
with left_col:
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

def extract_answer_only(text):
    match = re.search(r"Answer:\s*(.*)", text, re.DOTALL | re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return "Answer not found."

def get_index_path(file_bytes):
    file_hash = hashlib.md5(file_bytes).hexdigest()
    return os.path.join("index", f"{file_hash}")

# Initialize placeholders
faiss_index = None
index_loaded = False

# Process file if uploaded
if uploaded_file:
    file_bytes = uploaded_file.read()
    index_path = get_index_path(file_bytes)

    if os.path.exists(index_path):
        faiss_index = FAISS.load_local(index_path, embedding_model, allow_dangerous_deserialization=True)

        index_loaded = True
    else:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
            tmp_file.write(file_bytes)
            tmp_path = tmp_file.name

        loader = PyPDFLoader(tmp_path)
        documents = loader.load()
        splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        chunks = splitter.split_documents(documents)

        faiss_index = FAISS.from_documents(chunks, embedding_model)
        faiss_index.save_local(index_path)
        index_loaded = True

# Right column: Ask a question
with right_col:
    if uploaded_file and index_loaded:
        st.success("✅ PDF processed and ready!")
        user_query = st.text_input("Ask a question about the PDF:")
        if st.button("Submit Question") and user_query:
            with st.spinner("🔎 Searching..."):
                relevant_docs = faiss_index.similarity_search(user_query, k=3)
                context = "\n\n".join([doc.page_content for doc in relevant_docs])
                prompt = f"""Use the following context to answer the question:\n\n{context}\n\nQuestion: {user_query}\nAnswer:"""

                response = llm.invoke(prompt).strip()
                clean_answer = extract_answer_only(response)

                st.markdown("### 💬 Answer:")
                st.write(clean_answer)
    elif not uploaded_file:
        st.warning("👈 Please upload a PDF file first to begin asking questions.")
