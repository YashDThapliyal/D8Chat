import chromadb
from sentence_transformers import SentenceTransformer
import os

class QueryProcessor:
    def __init__(self):
        persist_directory = os.path.join(os.getcwd(), "chroma_db")
        self.client = chromadb.PersistentClient(path=persist_directory)
        self.collection = self.client.get_collection("data8_textbook")
        self.model = SentenceTransformer('all-MiniLM-L6-v2')

    def process_query(self, query, top_k=5):
        query_embedding = self.model.encode(query).tolist()
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        return results['documents'][0]


#TESTING    
if __name__ == "__main__":
    processor = QueryProcessor()

    test_query = "What is a hypothesis test?"
    relevant_chunks = processor.process_query(test_query)

    print(f"Retrieved {len(relevant_chunks)} chunks for the query: '{test_query}'")
    print("First chunk:", relevant_chunks[0][:200] + "...")
