import os


class Control():

    @staticmethod
    def clear_screen():
        """
        Clear terminal screen.
        """
        os.system('cls' if os.name == 'nt' else 'clear')
