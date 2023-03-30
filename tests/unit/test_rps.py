from rock_paper_scissors.rps import rock_paper_scissors

import random

# def test_rps_random():
#     """
#     Basic test for Rock Paper Scissors
#     """
#     for i in range(100): # Run enough times to make sure we cover all cases
#         assert rock_paper_scissors(random.randint(0, 2)) is not None


def test_rps_all_cases():
    """
    Exhausted test for Rock Paper Scissors
    """
    for i in range(3):  # Test all possible cases
        all_results = set()
        all_pc_choices = set()
        while len(all_results) < 3 or len(all_pc_choices) < 3:
            result, pc_choice = rock_paper_scissors(i)
            assert result in [-1, 0, 1]
            assert pc_choice in [0, 1, 2]
            all_results.add(result)
            all_pc_choices.add(pc_choice)
