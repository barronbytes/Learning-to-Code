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
