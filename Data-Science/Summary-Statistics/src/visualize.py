import matplotlib.pyplot as plt
import numpy as np
import os


class Visualize():

    image_dir_name = "images"

    @staticmethod
    def line_plot(file: str, data: list[int], images_dir: str) -> None:
        # set data
        time_increment = 5
        time = time_increment*len(data)
        x = np.arange(0.0, time, time_increment)
        y = data

        # plot data
        figure, axes = plt.subplots()
        axes.plot(x, y)

        # label data
        axes.set(xlabel="Time (minutes)", ylabel="Heart Rate (bpm)", title=f"Heart Rate Data for {file}")
        axes.grid()

        # save data, no need for plt.show() in this project
        file_name = file.replace(".txt", "")
        figure.savefig(os.path.join(images_dir, f"{file_name}_line_plot.png"))


    @staticmethod
    def box_plot(file: str, data: list[int], images_dir: str) -> None:
        # plot data
        figure, axes = plt.subplots()
        axes.boxplot(data, vert=False)  # Set vertical=False for horizontal box plot

        # label data
        axes.set(xlabel="Heart Rate (bpm)", ylabel="Study Participant", title=f"Heart Rate Box Plot for {file}")
        axes.grid()

        # save data, no need for plt.show() in this project
        file_name = file.replace(".txt", "")
        figure.savefig(os.path.join(images_dir, f"{file_name}_box_plot.png"))


    @staticmethod
    def histogram(file: str, data: list[int], images_dir: str) -> None:
        # set data
        bins = 10

        # plot data
        figure, axes = plt.subplots()
        axes.hist(data, bins=bins, edgecolor="black")

        # label data
        axes.set(xlabel="Heart Rate (bpm)", ylabel="Frequency", title=f"Heart Rate Histogram for {file}")
        axes.grid()

        # save data, no need for plt.show() in this project
        file_name = file.replace(".txt", "")
        figure.savefig(os.path.join(images_dir, f"{file_name}_histogram.png"))


    @staticmethod
    def brain(file: str, data: list[int]) -> None:
        # directory for saving data
        images_dir = os.path.join(os.path.dirname(__file__), "..", Visualize.image_dir_name)
        os.makedirs(images_dir, exist_ok=True)

        Visualize.box_plot(file, data, images_dir)
        Visualize.line_plot(file, data, images_dir)
        Visualize.histogram(file, data, images_dir)
