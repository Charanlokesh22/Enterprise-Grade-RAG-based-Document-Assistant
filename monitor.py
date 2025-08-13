
from app.config import Config
import whylogs as why
from arize.pandas.logger import Client
import pandas as pd

def log_to_whylabs(text, prediction):
    profile = why.log(pandas=pd.DataFrame({"text": [text], "prediction": [prediction]}))
    profile.writer("whylabs").option("org_id", Config.WHYLABS_ORG_ID).option("dataset_id", Config.WHYLABS_DATASET_ID).option("api_key", Config.WHYLABS_API_KEY).write()

def log_to_arize(text, prediction):
    client = Client(space_key=Config.ARIZE_SPACE_KEY, api_key=Config.ARIZE_API_KEY)
    df = pd.DataFrame({"text": [text], "prediction": [prediction]})
    client.log_dataframe(df=df, model_id="rag-doc-assistant", model_version="1.0", model_type="llm")
