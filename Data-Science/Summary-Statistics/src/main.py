from get_file_data import GetFileData
from cleaner import Cleaner

def main():
    raw_data = GetFileData.brain()
    clean_data = Cleaner(raw_data).brain()
    print(clean_data)


# run main() only when executed directly by main.py, not when imported by other files
if __name__ == "__main__":
    main()