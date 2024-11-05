import json
import requests

API_TOKEN = "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"
headers = {"Authorization": f"Bearer {API_TOKEN}"}
API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
# API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
# headers = {"Authorization": "Bearer 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"}

def query(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

data = query("input.flac")
print(data)
