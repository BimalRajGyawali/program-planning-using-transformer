import os
import time

from openai import AzureOpenAI

import helper

client = AzureOpenAI(
    api_key=os.environ['AZURE_OPEN_API_KEY'],
    api_version=os.environ['AZURE_API_VERSION'],
    azure_endpoint=os.environ['AZURE_OPEN_API_URL'],
    azure_deployment=os.environ['AZURE_DEPLOYMENT_NAME']
)

AZURE_MODEL_NAME = os.environ['AZURE_MODEL_NAME']  # gpt40


@helper.retry_on_exception
def complete_chat(messages):
    response = client.chat.completions.create(
        model=AZURE_MODEL_NAME,
        messages=messages,

    )
    return response.choices[0].message.content
