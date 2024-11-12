import requests
import json

# The base URL of your Flask application
url = "http://127.0.0.1:5000/predict_with_timestamps"

# Example data in the correct format
data = {
        "comments": [
            {"text": "This is fantastic!", "timestamp": "2024-10-25 10:00:00"},
            {"text": "Could be better.", "timestamp": "2024-10-26 14:00:00"}
        ]
    }

# Send a POST request
response = requests.post(url, json=data)

# Check the response status and content
if response.status_code == 200:
    print("Request was successful!")
    print("Response data:", response.json())
else:
    print(f"Request failed with status code: {response.status_code}")
    print("Error message:", response.text)
