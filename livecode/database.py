from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import DB_PATH, EMBEDDING_MODEL

def get_embeddings():
    # TODO 3: Initialize and return the Google Generative AI Embeddings
    pass

def create_vector_db(docs):
    # TODO 4: Initialize the text splitter (chunk_size=2000, chunk_overlap=200)

    # TODO 5: Create and return the Chroma vector store from the documents
    pass

def load_vector_db():
    # TODO 6: Load the existing Chroma vector store
    pass
