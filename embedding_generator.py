from sentence_transformers import SentenceTransformer
import pickle
from text_preprocessor import preprocess_and_chunk


def generate_embeddings(chunks):
    model = SentenceTransformer('all-MiniLM-L6-v2')
    embeddings = model.encode(chunks,show_progress_bar=True)
    return embeddings



# Usage
if __name__ == "__main__":
    with open("extracted_content.txt", "r", encoding="utf-8") as f:
        extracted_text = f.read()
    
    chunks = preprocess_and_chunk(extracted_text)
    
    embeddings = generate_embeddings(chunks)
    print(f"Number of embeddings generated: {len(embeddings)}")
    print(f"Embedding dimension: {len(embeddings[0])}")
    
    with open("chunks_and_embeddings.pkl", "wb") as f:
        pickle.dump((chunks, embeddings), f)
