class Cleaner():
    
    def __init__(self, data: list[str]):
        '''
        Initializes a Cleaner instance.

        Parameters:
            data (list[str]): Data values.
        '''
        self.data = data

    # object string representation        
    def __repr__(self) -> str:
        return f"Cleaner(data={self.data})"
    
    # equals
    def __eq__(self, other: object) -> bool:
        equality = False
        if isinstance(other, Cleaner):
            equality = self.data == other.data
        return equality
    
    def is_list(self) -> bool:
        return isinstance(self.data, list)
    
    def clean_data(data: list) -> list | None:
        data_strings = [d.strip() for d in data if isinstance(d, str)]
        data_numbers = [int(d) for d in data_strings if d.isdigit()]
        return data_numbers if data_numbers else None

    def brain(self) -> list[int] | None:
        is_list = self.is_list()
        clean_data = Cleaner.clean_data(self.data) if is_list else None
        return clean_data
