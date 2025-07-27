# one-time setup script to get all posts and their embeddings inside the database

from app.chroma_utils import collection
import json

with open('data/posts_data.json', 'r') as file:
    docs = json.load(file)

ids = [doc['id'] for doc in docs]
documents = [doc['text'] for doc in docs]

collection.add(
    ids=ids,
    documents=documents
)

print("Content loaded into ChromaDB.")
