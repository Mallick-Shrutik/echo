import requests
from config import HUGGING_FACE_TOKEN

headers = {"Authorization": f"Bearer {HUGGING_FACE_TOKEN}" }

API_URL = "https://api-inference.huggingface.co/models/meta-llama/Meta-Llama-3-8B-Instruct"

prompt = input()
data = {
    "inputs": prompt,
    "parameters": {
        "max_new_tokens": 256, 
        "return_full_text": True,
        "temperature": 0.5,
        "top_p": 0.9,
        "repetition_penalty": 1.5
        },
}

response = requests.post(API_URL, headers=headers, json=data, stream=True)
if response.status_code == 200:
    response_data = response.json()
    generated_text = response_data[0].get("generated_text","")
    if generated_text:
        print(generated_text)
    else:
        print("No response")
    
else:
    print("Error in getting response from the AI model")
