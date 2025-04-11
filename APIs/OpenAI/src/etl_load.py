import matplotlib.pyplot as plt
import os


class Load():
    SENTIMENTS = ["negative", "neutral", "positive", "irrelevant"]
    DST_DIR_NAME = "../images"


    @staticmethod
    def calc_tallies(sentiments: list[str]) -> dict[str, int]:
        '''
        Calcualtes how many times each sentiment category appears within list of sentiment one-word summaries.
        
        Parameters:
            sentiments list(str): Collection of one-word summaries for reviews.
        Returns:
            dict (str, str): Collection of sentiment category-count pairs.
        '''
        tallies = {
            category:sentiments.count(category)
            for category in Load.SENTIMENTS
        }
        return tallies
    

    @staticmethod
    def create_bar_graph(file_name: str, tallies: dict[str, int]) -> None:
        '''
        Creates bar graph from sentimental analysis tallies.

        Parameters:
            file_name (str): File name to create.
            tallies (dict(str, int)): Collection of sentiment category-count pairs.
        '''
        # set data:
        sentiment_names = Load.SENTIMENTS
        sentiment_counts = [tallies[cat] for cat in sentiment_names]

        # plot data
        figure, axes = plt.subplots()
        axes.bar(x=sentiment_names, height=sentiment_counts)

        # label data
        axes.set(xlabel="Sentiment Category", ylabel="Sentiment Count", title=f"Sentimental Analysis: {file_name}")

        # save data, no need for plt.show() in this project
        figure.savefig(os.path.join(Load.DST_DIR_NAME, file_name.replace(".json", ".png")))
        plt.close()


    @staticmethod
    def brain(file_name: str, sentiments: list[str]) -> None:
        '''
        Coordinates class methods to complete load step of ETL pipeline. Edge case not considered:
        - Visualization for original JSON file has already been created. Program will overwrite existing bar graph.

        Parameters:
            file_name (str): File name.
            sentiments (list(str)): Collection of one-word summaries for reviews.
        '''
        tallies = Load.calc_tallies(sentiments)
        Load.create_bar_graph(file_name=file_name, tallies=tallies)
