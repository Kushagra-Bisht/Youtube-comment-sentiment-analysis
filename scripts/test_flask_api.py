import pytest
import requests
import json

BASE_URL = "http://localhost:5000"# Replace with your deployed URL if needed

def test_generate_chart_endpoint():
    data = {
        "sentiment_counts": {"1": 5, "0": 3, "-1": 2}
    }
    response = requests.post(f"{BASE_URL}/generate_chart", json=data)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "image/png"

def test_generate_wordcloud_endpoint():
    data = {
        "comments": ["Love this!", "Not so great.", "Absolutely amazing!", "Horrible experience."]
    }
    response = requests.post(f"{BASE_URL}/generate_wordcloud", json=data)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "image/png"

def test_generate_trend_graph_endpoint():
    data = {
        "sentiment_data": [
            {"timestamp": "2024-10-01", "sentiment": 1},
            {"timestamp": "2024-10-02", "sentiment": 0},
            {"timestamp": "2024-10-03", "sentiment": -1}
        ]
    }
    response = requests.post(f"{BASE_URL}/generate_trend_graph", json=data)
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "image/png"