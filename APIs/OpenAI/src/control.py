import os


class Control():
    @staticmethod
    def clear_screen() -> bool:
        """
        Decides whether to continue or exit program.
        Returns:
            bool: Updated value for `run_all` variable from main.py
        """
        ask_user = input("Run program again?: (Yes/No) ")
        os.system('cls' if os.name == 'nt' else 'clear')
        return ask_user.lower() == "yes"
