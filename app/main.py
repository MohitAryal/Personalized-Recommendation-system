from fastapi import FastAPI
from pydantic import BaseModel
from app.recommender import recommend_for_user
from app.embeddings import get_embedding

app = FastAPI()


class UserRequest(BaseModel):
    user_id: str
    top_k: int = 3


class SearchRequest(BaseModel):
    query: str
    top_k: int = 5


@app.post("/recommend")
def get_recommendations(input: UserRequest):
    return recommend_for_user(input.user_id, input.top_k)


@app.post("/search")
def search_content(input: SearchRequest):
    from app.recommender import search_by_text
    return search_by_text(input.query, top_k=input.top_k)