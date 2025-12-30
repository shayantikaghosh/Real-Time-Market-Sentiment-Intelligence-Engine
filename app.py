import pathway as pw
from pathway.xpacks.llm.vector_store import VectorStoreServer
from pathway.xpacks.llm.embedders import OpenAIEmbedder
from pathway.xpacks.llm.llms import OpenAIChat
import os
from dotenv import load_dotenv

# Load environment variables (API Keys)
load_dotenv()

def run_live_intelligence_system():
    """
    Core Pathway pipeline that implements a Dynamic RAG.
    It monitors a data directory and updates the vector store in real-time.
    """
    
    # 1. LIVE DATA INGESTION
    # We use Pathway's JSON connector in 'streaming' mode.
    # It watches the 'data/' directory for new, modified, or deleted files.
    raw_data = pw.io.json.read(
        "data/",
        schema=pw.schema_from_dict({
            "title": str,
            "content": str,
            "source": str,
            "timestamp": str
        }),
        mode="streaming" 
    )

    # 2. STREAMING TRANSFORMATIONS
    # We add a metadata field for the LLM to understand source credibility
    enriched_data = raw_data.select(
        *pw.this,
        doc_content = pw.this.title + ": " + pw.this.content,
        metadata = pw.dict(
            source=pw.this.source,
            received_at=pw.this.timestamp
        )
    )

    # 3. REAL-TIME VECTOR INDEXING
    # Using OpenAI for embeddings. This index updates incrementally.
    embedder = OpenAIEmbedder(
        api_key=os.environ.get("OPENAI_API_KEY"),
        model="text-embedding-3-small"
    )

    # Setup the Vector Store Server
    # This exposes a REST API that can be queried by a frontend or CLI
    server = VectorStoreServer(
        enriched_data,
        embedder=embedder,
    )

    # 4. START THE INCREMENTAL ENGINE
    print("Pathway engine is starting...")
    print("Monitoring 'data/' folder for real-time updates...")
    pw.run()

if __name__ == "__main__":
    # Ensure data directory exists
    if not os.path.exists("data"):
        os.makedirs("data")
    run_live_intelligence_system()