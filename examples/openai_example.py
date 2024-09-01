from ethina import OpenAIClient, OpenAIChat

# Create client
provider_keys = {
    "api_key": "your-api-key"
}
client = OpenAIClient(provider_keys)

# Create chat object
chat = OpenAIChat(client)

# Prepare input data
input_data = {
    "model": "gpt-4",
    "messages": [
        {"role": "user", "content": "What are the main features of Python?"}
    ],
    "max_tokens": 800,
    "temperature": 0.7,
    "top_p": 0.95,
    "frequency_penalty": 0,
    "presence_penalty": 0,
    "stop": None,
    "stream": False
}

# Generate response
response = chat.generate(input_data)
print(response)