import os
import requests
from dotenv import load_dotenv
import json
import re

load_dotenv()

API_URL = "https://api-inference.huggingface.co/models/deepset/roberta-base-squad2"
API_TOKEN = os.getenv("bajaj011")

headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}


def query_huggingface(prompt: str) -> str:
    payload = {
        "inputs": {
            "past_user_inputs": [],
            "generated_responses": [],
            "text": prompt
        },
        "parameters": {
            "max_new_tokens": 1024,
            "do_sample": True,
            "temperature": 0.7,
        }
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json()[0]["generated_text"]
    else:
        raise Exception(f"API Error {response.status_code}: {response.text}")
def evaluate_decision_llm(query: str, chunks: list) -> dict:
    """
    Uses Hugging Face LLM to answer a user query based on relevant document chunks.
    """
    combined_chunks = "\n".join(chunks)

    prompt = f"""
You are an intelligent insurance assistant.

Based on the following extracted document content, answer the user's question in JSON format.

User Query:
{query}

Relevant Document Information:
{combined_chunks}

Respond in JSON with keys:
- "decision" (either "approve" or "deny")
- "amount" (approved amount, if any)
- "justification" (a list of 2–3 bullet points)
"""

    try:
        response_text = query_huggingface(prompt)
        json_str = re.search(r'\{.*\}', response_text, re.DOTALL)
        return json.loads(json_str.group()) if json_str else {"error": "No JSON found in LLM output."}
    except Exception as e:
        return {"error": str(e)}
