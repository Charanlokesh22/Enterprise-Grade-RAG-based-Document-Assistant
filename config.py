import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    AZURE_OPENAI_KEY = os.getenv("AZURE_OPENAI_KEY")
    AZURE_OPENAI_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
    AZURE_DEPLOYMENT_NAME = os.getenv("AZURE_DEPLOYMENT_NAME")

    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_ENV = os.getenv("PINECONE_ENV")

    ARIZE_API_KEY = os.getenv("ARIZE_API_KEY")
    ARIZE_SPACE_KEY = os.getenv("ARIZE_SPACE_KEY")

    WHYLABS_API_KEY = os.getenv("WHYLABS_API_KEY")
    WHYLABS_ORG_ID = os.getenv("WHYLABS_ORG_ID")
    WHYLABS_DATASET_ID = os.getenv("WHYLABS_DATASET_ID")
