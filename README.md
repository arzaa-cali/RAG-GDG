# RAG-GDG

## 1. Setup

```bash
git clone <repo_url>
cd livecode
python3 -m venv env
source env/bin/activate
```
## 2. Installations
```bash
pip install -r requirements.txt
```
ou

```bash
pip install streamlit langchain-google-genai langchain-chroma langchain-community langchain-classic python-dotenv beautifulsoup4 google-generativeai
```


## 3. API Key
Créez un fichier .env à la racine du projet et ajoutez-y la ligne suivante :

```
GOOGLE_API_KEY=your-api-key
```

## 4. Run

```bash
python3 ingest.py
streamlit run app.py
```
