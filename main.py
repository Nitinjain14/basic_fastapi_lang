from fastapi import FastAPI
from pydantic import BaseModel
from llm_service import ask_llm


app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
def ask_question(request: QuestionRequest):
    answer = ask_llm(request.question)
    return {"answer": answer}