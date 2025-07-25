from autogen_ext.models.openai import OpenAIChatCompletionClient
from config.constants import MODEL_OPENAI
import os

def getOpenAIModelClient():
    model_client_openai = OpenAIChatCompletionClient(
        model=MODEL_OPENAI,
        api_key=os.getenv('OPENAI_API_KEY')
    )
    
    return model_client_openai