import requests

url = "http://0.0.0.0:5000"

response = requests.get(f"{url}/health")
assert response.status_code == 200
assert response.content == b"OK"

print("OK")