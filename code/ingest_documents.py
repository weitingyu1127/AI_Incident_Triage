import os
from pathlib import Path

import psycopg
from dotenv import load_dotenv
from openai import OpenAI


# =========================================================
# 1. Configuration
# =========================================================

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

DB_NAME = os.getenv("DB_NAME", "ai_incident_copilot")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")

KNOWLEDGE_BASE_PATH = Path("knowledge_base")

# Chunk settings
CHUNK_SIZE = 250       # words per chunk
CHUNK_OVERLAP = 50     # overlapping words

# Embedding settings
EMBEDDING_MODEL = "text-embedding-3-small" # The embedding model provided by Open AI
EMBEDDING_DIMENSIONS = 1536 # Every embedding can store 1536 digital

# Number of chunks sent to OpenAI per request
BATCH_SIZE = 50

# =========================================================
# 2. Initialize OpenAI Client
# =========================================================

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY not found. "
        "Please add it to your .env file."
    )

client = OpenAI(api_key=OPENAI_API_KEY)

# =========================================================
# 3. Load Markdown Files
# =========================================================

def load_markdown_files():
    documents = []

    for file_path in KNOWLEDGE_BASE_PATH.rglob("*.md"):

        content = file_path.read_text(encoding="utf-8")

        relative_path = file_path.relative_to(
            KNOWLEDGE_BASE_PATH
        )

        category = relative_path.parts[0]

        # Example:
        # file_path = knowledge_base/database/sql_slow_query.md
        # relative_path = database/sql_slow_query.md
        # relative_path.part = (database, sql_slow_query)
        # category = database

        if category == "incidents":
            document_type = "past_incident"
        else:
            document_type = "technical_doc"

        documents.append({
            "content": content,
            "source_file": file_path.name,
            "category": category,
            "document_type": document_type,
        })

    return documents


# =========================================================
# 4. Chunk Text
# =========================================================

def chunk_text(
    text,
    chunk_size=CHUNK_SIZE,
    overlap=CHUNK_OVERLAP,
):

    words = text.split()

    chunks = []

    start = 0

    while start < len(words):

        end = start + chunk_size

        chunk_words = words[start:end]

        chunk = " ".join(chunk_words)

        # Avoid storing empty chunks
        if chunk.strip():
            chunks.append(chunk)

        # Move forward but preserve overlap
        start += chunk_size - overlap

    return chunks


# =========================================================
# 5. Convert Documents Into Chunks
# =========================================================

def create_chunks(documents):

    all_chunks = []

    for document in documents:

        chunks = chunk_text(
            document["content"]
        )

        for chunk_index, chunk in enumerate(chunks):

            all_chunks.append({
                "content": chunk,
                "source_file": document["source_file"],
                "category": document["category"],
                "document_type": document["document_type"],
                "chunk_index": chunk_index,
            })

    return all_chunks


# =========================================================
# 6. Generate Embeddings
# =========================================================

def generate_embeddings(texts):

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts,
        dimensions=EMBEDDING_DIMENSIONS,
    )

    # Sort by index just to make sure
    sorted_data = sorted(
        response.data,
        key=lambda item: item.index
    )

    embeddings = [
        item.embedding
        for item in sorted_data
    ]

    return embeddings


# =========================================================
# 7. Convert Python List → PostgreSQL Vector
# =========================================================

def vector_to_pgvector(vector):

    return "[" + ",".join(
        str(value)
        for value in vector
    ) + "]"


# =========================================================
# 8. Connect to PostgreSQL
# =========================================================

def get_database_connection():

    connection_params = {
        "dbname": DB_NAME,
        "host": DB_HOST,
        "port": DB_PORT,
        "user": DB_USER,
    }

    # Local PostgreSQL may not require password
    if DB_PASSWORD:
        connection_params["password"] = DB_PASSWORD

    return psycopg.connect(
        **connection_params
    )


# =========================================================
# 9. Make Sure Database Schema Exists
# =========================================================

