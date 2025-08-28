import fitz  # PyMuPDF

def load_pdf_chunks(pdf_path):
    doc = fitz.open(pdf_path)
    chunks = []
    for page_num in range(len(doc)):
        text = doc[page_num].get_text()
        if text.strip():
            chunks.append({"text": text.strip(), "page": page_num + 1})
    return chunks
