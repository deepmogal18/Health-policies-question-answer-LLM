from dotenv import load_dotenv
load_dotenv()

from loader import load_documents
from retriever import build_faiss_index, retrieve_top_k
from decision_logic import evaluate_decision
from decision_llm import evaluate_decision_llm
from transformers import AutoTokenizer, AutoModelForQuestionAnswering

tokenizer = AutoTokenizer.from_pretrained("deepset/roberta-base-squad2")
model = AutoModelForQuestionAnswering.from_pretrained("deepset/roberta-base-squad2")
API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
API_TOKEN = "api key"

all_chunks = load_documents("pdfs")
index, all_chunks, text_chunks = build_faiss_index(all_chunks)

query = input("Enter your query: ")
top_chunks = retrieve_top_k(query, index, text_chunks)
print("\nTop relevant chunks:\n")
for i, chunk in enumerate(top_chunks, 1):
    print(f"{i}. {chunk}\n")

try:
    decision_result = evaluate_decision_llm(query, top_chunks)
    print("\n🔮 LLM Decision Output:\n", decision_result)
except Exception as e:
    print("LLM failed. Falling back to rule-based logic.")
    rule_result = evaluate_decision(query, top_chunks)
    print("\n🧠 Rule-based Decision Output:\n", rule_result)

