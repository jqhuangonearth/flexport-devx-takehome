import json
import requests

mapping = ["Rock", "Paper", "Scissors"]
url = "http://0.0.0.0:5000"

for i in range(3):  # Test all possible cases
    all_results = set()
    all_pc_choices = set()
    while len(all_results) < 3 or len(all_pc_choices) < 3:
        headers = {'Content-type': 'application/json'}
        response = requests.post(
            f"{url}/rps",
            headers=headers,
            data=json.dumps(dict(move=mapping[i]))
        )
        assert response.status_code == 200
        
        obj = response.json()

        assert obj["game_result"] in [-1, 0, 1]
        assert obj["pc_choice"] in [0, 1, 2]
        all_results.add(obj["game_result"])
        all_pc_choices.add(obj["pc_choice"])

print("OK")