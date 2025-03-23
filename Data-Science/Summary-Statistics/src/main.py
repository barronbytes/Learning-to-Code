from get_file_data import GetFileData
from cleaner import Cleaner
from metrics import Metrics
from visualize import Visualize


def display_results(stats: list[float]) -> None:
    max_num, avg, stdev = stats
    print(f"\nMaximum HR: {max_num} \nAverage HR: {avg} \nStandard Deviation HR: {stdev}")

def main():
    file_name, raw_data = GetFileData.brain()
    clean_data = Cleaner(raw_data).brain()
    stats = Metrics().brain(clean_data) if isinstance(clean_data, list) and len(clean_data) >= 1 else [0, 0, 0]
    display_results(stats)
    Visualize.line_plot(file=file_name, data=clean_data, time_increment=5)


# run main() only when executed directly by main.py, not when imported by other files
if __name__ == "__main__":
    main()