def setup_database(conn):

    with conn.cursor() as cursor:

        cursor.execute(
            """
            CREATE EXTENSION IF NOT EXISTS vector;
            """
        )

        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS documents (
                id BIGSERIAL PRIMARY KEY,
                content TEXT NOT NULL,
                embedding VECTOR(1536),
                source_file TEXT,
                category TEXT,
                document_type TEXT
            );
            """
        )

    conn.commit()


# =========================================================
# 10. Insert Chunk Into Database
# =========================================================

def insert_chunk(
    cursor,
    chunk,
    embedding,
):

    embedding_string = vector_to_pgvector(
        embedding
    )

    cursor.execute(
        """
        INSERT INTO documents (
            content,
            embedding,
            source_file,
            category,
            document_type
        )
        VALUES (
            %s,
            %s::vector,
            %s,
            %s,
            %s
        );
        """,
        (
            chunk["content"],
            embedding_string,
            chunk["source_file"],
            chunk["category"],
            chunk["document_type"],
        )
    )


# =========================================================
# 11. Main Ingestion Process
# =========================================================

def ingest():

    print("========================================")
    print("AI Incident Copilot - Document Ingestion")
    print("========================================")

    # -----------------------------------------------------
    # Load Markdown
    # -----------------------------------------------------

    print("\n1. Loading Markdown files...")

    documents = load_markdown_files()

    print(
        f"Loaded {len(documents)} documents."
    )

    if not documents:
        print(
            "No Markdown files found."
        )
        return

    # -----------------------------------------------------
    # Chunk Documents
    # -----------------------------------------------------

    print("\n2. Creating chunks...")

    chunks = create_chunks(
        documents
    )

    print(
        f"Generated {len(chunks)} chunks."
    )

    # Show example
    # if chunks:

    #     print("\nExample chunk:")
    #     print("-----------------------------------")
    #     print(
    #         "Source:",
    #         chunks[0]["source_file"]
    #     )
    #     print(
    #         "Category:",
    #         chunks[0]["category"]
    #     )
    #     print(
    #         "Chunk index:",
    #         chunks[0]["chunk_index"]
    #     )
    #     print()

    #     print(
    #         chunks[0]["content"][:300]
    #     )

    #     print("\n-----------------------------------")

    # -----------------------------------------------------
    # Database
    # -----------------------------------------------------

    print("\n3. Connecting to PostgreSQL...")

    conn = get_database_connection()

    # setup_database(conn)

    print(
        "Database connected successfully."
    )

    # -----------------------------------------------------
    # Clear Existing Data
    # -----------------------------------------------------

    print("\n4. Clearing old document data...")

    with conn.cursor() as cursor:

        cursor.execute(
            "DELETE FROM documents;"
        )

    conn.commit()

    print(
        "Old data cleared."
    )

    # -----------------------------------------------------
    # Generate Embeddings + Insert
    # -----------------------------------------------------

    print(
        "\n5. Generating embeddings and inserting data..."
    )

    total_chunks = len(chunks)

    for batch_start in range(
        0,
        total_chunks,
        BATCH_SIZE
    ):

        batch_end = min(
            batch_start + BATCH_SIZE,
            total_chunks
        )

        batch = chunks[
            batch_start:batch_end
        ]

        texts = [
            chunk["content"]
            for chunk in batch
        ]

        print(
            f"Processing chunks "
            f"{batch_start + 1} - {batch_end} "
            f"of {total_chunks}"
        )

        # ---------------------------------------------
        # OpenAI Embedding
        # ---------------------------------------------

        embeddings = generate_embeddings(
            texts
        )

        # ---------------------------------------------
        # Insert into PostgreSQL
        # ---------------------------------------------

        with conn.cursor() as cursor:

            for chunk, embedding in zip(
                batch,
                embeddings
            ):

                insert_chunk(
                    cursor,
                    chunk,
                    embedding
                )

        conn.commit()

    # -----------------------------------------------------
    # Verify
    # -----------------------------------------------------

    print("\n6. Verifying database...")

    with conn.cursor() as cursor:

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM documents;
            """
        )

        count = cursor.fetchone()[0]

    conn.close()

    print(
        f"Database contains {count} chunks."
    )

    print("\n========================================")
    print("Ingestion completed successfully!")
    print("========================================")


# =========================================================
# 12. Run
# =========================================================

if __name__ == "__main__":
    ingest()