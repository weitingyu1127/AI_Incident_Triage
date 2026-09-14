from fastapi import FastAPI
from pydantic import BaseModel

from rag import ask_rag


app = FastAPI()


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def root():
    return {
        "message": "AI Incident Copilot API"
    }


@app.post("/ask")
def ask(request: QuestionRequest):

    answer, sources, results = ask_rag(
        request.question
    )

    return {
        "answer": answer,
        "sources": sources
    }