import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# STARTS FROM HERE !!
from ethina import AzureOpenAIClient, AzureOpenAIChat# Create client
provider_keys = {
    "base": "BASE_URL",
    "api_key": "API_KEY",
    "api_version": "API_VERSION"
}
client = AzureOpenAIClient(provider_keys)

# Create chat object
chat = AzureOpenAIChat(client)
stream = True
# Prepare input data
input_data = {
    "model": "DEPLOYMENT_NAME",
    "messages": [
        {"role": "user", "content": "What are the differences between Azure Machine Learning and Azure AI services?"}
    ],
    "max_tokens": 800,
    "temperature": 0.7,
    "top_p": 0.95,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "stop": None,
    "stream": stream
}

# Generate response
response = chat.generate(input_data)
if stream:
    for chunk in response:
        print(chunk)
else:
    print(response)