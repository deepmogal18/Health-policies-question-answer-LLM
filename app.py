import streamlit as st
import os
from loader import load_documents
from retriever import build_faiss_index, retrieve_top_k
from decision_llm import evaluate_decision_llm
from decision_logic import evaluate_decision
import tempfile
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")

st.title("📄 Insurance Document Decision System")

query = st.text_input("Enter your query:")

uploaded_files = st.file_uploader("Upload additional PDF(s):", type=["pdf"], accept_multiple_files=True)

@st.cache_resource
def load_all_documents(uploaded_files):
    # Load existing PDFs
    base_chunks = load_documents("pdfs")

    # Load uploaded PDFs
    uploaded_chunks = []
    if uploaded_files:
        for file in uploaded_files:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_file:
                tmp_file.write(file.read())
                tmp_file_path = tmp_file.name
            from pdf_loader import load_pdf_chunks
            uploaded_chunks.extend(load_pdf_chunks(tmp_file_path))
            os.remove(tmp_file_path)

    all_chunks = base_chunks + uploaded_chunks
    return all_chunks

if st.button("Evaluate") and query:
    st.write("🔍 Processing query...")

    # Combine chunks from existing + uploaded files
    all_chunks = load_all_documents(uploaded_files)

    # Build FAISS index
    index, _, text_chunks = build_faiss_index(all_chunks)

    # Retrieve top chunks
    top_chunks = retrieve_top_k(query, index, text_chunks)

    # Display top chunks (optional)
    st.subheader("📌 Top Relevant Chunks:")
    for i, chunk in enumerate(top_chunks, 1):
        st.markdown(f"**{i}.** {chunk}")

    # Run LLM decision
    try:
        result = evaluate_decision_llm(query, top_chunks)
        st.subheader("🔮 LLM Decision Output")
        st.json(result)
    except Exception as e:
        st.warning("LLM failed. Falling back to rule-based logic.")
        rule_result = evaluate_decision(query, top_chunks)
        st.subheader("🧠 Rule-Based Decision Output")
        st.json(rule_result)
