import os


class GetFileData():
    data_dir_name = "data"

    @staticmethod
    def root_dir() -> str:
        file_path = os.path.relpath(__file__)
        file_dir = os.path.dirname(file_path)
        root_dir = os.path.relpath(os.path.join(file_dir, ".."))
        return root_dir

    @staticmethod
    def get_data_files(root_dir:str) -> list[str]:
        data_dir = os.path.join(root_dir, GetFileData.data_dir_name)
        dir_contents = os.listdir(data_dir)
        return [content for content in dir_contents if os.path.isfile(os.path.join(data_dir, content))]

    @staticmethod   
    def select_data_file(data_files: list[str]) -> int:
        print("These files contain heart rate data:")
        options = "\n".join(f"[{i+1}] file=\"{file}\"" for i, file in enumerate(data_files))
        print(options)
        selection = input("\nEnter the file number you want to analyze.\nWill default to '1' for invalid input: ")
        indices = [str(n) for n in range(0, len(data_files))]
        index = int(selection)-1 if selection in indices else 0
        return index

    @staticmethod
    def read_data(file_path: str) -> list[str]:
        with open(file=file_path, mode="r", encoding="utf-8") as file:
            raw_data = file.readlines()
        return raw_data

    @staticmethod
    def brain() -> list[list[str], str]:
        root_dir = GetFileData.root_dir()
        is_data_dir_exists = os.path.isdir(os.path.join(root_dir, GetFileData.data_dir_name))
        data_files = GetFileData.get_data_files(root_dir) if is_data_dir_exists else []
        raw_data = []
        file_name = data_files[0]
        if data_files:
            file_index = GetFileData.select_data_file(data_files)
            file_name = data_files[file_index]
            file_path = os.path.join(root_dir, GetFileData.data_dir_name, file_name)
            file_lines = GetFileData.read_data(file_path)
            raw_data = file_lines
        return [file_name, raw_data]
