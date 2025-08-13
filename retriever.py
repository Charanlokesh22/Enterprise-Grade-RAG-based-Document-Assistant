
from langchain.vectorstores import Pinecone
from langchain.embeddings import OpenAIEmbeddings
import pinecone
from app.config import Config

def get_retriever():
    pinecone.init(api_key=Config.PINECONE_API_KEY, environment=Config.PINECONE_ENV)
    embeddings = OpenAIEmbeddings(deployment=Config.AZURE_DEPLOYMENT_NAME)
    vectorstore = Pinecone.from_existing_index("enterprise-doc-index", embeddings)
    return vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 3})
