import streamlit as st
import os
from config import DB_PATH
from database import load_vector_db
from rag_engine import get_ta_response

st.set_page_config(
    page_title="Assistant Virtuel INF1900",
    page_icon="🤖",
    layout="wide"
)

@st.cache_resource
def init_resources():
    if not os.path.exists(DB_PATH):
        return None
    return load_vector_db()

vector_db = init_resources()

with st.sidebar:
    st.header("📚 Chargé de Lab Virtuel INF1900")
    st.markdown("---")
    st.markdown("**Liens Rapides :**")
    st.markdown("- [Site du Cours INF1900](https://cours.polymtl.ca/inf1900/)")
    st.markdown("- [Moodle](https://moodle.polymtl.ca/)")

st.title("🤖 Chargé de Lab Virtuel INF1900")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ex: Comment initialiser le UART sur le ATmega?"):
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    if vector_db:
        with st.spinner("🔍 Recherche dans la documentation..."):
            response_text, source_docs = get_ta_response(prompt, vector_db)
        
        with st.chat_message("assistant"):
            st.markdown(response_text)
            with st.expander("📚 Sources consultées"):
                for i, doc in enumerate(source_docs):
                    source = doc.metadata.get('source', 'Inconnu')
                    st.markdown(f"**Source {i+1}:** `{source}`")
                    st.caption(doc.page_content[:150] + "...")

        st.session_state.messages.append({"role": "assistant", "content": response_text})
    else:
        st.error("Erreur: La base de données n'est pas chargée.")
