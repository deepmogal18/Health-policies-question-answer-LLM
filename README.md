# Health-policies-question-answer-LLM
/////////////////////////////////////////////

This project is an LLM-powered question answering system designed to process health policy and insurance documents (PDFs) and provide accurate, context-based answers. It uses embeddings, retrieval, and reasoning layers to parse complex insurance and healthcare policy language into user-friendly responses.

//////////////////////////////////////////


//////////   Features  //////////

PDF Loader: Extracts text from insurance/healthcare policy PDFs.

Embeddings & Retriever: Converts documents into vector representations for efficient semantic search.

Decision Logic: Routes queries through logic rules + LLM for accurate domain-specific answers.

LLM Extractor: Uses LLMs for summarization, policy interpretation, and natural language Q&A.

Query Parser: Breaks down user queries into structured components for better retrieval.

REST API (FastAPI/Flask): Exposes endpoints for asking questions against uploaded policies.

Modular Design: Each component (loading, embedding, retrieval, answering) is isolated for flexibility.



///////////     Installation        /////////////

Clone the repository:

git clone https://github.com/yourusername/Health-policies-question-answer-LLM
.git
cd health-insurance-qa-llm


Create a virtual environment and install dependencies:

python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

pip install -r requirements.txt






/////////     Add your API keys to .env:       ///////////

OPENAI_API_KEY=your_key_here
GROQ_API_KEY=your_key_here




/////////    Usage       //////////
Run the API
python app.py


Upload a PDF policy to pdfs/

Ask question like:

AGE 45 MALE, CAN I AVAIL INSURANCE FOR HEART SURGERY ?
