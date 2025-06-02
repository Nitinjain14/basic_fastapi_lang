from fastapi import FastAPI, Query
from llm_service import ask_llm_with_langchain

app = FastAPI()

@app.get("/ask")
def ask_question(q: str = Query(..., description="Your question for the AI")):
    answer = ask_llm_with_langchain(q)
    return {"question": q, "answer": answer}
