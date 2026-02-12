from langchain_community.document_loaders import RecursiveUrlLoader
from bs4 import BeautifulSoup

def scrape_website(url):
    loader = RecursiveUrlLoader(
        url=url,
        max_depth=3,
        extractor=lambda x: BeautifulSoup(x, "html.parser").get_text(separator="\n", strip=True),
        prevent_outside=True 
    )
    return loader.load()
