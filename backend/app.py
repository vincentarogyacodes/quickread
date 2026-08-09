from fastapi import FastAPI
from pydantic import BaseModel
from backend.quickread import extract_article, summarize_article

app = FastAPI()

class SummarizeRequest(BaseModel):
    url: str

@app.get("/")
def home():
    return {"message": "QuickRead backend is running"}

@app.post("/summarize")
def summarize(request: SummarizeRequest):
    extracted_article = extract_article(request.url)

    if extracted_article is None:
        return {"message": "Could not extract article text from the provided URL."}
    else:
        summarized_article = summarize_article(extracted_article)
        return {"message": summarized_article}