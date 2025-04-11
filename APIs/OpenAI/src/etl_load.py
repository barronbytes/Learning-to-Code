class Load():
    SENTIMENTS = ["negative", "neutral", "positive", "irrelevant"]


    @staticmethod
    def calc_tallies(sentiments: list[str]) -> dict[str, int]:
        tallies = {
            category:sentiments.count(category)
            for category in Load.SENTIMENTS
        }
        return tallies


    @staticmethod
    def brain(file_name: str, sentiments: list[str]) -> None:
        tallies = Load.calc_tallies(sentiments)


print(Load.calc_tallies(["negative", "negative", "positive", "irrelevant"]))