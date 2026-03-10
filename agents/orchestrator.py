from processors.pdf_processor import process_pdf
from rag.chunker import chunk_text
from rag.embedder import create_embeddings
from rag.vector_store import store_chunks
from rag.retriever import retrieve_chunks
from llm.generator import generate_answer

def ingest_document(file_path):

    text = process_pdf(file_path)

    chunks = chunk_text(text)

    embeddings = create_embeddings(chunks)

    store_chunks(chunks, embeddings)

    return "Document indexed successfully"


def answer_question(question):

    retrieved_chunks = retrieve_chunks(question)

    context = "\n".join(retrieved_chunks)

    answer = generate_answer(context, question)

    return answer