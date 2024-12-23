import chromadb
import pickle
import os

def setup_vector_store():
    persist_directory = os.path.join(os.getcwd(), "chroma_db")
    client = chromadb.PersistentClient(path=persist_directory)

    collection = client.get_or_create_collection("data8_textbook")

    if collection.count() == 0:
        print("Collection is empty. Loading data...")
        with open("chunks_and_embeddings.pkl", "rb") as f:
            chunks, embeddings = pickle.load(f)


        collection.add(
            documents=chunks,
            embeddings=embeddings,
            ids=[f"chunk_{i}" for i in range(len(chunks))]
        )
        print(f"Added {len(chunks)} documents to the vector store.")
    else:
        print(f"Collection already contains {collection.count()} documents.")

    return collection

if __name__ == "__main__":
    setup_vector_store()
