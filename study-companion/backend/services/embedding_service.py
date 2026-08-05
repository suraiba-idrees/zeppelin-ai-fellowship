from sentence_transformers import SentenceTransformer

# Load the embedding model once
model = SentenceTransformer("all-MiniLM-L6-v2")


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100):
    """
    Split text into overlapping chunks.
    """

    if not text:
        return []

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])

        if end >= len(text):
            break

        start += chunk_size - overlap

    return chunks


def generate_embeddings(chunks):
    """
    Generate embeddings for a list of text chunks.
    """

    if not chunks:
        return []

    embeddings = model.encode(chunks)

    results = []

    for chunk, embedding in zip(chunks, embeddings):
        results.append({
            "text": chunk,
            "embedding": embedding.tolist()
        })

    return results


def process_document(text: str):
    """
    Complete pipeline:
    1. Chunk the text
    2. Generate embeddings
    """

    chunks = chunk_text(text)
    return generate_embeddings(chunks)