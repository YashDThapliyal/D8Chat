from langchain.text_splitter import RecursiveCharacterTextSplitter

def preprocess_and_chunk(text, chunk_size=1000, chunk_overlap=200):
    #TODO: Add more preprocessing steps here for robustness
    text = text.replace('\n', ' ').replace('\r', '')


    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
    )
    

    chunks = text_splitter.split_text(text)
    
    return chunks

## Test the function
if __name__ == "__main__":
    with open("extracted_content.txt", "r", encoding="utf-8") as f:
        extracted_text = f.read()
    
    chunks = preprocess_and_chunk(extracted_text)
    print(f"Number of chunks created: {len(chunks)}")
    print(f"Average chunk length: {sum(len(chunk) for chunk in chunks) / len(chunks)}")
