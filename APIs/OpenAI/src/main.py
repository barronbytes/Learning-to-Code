from etl_extract import Extract
from etl_transform import Transform
from etl_load import Load
from control import Control


def main():
    run_all = True
    while run_all:
        is_extracted, file_name, raw_data = Extract.brain()
        sentiments = Transform.brain(raw_data) if is_extracted else []
        #if sentiments:
        #    Load.brain(file_name, sentiments)
        run_all = Control.clear_screen() if is_extracted else False


if __name__ == "__main__":
    main()
