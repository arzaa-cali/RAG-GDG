from config import ENTRY_URL
from scraper import scrape_website
from database import create_vector_db

def run_ingestion():
    # TODO 1: Scrape the website to get raw documents

    raw_documents = scrape_website(ENTRY_URL)
    print(f"Scraped {len(raw_documents)} documents from the website.")

    # TODO 2: Create the vector database from the raw documents
    create_vector_db(raw_documents)
    print("Vector database created.")


if __name__ == "__main__":
    run_ingestion()
