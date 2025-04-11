import os
from openai import OpenAI


class Transform():
    @staticmethod
    def validate(raw_data: list[str]) -> bool:
        '''
        Determines if raw sentiment data contains any erroneous data. Egdge cases considered:
        (1) Empty data -> [] -> print error message
        (2) Any non-string data -> ["hello", "world", 1] -> print error message

        Parameters:
            raw_data list(str): Raw data of sentiment comments.
        Returns:
            bool: If erroneous data exists returns True, otherwise False.
        '''
        is_empty = not bool(raw_data)
        is_strings = all(isinstance(data, str) for data in raw_data) if raw_data else False
        is_valid = True
        if is_empty or not is_strings:
            is_valid = False
            print("\nError: JSON file contained no reviews." if is_empty else "\nError: JSON file contained erroneous reviews.")
        return is_valid


    @staticmethod
    def open_ai_mapper(raw_data: list[str]) -> list[str]:
        '''
        '''
        client = OpenAI(api_key=os.getenv("API_OPENAI"))
        print("\nWe are about to use the OpenAI API to condense our sentiment surveys into a collection of one-word summaries!")


    @staticmethod
    def brain(raw_data: list[str], file_name: str) -> list[str]:
        '''
        Coordinates class methods to complete transformation step of ETL pipeline.

        Returns:
            list (str): Collection of One-word summaries for reviews.
        '''
        is_valid = Transform.validate(raw_data)
        sentiments = []
        if is_valid:
            Transform.open_ai_mapper(raw_data)
