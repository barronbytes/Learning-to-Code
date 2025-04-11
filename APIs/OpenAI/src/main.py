from etl_extract import Extract
from etl_transform import Transform
from control import Control


def main():
    run_all = True
    while run_all:
        is_extracted, raw_data = Extract.brain()
        if is_extracted:
            Transform.brain(raw_data)
        run_all = Control.clear_screen() if is_extracted else False


if __name__ == "__main__":
    main()
