
from langchain.agents import initialize_agent, Tool
from langchain.chat_models import AzureChatOpenAI
from app.rag_pipeline import ask_question
from app.config import Config

def run_agent(query: str):
    llm = AzureChatOpenAI(
        deployment_name=Config.AZURE_DEPLOYMENT_NAME,
        openai_api_base=Config.AZURE_OPENAI_ENDPOINT,
        openai_api_version="2023-05-15",
        openai_api_key=Config.AZURE_OPENAI_KEY,
        temperature=0
    )

    tools = [
        Tool(
            name="Document Search",
            func=ask_question,
            description="Search and answer questions from enterprise documents."
        )
    ]

    agent = initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)
    return agent.run(query)
