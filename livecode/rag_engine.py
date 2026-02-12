from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.prompts import PromptTemplate
from langchain_classic.chains import LLMChain
from config import LLM_MODEL

def get_llm():
    # TODO 7: Initialize the ChatGoogleGenerativeAI with the model and temperature
    pass

def get_rag_chain():
    # TODO 8: Define the prompt template
    
    # TODO 9: Create the LLMChain with the LLM and the prompt
    pass

def get_ta_response(question, vector_db):
    # TODO 10: Perform similarity search on the vector database
    
    # TODO 11: Run the RAG chain
    pass
