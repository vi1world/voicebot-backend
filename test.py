import requests

SERVER_URL = "http://localhost:31330"
prompt = "What is the capital of France?"

response = requests.post(f"{SERVER_URL}/generate", json={"prompt": prompt})
generated_text = response.json().get("generated_text")

print(f"Response: {generated_text}")
