from get_file_data import GetFileData

def main():
    raw_data = GetFileData.brain()
    print(raw_data)


# run main() only when executed directly by main.py, not when imported by other files
if __name__ == "__main__":
    main()