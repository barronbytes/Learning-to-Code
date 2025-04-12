import matplotlib.pyplot as plt
import os


class Load():
    DST_DIR_NAME = "../assets"


    @staticmethod
    def create_bar_graph(file_name: str, data_labels: list[str], data_counts: list[int]) -> None:
        '''
        Creates bar graph from sentimental analysis results.

        Parameters:
            file_name (str): File name to create or overwrite.
            data_labels (list(str)): Sentiment labels as quantitative data for bar graph.
            data_counts (list(int)): Sentiment counts as quantitative data for bar graph.
        '''
        # set data:
        x = data_labels
        y = data_counts

        # plot data
        figure, axes = plt.subplots()
        bars = axes.bar(x=x, height=y)

        # label data
        axes.set(xlabel="Sentiment Category", ylabel="Sentiment Count", title=f"Sentimental Analysis: {file_name}")
        axes.set_ylim(0, max(y) + 5) # y-axis padding
        axes.bar_label(bars, padding=3) # bar chart labels

        # save data, no need for plt.show() in this project
        figure.savefig(os.path.join(Load.DST_DIR_NAME, file_name.replace(".json", ".png")))
        plt.close()
