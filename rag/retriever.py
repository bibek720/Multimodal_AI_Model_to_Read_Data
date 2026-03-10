from rag.embedder import model
from rag.vector_store import collection

def retrieve_chunks(query):

    query_embedding = model.encode([query])

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=3
    )

    return results["documents"][0]