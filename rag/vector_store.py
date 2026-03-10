import chromadb

client = chromadb.Client()

collection = client.get_or_create_collection("documents")

def store_chunks(chunks, embeddings):

    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )