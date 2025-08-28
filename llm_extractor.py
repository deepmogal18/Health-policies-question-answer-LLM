from groq import Groq
import os

client = Groq(api_key=os.environ["GROQ_API_KEY"])

def extract_insurance_info(query):
    prompt = f"""
You are an expert insurance assistant. Extract the following fields from the query and return them in JSON format:

Fields to extract:
- insured_name (if available)
- age (in number only)
- gender (M/F)
- location (City)
- claim_date (approximate or mentioned)
- policy_start_date (if mentioned)
- policy_duration (e.g., 3-month policy)
- claim_amount (if mentioned)
- coverage_amount (if mentioned)
- surgery_type (e.g., cataract, knee surgery)

Query: {query}

Only return JSON object with those fields. Do not explain anything.
"""

    response = client.chat.completions.create(
        model="mixtral-8x7b-32768",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )

    json_output = response.choices[0].message.content

    # Optional: Use `json.loads()` if you want to return it as dict
    return json_output
