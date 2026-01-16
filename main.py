# main.py
import uvicorn
from api import app
import os
import logging

SERVER_PORT = int(os.getenv("SERVER_PORT", 8000))
SERVER_HOST = os.getenv("SERVER_HOST", "0.0.0.0")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
)

if __name__ == "__main__":
    print("::: Jina API :::")
    uvicorn.run(app, host=SERVER_HOST, port=SERVER_PORT)
