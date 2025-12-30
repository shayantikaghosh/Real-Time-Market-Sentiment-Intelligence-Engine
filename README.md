LivePulse: Real-Time Market Intelligence Engine

Developed for the Pathway "Live AI" Hackathon, LivePulse is a dynamic Retrieval-Augmented Generation (RAG) application that provides instant insights into breaking news. Unlike traditional RAG systems with stale knowledge bases, LivePulse uses the Pathway framework to process data streams incrementally, ensuring the LLM always reasons over the absolute latest information.

🚀 Key Features

Streaming RAG: Automatically updates its vector index as new data arrives.

Dynamic Ingestion: Custom Python connector fetching live data from News APIs.

Incremental Processing: Built on Pathway's Rust-powered engine for low-latency updates.

Demonstrable Dynamism: Response logic changes instantly when source JSON files are modified.

🛠️ Architecture

Ingestion Layer: ingestor.py fetches live headlines and writes them to a monitored directory.

Processing Layer: app.py uses Pathway to watch the directory, perform streaming transformations, and maintain a live vector store.

Retrieval Layer: A REST API endpoint (provided by Pathway's VectorStoreServer) for querying the real-time knowledge base.

🏃 Quick Start

1. Prerequisites

Python 3.10+

OpenAI API Key

2. Setup

# Clone the repository
git clone <your-repo-link>
cd live-pulse

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY


3. Running the Project

Open two terminals:

Terminal 1 (Data Ingestor):

python ingestor.py


Terminal 2 (Pathway Engine):

python app.py


📊 Demonstrating "Liveness"

To prove the real-time capability to judges:

Ask the bot a question about a very recent event not in its training data.

Add a new .json file to the data/ folder containing specific info about that event.

Re-ask the question
