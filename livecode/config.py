import os
from dotenv import load_dotenv

load_dotenv()

DB_PATH = "./inf1900_db"
ENTRY_URL = "https://cours.polymtl.ca/inf1900/"
EMBEDDING_MODEL = "gemini-embedding-001"
LLM_MODEL = "gemini-flash-latest" # peut être changé pour "gemini-pro-latest" si vous avez accès à ce modèle plus puissant