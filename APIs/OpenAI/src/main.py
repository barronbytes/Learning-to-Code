from etl_extract import Extract
from etl_transform import Transform
from control import Control


def main():
    run_all = True
    while run_all:
        is_extracted, file_name, raw_data = Extract.brain()
        sentiments = Transform.brain(raw_data) if is_extracted else []
        run_all = Control.clear_screen() if is_extracted else False


if __name__ == "__main__":
    main()
