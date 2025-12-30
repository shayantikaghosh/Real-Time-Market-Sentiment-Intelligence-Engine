import requests
import json
import time
import os
import uuid
from datetime import datetime

# Configuration
DATA_DIR = "data/"
FETCH_INTERVAL = 60 # Seconds between API polls

def fetch_mock_or_live_news():
    """
    Simulates a custom connector. 
    In a real scenario, replace the 'mock_news' with an actual API call to NewsAPI.org.
    """
    
    # Example logic for a news stream
    timestamp = datetime.now().isoformat()
    
    # Simulating a dynamic update
    news_item = {
        "title": f"Breaking Tech Update at {timestamp}",
        "content": "Pathway has just released a new post-transformer architecture that processes data streams 10x faster.",
        "source": "TechWire",
        "timestamp": timestamp
    }
    
    filename = os.path.join(DATA_DIR, f"news_{uuid.uuid4().hex[:8]}.json")
    
    with open(filename, 'w') as f:
        json.dump(news_item, f)
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Ingested new data: {filename}")

if __name__ == "__main__":
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
        
    print("Custom Ingestor started. Press Ctrl+C to stop.")
    try:
        while True:
            fetch_mock_or_live_news()
            time.sleep(FETCH_INTERVAL)
    except KeyboardInterrupt:
        print("Ingestor stopped.")