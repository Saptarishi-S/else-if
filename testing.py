
import requests
import json
import os
from dotenv import load_dotenv
from prompt_enhance import enhancer

load_dotenv()

# api_key = os.getenv('API_KEY')
api_key = "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"
model = "claude-v1.3-100k"
conversation_history = ""

def chat_with_ai(user_question, api_key, model):
    global conversation_history

    # Instantiate the endpoint URL
    url = 'https://api.anthropic.com/v1/complete'

    # Define the headers for the HTTP request
    headers = {
        'Content-Type': 'application/json',
        'X-API-Key': api_key,
    }

    # Define the parameters for the request
    params = {
        'prompt': f'{conversation_history}\n\nHuman: {user_question}\n\nAssistant:',
        'model': model,
        'max_tokens_to_sample': 4000,
        'stop_sequences': ['\n\nHuman:'],
        'temperature': 0.8,
        'top_p': -1,
        'metadata': {}
    }

    # Convert the params dict to a JSON string
    params_json = json.dumps(params)

    # Send the HTTP request to the API
    response = requests.post(url, headers=headers, data=params_json)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON response
        response_json = response.json()
        # conversation_history += f'\n\n{response_json["completion"]}'
        conversation_history = f'\n\n{response_json["completion"]}'
        return conversation_history
    else:
        return f'Error: {response.status_code}'

# Example usage:
while True:
    user_input = input("Enter your question: ")
    if user_input=="quit()":
        break
    user_prompt=enhancer(user_input)
    response=None
    response = chat_with_ai(user_prompt, api_key, model)
    print(response)
