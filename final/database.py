from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import DB_PATH, EMBEDDING_MODEL

def get_embeddings():
    return GoogleGenerativeAIEmbeddings(model=EMBEDDING_MODEL)

def create_vector_db(docs):
    print(f"\nSplitting {len(docs)} documents...")
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=200)
    splits = text_splitter.split_documents(docs)
    
    print(f"Created {len(splits)} text chunks.")
    print(f"\nGenerating embeddings ({EMBEDDING_MODEL})...")
    
    sample_vector = get_embeddings().embed_query("INF1900")
    
    print(f"Vector Preview (first 5 dims): {sample_vector[:5]}...")
    print(f"Total dimensions: {len(sample_vector)}")
    print(f"\nSaving to database at: {DB_PATH}")
    
    return Chroma.from_documents(
        documents=splits,
        embedding=get_embeddings(),
        persist_directory=DB_PATH
    )

def load_vector_db():
    return Chroma(
        persist_directory=DB_PATH, 
        embedding_function=get_embeddings()
    )