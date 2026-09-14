import os

from dotenv import load_dotenv
from openai import OpenAI

# Reuse the vector search we already built
from search import search_documents


# =========================================================
# 1. Configuration
# =========================================================

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

LLM_MODEL = "gpt-5.6-luna"

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
# 3. Build Context
# =========================================================

def build_context(results):

    context_parts = []

    for index, row in enumerate(
        results,
        start=1
    ):
        # tuple unpacking: put the value row[0] ~ row[x] into paramters, so it easier to know the defination of value
        (
            document_id,
            content,
            source_file,
            category,
            document_type,
            similarity
        ) = row

        context_part = f"""
                [Context {index}]
                Source: {source_file}
                Category: {category}
                Document Type: {document_type}
                Similarity: {similarity:.4f}

                Content:
                {content}
            """

        context_parts.append(
            context_part
        )

    context = "\n".join(
        context_parts
    )

    return context


# =========================================================
# 4. Get Unique Sources
# =========================================================

def get_sources(results):

    sources = []

    for row in results:

        source_file = row[2]

        if source_file not in sources:
            sources.append(
                source_file
            )

    return sources


# =========================================================
# 5. Generate Answer
# =========================================================

def generate_answer(
    question,
    context
):

    instructions = """
        You are an AI incident troubleshooting assistant.

        Answer the user's question using ONLY the provided context.

        Rules:
        1. Do not use outside knowledge.
        2. If the context does not contain enough information, clearly say that there is not enough information.
        3. Explain the likely cause clearly and concisely.
        4. Give recommended troubleshooting steps when supported by the context.
        5. When using information from a document, mention the source filename in brackets.

        Example:
        A missing database index may cause the slowdown [sql_slow_query.md].
    """

    prompt = f"""
        User Question: {question}

        Retrieved Context: {context}

        Answer the user's question based on the retrieved context.
    """

    response = client.responses.create(
        model=LLM_MODEL,
        instructions=instructions,
        input=prompt,
        reasoning={
            "effort": "low"
        },
        store=False
    )

    return response.output_text


# =========================================================
# 6. RAG Pipeline
# =========================================================

def ask_rag(question):

    # ----------------------------------------
    # Step 1: Retrieve relevant chunks
    # ----------------------------------------

    results = search_documents(
        question,
        top_k=TOP_K
    )

    if not results:
        return (
            "No relevant documents found.",
            [],
            []
        )

    # ----------------------------------------
    # Step 2: Build context
    # ----------------------------------------

    context = build_context(
        results
    )

    # ----------------------------------------
    # Step 3: Send context + question to LLM
    # ----------------------------------------

    answer = generate_answer(
        question,
        context
    )

    # ----------------------------------------
    # Step 4: Collect sources
    # ----------------------------------------

    sources = get_sources(
        results
    )

    return (
        answer,
        sources,
        results
    )


# =========================================================
# 7. Display Retrieval Debug Information
# =========================================================

def print_retrieval_results(results):

    print("\nRetrieved Documents")
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

        print(
            f"{rank}. "
            f"{source_file} "
            f"(similarity: {similarity:.4f})"
        )


# =========================================================
# 8. Main
# =========================================================

def main():

    print(
        "AI Incident Copilot - RAG"
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
            "\nSearching knowledge base..."
        )

        answer, sources, results = ask_rag(
            question
        )

        # Show retrieval results
        print_retrieval_results(
            results
        )

        # Show final LLM answer
        print("\nAI Answer")
        print("========================================")

        print(answer)

        # Show source files
        print("\nSources")
        print("========================================")

        for source in sources:
            print(
                f"- {source}"
            )


# =========================================================
# 9. Run
# =========================================================

if __name__ == "__main__":
    main()