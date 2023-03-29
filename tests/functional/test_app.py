import json

from rock_paper_scissors.app import app


def test_health():
    """
    Test Flask Application and API for health
    """
    with app.test_client() as test_client:
        response = test_client.get("/health")
        assert response.status_code == 200
        assert response.data == b"OK"


def test_rps_expected_cases():
    """
    Test Flask Application and API for Rock Paper Scissors
    """

    with app.test_client() as test_client:
        mapping = ["Rock", "Paper", "Scissors"]

        for i in range(3):  # Test all possible cases
            all_results = set()
            all_pc_choices = set()
            while len(all_results) < 3 or len(all_pc_choices) < 3:
                response = test_client.post(
                    "/rps",
                    data=json.dumps(dict(move=mapping[i])),
                    content_type="application/json",
                )
                assert response.status_code == 200
                print(response.json)
                assert response.json["game_result"] in [-1, 0, 1]
                assert response.json["pc_choice"] in [0, 1, 2]
                all_results.add(response.json["game_result"])
                all_pc_choices.add(response.json["pc_choice"])


def test_rps_exception_cases():
    """
    Test Flask Application and API for exception cases
    """
    invalid_moves = [" ", "Rockk", "ro"]
    with app.test_client() as test_client:
        for i in range(len(invalid_moves)):
            response = test_client.post(
                "/rps",
                data=json.dumps(dict(move=invalid_moves[i])),
                content_type="application/json",
            )
            assert response.status_code == 500
