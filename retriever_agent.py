from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings

def get_retriever():
    embeddings = OpenAIEmbeddings()
    return FAISS.load_local("faiss_index", embeddings)
