import random
import requests
import json
import os

ip_address = "10.110.77.3"
port = "8003"
connect_host = f"{ip_address}:{port}"

last_data_url= f"http://{connect_host}/data/last/"
last_data = requests.get(last_data_url)
last_data = json.loads(last_data.content.decode('utf-8'))

# Generate random float values between 165 and 180
open = random.uniform(165.0, 180.0)
high = random.uniform(165.0, 180.0)
low = random.uniform(165.0, 180.0)
previous_close = random.uniform(165.0, 180.0)

try:
    # Define the data payload for the POST request
    data = {
        "id": last_data['id'] + 1,
        "open": open,
        "high": high,
        "low": low,
        "previous_close": previous_close
    }
except:
    data = {
        "id": 0,
        "open": open,
        "high": high,
        "low": low,
        "previous_close": previous_close
    }

create_data_url= f"http://{connect_host}/data/"
# Make the POST request
response = requests.post(create_data_url, json=data)

last_data_url= f"http://{connect_host}/data/last/"
last_data = requests.get(last_data_url)
last_data = json.loads(last_data.content.decode('utf-8'))

model_data = {
    "open": last_data["open"],
    "high": last_data["high"],
    "low": last_data["low"],
    "previous_close": last_data["previous_close"]
}

model_url= f"http://{connect_host}/model/"
# Make the POST request
response = requests.post(model_url, json=model_data)
print(response.content.decode('utf-8'))
