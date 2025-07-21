import json
import numpy as np
from app.chroma_utils import collection
from app.embeddings import get_embedding


def get_user_embedding(user_id: str):

    with open("app/data/user_history.json") as f:
        history = json.load(f)

    liked_ids = history.get(user_id, [])
    if not liked_ids:
        return None, None

    results = collection.get(ids=liked_ids)
    docs_returned = results["documents"]
    embeddings = get_embedding(docs_returned)
    user_vector = np.mean(embeddings, axis=0)
    return user_vector.tolist(), liked_ids


def recommend_for_user(user_id: str, top_k=3):

    user_vector, seen_ids = get_user_embedding(user_id)
    if not user_vector:
        return {"message": "No history for this user."}

    results = collection.query(query_embeddings=[user_vector], n_results=top_k + len(seen_ids))
    recommendations = []
    
    for doc, id in zip(results["documents"][0], results["ids"][0]):        
        if id not in seen_ids:
            recommendations.append({"document": doc, "post_id": id})
        
        if len(recommendations) >= top_k:
            break
    
    return recommendations


def search_by_text(query_text: str, top_k=5):
    
    query_vector = get_embedding(query_text)
    
    results = collection.query(
        query_embeddings=[query_vector],
        n_results=top_k
    )

    response = []
    for doc, id in zip(results["documents"][0], results["ids"][0]):
        response.append({'text': doc, 'id': id})

    return response