from fastapi import FastAPI, UploadFile
import shutil

from agents.orchestrator import ingest_document, answer_question

app = FastAPI()

@app.post("/upload")

async def upload(file: UploadFile):

    path = f"uploads/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    ingest_document(path)

    return {"message":"Document processed"}


@app.post("/ask")

async def ask(question: str):

    answer = answer_question(question)

    return {"answer":answer}