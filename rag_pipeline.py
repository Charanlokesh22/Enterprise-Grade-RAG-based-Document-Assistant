
from langchain.chat_models import AzureChatOpenAI
from langchain.chains import RetrievalQA
from app.retriever import get_retriever
from app.config import Config

def create_rag_pipeline():
    retriever = get_retriever()
    llm = AzureChatOpenAI(
        deployment_name=Config.AZURE_DEPLOYMENT_NAME,
        openai_api_base=Config.AZURE_OPENAI_ENDPOINT,
        openai_api_version="2023-05-15",
        openai_api_key=Config.AZURE_OPENAI_KEY,
        temperature=0
    )
    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)
    return qa_chain

def ask_question(question: str):
    qa = create_rag_pipeline()
    return qa.run(question)
