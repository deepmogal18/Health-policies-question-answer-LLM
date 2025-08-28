def parse_query_to_json(query):
    return {
        "query": query,
        "surgery_type": "knee" if "knee" in query.lower() else "cataract" if "cataract" in query.lower() else "unknown",
        "claim_amount": 25000,
        "start_date": "2024-01-01",
        "claim_date": "2024-04-01",
        "coverage_amount": 30000,
        "policy_number": "PN123456",
        "insured_name": "Ravi Kumar"
    }
