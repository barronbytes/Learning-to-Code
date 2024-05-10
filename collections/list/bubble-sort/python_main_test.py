from python_main import *

submit_cases = [
    ([], []),
    ([38, 68, 88], [88, 68, 38]),
    ([32, 75, 11, 94], [94, 75, 32, 11]),
    ([45, 92, 24, 60, 87, 90], [92, 90, 87, 60, 45, 24]),
]

def test(input, expected_output):
    print("---------------------------------")
    print("Goal: sort an unsorted array in descending order")
    print(f"Input: {input}")
    print(f"Expected output: {expected_output}")
    result = top_scores(input)
    print(f"Actual output: {result}")
    outcome = result == expected_output
    print(f"Outcome: {'Pass' if outcome else 'Fail'}")
    return outcome
    
def main():
    outcomes = [test(*submit_case) for submit_case in submit_cases]
    passed = outcomes.count(True)
    failed = outcomes.count(False)
    result = "PASS" if failed == 0 else "FAIL"
    print(f"============== {result} ==============")
    print(f"{passed} passed, {failed} failed")

main()
