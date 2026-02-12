from config import ENTRY_URL
from scraper import scrape_website
from database import create_vector_db

def run_ingestion():
    raw_docs = scrape_website(ENTRY_URL)
    create_vector_db(raw_docs)

if __name__ == "__main__":
    run_ingestion()
