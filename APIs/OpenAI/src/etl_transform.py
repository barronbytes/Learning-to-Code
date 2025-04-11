class Transform():
    @staticmethod
    def validate(raw_data: list[str]) -> None:
        '''
        Determines if raw sentiment data contains any erroneous data. Egdge cases considered:
        (1) Empty data -> [] -> print error message
        (2) Any non-string data -> ["hello", "world", 1] -> print error message

        Parameters:
            raw_data list(str): Raw data of sentiment comments.
        '''
        is_empty = not bool(raw_data)
        is_strings = all(isinstance(data, str) for data in raw_data) if raw_data else False
        if is_empty:
            print("\nError: JSON file contained no reviews.")
        elif not is_strings:
            print("\nError: JSON file contained erroneous reviews.")

    
    @staticmethod
    def brain(raw_data: list[str]):
        '''
        Coordinates class methods to complete transformation step of ETL pipeline. Edge cases considered:
        '''
        Transform.validate(raw_data)
