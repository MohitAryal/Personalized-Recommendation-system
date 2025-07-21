from chromadb import PersistentClient

client = PersistentClient(path='/chroma')
collection = client.get_or_create_collection(name='content_recommender',)

print('client initialized successfully')