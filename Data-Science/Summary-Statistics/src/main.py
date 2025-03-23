from get_file_data import GetFileData
from cleaner import Cleaner
from metrics import Metrics
from visualize import Visualize


def print_results(stats: list[float]) -> None:
    '''
    Unpacks list of input summary statistics to print.

    Parameters:
        data (list[str]): List of summary statistics.
    '''
    max_num, avg, stdev = stats
    print(f"\nMaximum HR: {max_num} \nAverage HR: {avg:.2f} \nStandard Deviation HR: {stdev:.2f}")


def main():
    '''
    Main function that coordinates actions of entire project files as follows:
    (1) Allow user to choose data for analysis via GetFileData class
    (2) Clean data via Cleaner class
    (3) Calculcate summary statistics via Metrics class, and print results via local function print_results()
    (4) Generate visualizations of data via Visualize class
    '''
    file_name, raw_data = GetFileData.brain()
    clean_data = Cleaner(raw_data).brain()
    stats = Metrics().brain(clean_data) if isinstance(clean_data, list) and len(clean_data) >= 1 else [0, 0, 0]
    print_results(stats)
    Visualize.brain(file=file_name, data=clean_data)


# run main() only when executed directly by main.py, not when imported by other files
if __name__ == "__main__":
    main()