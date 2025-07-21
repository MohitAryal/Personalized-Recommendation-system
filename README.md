# Personalized Vector Recommender

A FastAPI-based personalized recommendation system using user history, content embeddings, and ChromaDB for fast vector search.


##  Overview

This project recommends relevant content to users by combining:

- User interaction history (liked posts)
- Content embeddings (text representation)
- User profile embeddings (averaged from liked contents)
- ChromaDB for fast vector similarity search

The goal is to generate **relevant, unseen** recommendations using lightweight machine learning techniques — ideal for real-world personalization use cases.

----------------------------------------------

## How It Works
[User ID]
└──► Lookup liked posts (history)
└──► Fetch embeddings of those posts
└──► Average → User embedding
└──► Query ChromaDB
└──► Return unseen top-k documents

----------------------------------------------