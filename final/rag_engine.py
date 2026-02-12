from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_classic.prompts import PromptTemplate
from langchain_classic.chains import LLMChain
from config import LLM_MODEL

def get_llm():
    return ChatGoogleGenerativeAI(model=LLM_MODEL, temperature=0.3)

def get_rag_chain():
    ta_prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
        Tu es un chargé de laboratoire (TA) utile et patient pour le cours INF1900 (Projet de systèmes embarqués) à Polytechnique Montréal.
        Ton but est de guider l'étudiant vers la réponse sans faire le travail à sa place.

        CONTEXTE (Tiré du site web du cours et des manuels):
        {context}

        QUESTION DE L'ÉTUDIANT:
        {question}

        DIRECTIVES:
        1. **Pédagogie:** Ne donne JAMAIS le code complet. Explique la logique ou donne un petit exemple.
        2. **Sources:** Si le contexte mentionne un PDF spécifique (ex: "TP1.pdf") ou une page de datasheet, cite-le.
        3. **Matériel:** Si la question porte sur le ATmega324PA, mentionne les registres spécifiques (DDRA, PORTA, etc.) si pertinent.
        4. **Ton:** Académique, encourageant, professionnel.
        5. **Langue:** Réponds dans la même langue que l'étudiant (Français ou Anglais).

        RÉPONSE:
        """
    )
    return LLMChain(llm=get_llm(), prompt=ta_prompt)

def get_ta_response(question, vector_db):
    print(f"\nQuerying Vector DB for: '{question}'")
    docs = vector_db.similarity_search(question, k=5)
    
    print(f"Found {len(docs)} relevant chunks. Top sources:")
    for i, d in enumerate(docs):
        source = d.metadata.get('source', 'Unknown')
        print(f"   [{i+1}] {source}")

    context_text = "\n\n---\n\n".join([d.page_content for d in docs])
    
    print(f"\nGenerating response using {LLM_MODEL}...")
    chain = get_rag_chain()
    response = chain.run(context=context_text, question=question)
    
    return response, docs