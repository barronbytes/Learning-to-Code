import os


class FileHandler():
    data_dir_name = "data"

    @staticmethod
    def root_dir() -> str:
        file_path = os.path.relpath(__file__)
        file_dir = os.path.dirname(file_path)
        root_dir = os.path.relpath(os.path.join(file_dir, ".."))
        return root_dir

    @staticmethod
    def get_data_files(root_dir:str) -> list[str]:
        data_dir = os.path.join(root_dir, FileHandler.data_dir_name)
        dir_contents = os.listdir(data_dir)
        return [content for content in dir_contents if os.path.isfile(os.path.join(data_dir, content))]

    @staticmethod
    def brain() -> None:
        root_dir = FileHandler.root_dir()
        is_data_dir_exists = os.path.isdir(os.path.join(root_dir, FileHandler.data_dir_name))
        data_files = FileHandler.get_data_files(root_dir) if is_data_dir_exists else []
