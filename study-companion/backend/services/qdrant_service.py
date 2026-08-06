import os
import uuid
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import Distance, PointStruct, VectorParams

from services.embedding_service import model as embedding_model

# Load environment variables
load_dotenv()

# Initialize Qdrant client
# Use remote Qdrant if QDRANT_URL is available, otherwise use in-memory storage.
qdrant_url = os.getenv("QDRANT_URL")
if qdrant_url:
    client = QdrantClient(url=qdrant_url)
else:
    client = QdrantClient(":memory:")

COLLECTION_NAME = "study_notes"

# Dynamically match the embedding model's real output dimension
# (all-MiniLM-L6-v2 -> 384). This removes the hardcoded-mismatch bug
# and stays correct even if the embedding model is changed later.
VECTOR_SIZE = embedding_model.get_sentence_embedding_dimension()


def create_collection(vector_size: int = VECTOR_SIZE) -> None:
    """
    Create the Qdrant collection if it does not already exist.
    """
    try:
        if client.collection_exists(COLLECTION_NAME):
            print(f"Collection '{COLLECTION_NAME}' already exists.")
            return

        client.create_collection(
            collection_name=COLLECTION_NAME,
            vectors_config=VectorParams(
                size=vector_size,
                distance=Distance.COSINE,
            ),
        )

        print(f"Collection '{COLLECTION_NAME}' created successfully.")

    except Exception as e:
        print(f"Error creating collection: {e}")
        raise


def insert_vector(vector: list[float], text: str) -> None:
    """
    Insert a single vector and its corresponding text into Qdrant.
    Kept for simple/manual use (also used by the __main__ self-test below).
    """
    try:
        unique_id = str(uuid.uuid4())

        client.upsert(
            collection_name=COLLECTION_NAME,
            points=[
                PointStruct(
                    id=unique_id,
                    vector=vector,
                    payload={
                        "text": text
                    },
                )
            ],
        )

        print(f"Vector inserted successfully with ID: {unique_id}")

    except Exception as e:
        print(f"Error inserting vector: {e}")
        raise


def insert_chunks(chunks_with_embeddings: list[dict]) -> int:
    """
    Batch-insert chunk texts + embeddings, as produced by
    embedding_service.process_document(), into Qdrant in a single
    upsert call. Returns the number of points inserted.

    Expects each item to look like: {"text": str, "embedding": list[float]}
    """
    if not chunks_with_embeddings:
        return 0

    try:
        points = [
            PointStruct(
                id=str(uuid.uuid4()),
                vector=item["embedding"],
                payload={"text": item["text"]},
            )
            for item in chunks_with_embeddings
        ]

        client.upsert(
            collection_name=COLLECTION_NAME,
            points=points,
        )

        print(f"Inserted {len(points)} chunks into '{COLLECTION_NAME}'.")
        return len(points)

    except Exception as e:
        print(f"Error inserting chunks: {e}")
        raise


def search_vectors(query_vector: list[float], limit: int = 3) -> list[str]:
    """
    Search the Qdrant collection and return the most relevant text chunks.

    Supports both newer and older versions of the Qdrant client.
    """
    retrieved_chunks: list[str] = []

    try:
        # Preferred API (newer client versions)
        results = client.search(
            collection_name=COLLECTION_NAME,
            query_vector=query_vector,
            limit=limit,
        )

        for point in results:
            if point.payload and "text" in point.payload:
                retrieved_chunks.append(point.payload["text"])

        return retrieved_chunks

    except AttributeError:
        # Fallback for client versions using query_points()
        results = client.query_points(
            collection_name=COLLECTION_NAME,
            query=query_vector,
            limit=limit,
        )

        for point in results.points:
            if point.payload and "text" in point.payload:
                retrieved_chunks.append(point.payload["text"])

        return retrieved_chunks

    except Exception as e:
        print(f"Error searching vectors: {e}")
        raise


if __name__ == "__main__":
    # Local validation
    create_collection()

    dummy_vector = [0.1] * VECTOR_SIZE

    insert_vector(
        dummy_vector,
        "Operating Systems introduction"
    )

    results = search_vectors(dummy_vector)

    print(f"Retrieved Chunks: {results}")