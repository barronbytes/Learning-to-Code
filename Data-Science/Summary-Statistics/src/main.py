from get_file_data import GetFileData
from cleaner import Cleaner
from metrics import Metrics

@staticmethod
def display_results(stats: list[float]) -> str:
    max_num, avg, stdev = stats
    print(f"\nMaximum HR: {max_num} \nAverage HR: {avg} \nStandard Deviation HR: {stdev}")

def main():
    raw_data = GetFileData.brain()
    clean_data = Cleaner(raw_data).brain()
    stats = Metrics().brain(clean_data) if isinstance(clean_data, list) and len(clean_data) >= 1 else [0, 0, 0]
    display_results(stats)

# run main() only when executed directly by main.py, not when imported by other files
if __name__ == "__main__":
    main()