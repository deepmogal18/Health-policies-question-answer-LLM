import os
from pdf_loader import load_pdf_chunks

def load_documents(folder_path):
    all_chunks = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".pdf"):
            path = os.path.join(folder_path, filename)
            print(f"Loading {path}...")
            chunks = load_pdf_chunks(path)
            all_chunks.extend(chunks)
    print(f"Total chunks created: {len(all_chunks)}")
    return all_chunks
