# Infrastructure for Retrieval-Augmented Generation (RAG) using ChromaDB as a Vector Database

# Passo 1: Installare le dipendenze
# Per realizzare questa infrastruttura, è necessario installare alcune librerie:
# - `chromadb`: per gestire il Vector Store
# - `langchain`: per l'integrazione con il modello LLM e la catena di retrieval
# - `groq`: per utilizzare i modelli Groq per la generazione
# - `ollama`: per creare gli embedding

# Comandi di installazione:
# !pip install chromadb langchain groq ollama

from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from app.my_agent.groq_v2 import GroqLlama
from langchain.prompts import PromptTemplate
from langchain.text_splitter import CharacterTextSplitter

class RAGChromaPipeline:
    def __init__(self, model_name="groq-llm", chunk_size=1000, chunk_overlap=100):
        # Inizializzazione dei componenti principali
        GroqLlama()
        self.embeddings = OllamaEmbeddings( model="llama3")
        self.text_splitter = CharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        self.vector_store = None
        self.llm = GroqLlama().model
        self.retriever = None
        self.qa_chain = None

    def ingest_text(self, text, label):
        """
        Ingestione di testo puro nella knowledge base (vector DB) con una label specifica.
        - text: il testo da suddividere e caricare nel vector store
        - label: la label per identificare la knowledge base
        """
        
        self.vector_store = Chroma.from_texts(text, self.embeddings, collection_name=label)

        self.retriever = self.vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 5})

    def create_qa_chain(self):
        """
        Configurare la catena RAG per il QA.
        """
        if not self.retriever:
            raise ValueError("Il retriever non è stato ancora inizializzato. Assicurarsi di aver caricato del testo nel vector store.")
        self.qa_chain = RetrievalQA(
            llm=self.llm,
            retriever=self.retriever,
            return_source_documents=False
        )

    def get_answer(self, query):
        """
        Utilizzare la catena RAG per ottenere una risposta a una query.
        - query: la domanda da porre alla knowledge base
        """
        if not self.qa_chain:
            raise ValueError("La catena QA non è stata ancora creata. Assicurarsi di aver creato la catena con il metodo create_qa_chain().")
        result = self.qa_chain.run(query)
        return result

