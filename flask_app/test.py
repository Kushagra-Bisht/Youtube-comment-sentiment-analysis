import requests
import json

# The base URL of your Flask application
url = "http://127.0.0.1:5000/predict"

# Example data in the correct format
data = {
        "comments": ["This is a great product!", "Not worth the money.", "It's okay."]
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
