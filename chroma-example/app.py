import chromadb


client = chromadb.Client()

collection = client.get_or_create_collection("test")

documents = [
    {
        "id": "1",
        "text": "Hello World",
        "metadata": {"source": "test"},
    },
    {
        "id": "2",
        "text": "How are you?",
        "metadata": {"source": "test"},
    },
    {
        "id": "3",
        "text": "How can I help you?",
        "metadata": {"source": "test"},
    },
]

# Extract all data into lists for batch operation
ids = [doc["id"] for doc in documents]
texts = [doc["text"] for doc in documents]
metadatas = [doc["metadata"] for doc in documents]

# Single batch upsert
collection.upsert(
    ids=ids,
    documents=texts,
    metadatas=metadatas,
)

results = collection.query(
    query_texts=["Hello"],
    n_results=2,
)

print(results)