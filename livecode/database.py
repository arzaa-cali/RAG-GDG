from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import DB_PATH, EMBEDDING_MODEL

def get_embeddings():
    # TODO 3: Initialize and return the Google Generative AI Embeddings
    return GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)

def create_vector_db(docs):
    # TODO 4: Initialize the text splitter (chunk_size=2000, chunk_overlap=200)
    splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    print(f"Splitting {len(docs)} documents into chunks...")
    
    # TODO 5: Create and return the Chroma vector store from the documents
    vector_db = Chroma.from_documents(
        documents=splitter.create_documents([d.page_content for d in docs]),
        embedding=get_embeddings(),
        persist_directory=DB_PATH
    )
    return vector_db

def load_vector_db():
    # TODO 6: Load the existing Chroma vector store
    return Chroma(persist_directory=DB_PATH, embedding_function=get_embeddings())
