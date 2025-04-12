from etl_extract import Extract
from etl_transform import Transform
from etl_load import Load
from control import Control


def main():
    run_all = True
    while run_all:
        is_extracted, file_name, reviews = Extract.brain()
        data_labels, sentiments = Transform.brain(reviews) if is_extracted else []
        data_counts = [sentiments[label] for label in data_labels]
        print("dict:", sentiments)
        print("y", data_counts)
        print("x", data_labels)
        #if sentiments:
        #    Load.brain(file_name, sentiments)
        run_all = Control.clear_screen() if is_extracted else False


if __name__ == "__main__":
    main()
