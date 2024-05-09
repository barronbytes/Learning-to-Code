from main import *

submit_cases = [
    ([], []),
    ([3, 0, 4], [4, 0, 3]),
    (["hello", "world"], ["world", "hello"]),
]

def test(input, expected_output):
    print("---------------------------------")
    print("Goal: reverse an array")
    print(f"Input: {input}")
    print(f"Expected output: {expected_output}")
    result = reverse_array(input)
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