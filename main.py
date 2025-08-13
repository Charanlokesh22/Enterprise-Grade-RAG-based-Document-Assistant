
from fastapi import FastAPI
from pydantic import BaseModel
from app.agent_workflow import run_agent
from app.monitor import log_to_whylabs, log_to_arize

app = FastAPI(title="Enterprise RAG-based Document Assistant")

class QueryRequest(BaseModel):
    query: str

@app.post("/ask")
def ask_doc(query_request: QueryRequest):
    answer = run_agent(query_request.query)
    log_to_whylabs(query_request.query, answer)
    log_to_arize(query_request.query, answer)
    return {"query": query_request.query, "answer": answer}
