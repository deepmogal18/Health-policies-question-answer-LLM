# Health-policies-question-answer-LLM

//

Health Policy & Insurance Question Answering
LLM
This project is an LLM-powered question answering system designed to process health policy and
insurance documents (PDFs) and provide accurate, context-based answers. It uses embeddings,
retrieval, and reasoning layers to parse complex insurance and healthcare policy language into
user-friendly responses.
■ Features
• PDF Loader: Extracts text from insurance/healthcare policy PDFs.
• Embeddings & Retriever: Converts documents into vector representations for efficient semantic
search.
• Decision Logic: Routes queries through logic rules + LLM for accurate domain-specific
answers.
• LLM Extractor: Uses LLMs for summarization, policy interpretation, and natural language Q&A.;
• Query Parser: Breaks down user queries into structured components for better retrieval.
• REST API (FastAPI/Flask): Exposes endpoints for asking questions against uploaded policies.
• Modular Design: Each component (loading, embedding, retrieval, answering) is isolated for
flexibility.
■ Project Structure
__pycache__/ # Python cache pdfs/ # Store PDF documents (health/insurance policies) .env #
Environment variables (API keys, configs) app.py # Main app entry point (API server)
decision_llm.py # LLM decision layer for handling responses decision_logic.py # Rule-based logic
for special cases embedder.py # Embedding generator for documents llm_extractor.py #
LLM-based text extraction & summarization loader.py # Loads documents into the pipeline main.py
# Orchestrator script (CLI or runner) pdf_loader.py # PDF parsing utility query_parser.py # Parses
user questions into structured form requirements.txt # Dependencies retriever.py # Vector retriever
for semantic search test_groq.py # Testing with Groq LLM API
■■ Installation
1. Clone the repository: git clone https://github.com/yourusername/health-insurance-qa-llm.git cd
health-insurance-qa-llm 2. Create a virtual environment and install dependencies: python -m venv
venv source venv/bin/activate # (Linux/Mac) venv\Scripts\activate # (Windows) pip install -r
requirements.txt 3. Add your API keys to .env: OPENAI_API_KEY=your_key_here
GROQ_API_KEY=your_key_here
■■ Usage
Run the API: python app.py - Upload a PDF policy to pdfs/ - Ask questions like: "What is covered
under hospitalization expenses?" "What are the exclusions in this policy?" "What is the maximum
claim limit for maternity benefits?" CLI Usage: python main.py --query "What is the waiting period
for pre-existing conditions?"
■ Example Workflow
• Upload a health policy PDF → pdf_loader.py extracts text.
• Text is embedded → embedder.py.
• Semantic search retrieves relevant chunks → retriever.py.
• LLM + logic combine to generate final answer → decision_llm.py.
■ Roadmap
• Support multi-document querying
• Add RAG (Retrieval-Augmented Generation) optimization
• Improve insurance-specific reasoning templates
• Deploy as a web app with frontend
