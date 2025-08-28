import numpy as np

def embed_chunks(text_chunks):
    return np.random.rand(len(text_chunks), 384).astype("float32")  # Dummy embeddings for FAISS

def embed_query(query):
    return np.random.rand(384).astype("float32")  # Dummy embedding for query
