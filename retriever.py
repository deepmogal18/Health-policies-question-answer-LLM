import faiss
import numpy as np
from embedder import embed_chunks, embed_query

def build_faiss_index(chunks):
    text_chunks = [chunk['text'] for chunk in chunks]
    embeddings = embed_chunks(text_chunks)
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index, chunks, text_chunks

def retrieve_top_k(query, index, text_chunks, k=5):
    query_embedding = embed_query(query).reshape(1, -1)
    distances, indices = index.search(query_embedding, k)
    return [text_chunks[i] for i in indices[0]]
