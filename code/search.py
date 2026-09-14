import os

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

EMBEDDING_MODEL = "text-embedding-3-small"
EMBEDDING_DIMENSIONS = 1536

TOP_K = 5


# =========================================================
# 2. OpenAI Client
# =========================================================

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY not found. "
        "Please check your .env file."
    )

client = OpenAI(
    api_key=OPENAI_API_KEY
)


# =========================================================
# 3. Connect to PostgreSQL
# =========================================================

def get_database_connection():

    connection_params = {
        "dbname": DB_NAME,
        "host": DB_HOST,
        "port": DB_PORT,
        "user": DB_USER,
    }

    if DB_PASSWORD:
        connection_params["password"] = DB_PASSWORD

    return psycopg.connect(
        **connection_params
    )


# =========================================================
# 4. Generate Question Embedding
# =========================================================

def generate_embedding(text):

    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=text,
        dimensions=EMBEDDING_DIMENSIONS,
    )

    embedding = response.data[0].embedding

    return embedding


# =========================================================
# 5. Convert Python List → PostgreSQL Vector
# =========================================================

def vector_to_pgvector(vector):

    return "[" + ",".join(
        str(value)
        for value in vector
    ) + "]"


# =========================================================
# 6. Search Similar Chunks
# =========================================================

def search_documents(
    question,
    top_k=TOP_K
):

    # ----------------------------------------
    # Step 1: Question → Embedding
    # ----------------------------------------

    question_embedding = generate_embedding(
        question
    )

    embedding_string = vector_to_pgvector(
        question_embedding
    )

    # ----------------------------------------
    # Step 2: Connect DB
    # ----------------------------------------

    conn = get_database_connection()

    # ----------------------------------------
    # Step 3: Vector Similarity Search
    # ----------------------------------------

    with conn.cursor() as cursor:

        cursor.execute(
            """
            SELECT
                id,
                content,
                source_file,
                category,
                document_type,
                1 - (
                    embedding <=> %s::vector
                ) AS similarity
            FROM documents
            WHERE embedding IS NOT NULL
            ORDER BY embedding <=> %s::vector
            LIMIT %s;
            """,
            (
                embedding_string,
                embedding_string,
                top_k
            )
        )

        results = cursor.fetchall()

    conn.close()

    return results


# =========================================================
# 7. Display Results
# =========================================================

def print_results(results):

    if not results:
        print("No results found.")
        return

    print("\n========================================")
    print("Top Matching Documents")
    print("========================================")

    for rank, row in enumerate(
        results,
        start=1
    ):

        (
            document_id,
            content,
            source_file,
            category,
            document_type,
            similarity
        ) = row

        print(f"\nResult #{rank}")
        print("----------------------------------------")

        print(
            f"ID: {document_id}"
        )

        print(
            f"Source: {source_file}"
        )

        print(
            f"Category: {category}"
        )

        print(
            f"Type: {document_type}"
        )

        print(
            f"Similarity: {similarity:.4f}"
        )

        print("\nContent:")

        print(content)

        print("----------------------------------------")


# =========================================================
# 8. Main
# =========================================================

def main():

    print(
        "AI Incident Copilot - Vector Search"
    )

    print(
        "Type 'exit' to quit."
    )

    while True:

        question = input(
            "\nEnter your question: "
        ).strip()

        if question.lower() == "exit":
            print("Goodbye.")
            break

        if not question:
            print(
                "Please enter a question."
            )
            continue

        print(
            "\nSearching..."
        )

        results = search_documents(
            question
        )

        print_results(
            results
        )


# =========================================================
# 9. Run
# =========================================================

if __name__ == "__main__":
    main()