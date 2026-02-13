# RAG-GDG

Chatbot basé sur l’architecture RAG (Retrieval-Augmented Generation) développé avec LangChain, Google Gemini, ChromaDB et Streamlit. Ce projet illustre comment construire un assistant intelligent capable de rechercher des informations pertinentes dans une base documentaire avant de générer une réponse.


## 1. Setup

### 1.1 MacOS
```bash
git clone <repo_url>
cd livecode
python3 -m venv env
source env/bin/activate
```

### 1.2 Windows
```bash
git clone <repo_url>
cd livecode
python -m venv env
env\Scripts\activate
```
## 2. Installations
```bash
pip install streamlit langchain-google-genai langchain-chroma langchain-community langchain-classic python-dotenv beautifulsoup4 google-generativeai
```


## 3. API Key
Créez un fichier .env à la racine du projet et ajoutez-y la ligne suivante :

```
GOOGLE_API_KEY=your-api-key
```

## 4. Run
### 4.1 MacOS
```bash
python3 ingest.py
streamlit run app.py
```

### 4.2 Windows
```bash
python ingest.py
streamlit run app.py
```