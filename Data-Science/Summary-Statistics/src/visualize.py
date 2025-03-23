import matplotlib.pyplot as plt
import numpy as np
import os


class Visualize():

    image_dir_name = "images"

    @staticmethod
    def line_plot(file: str, data: list[int]) -> None:
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

        # directory for saving data
        images_dir = os.path.join(os.path.dirname(__file__), "..", Visualize.image_dir_name)
        os.makedirs(images_dir, exist_ok=True)

        # save data, no need for plt.show() in this project
        figure.savefig(os.path.join(images_dir, "line_plot.png"))


    @staticmethod
    def box_plot(file: str, data: list[int]) -> None:
        # plot data
        figure, axes = plt.subplots()
        axes.boxplot(data, vert=False)  # Set vertical=False for horizontal box plot

        # label data
        axes.set(xlabel="Heart Rate (bpm)", ylabel="Study Participant", title=f"Heart Rate Box Plot for {file}")
        axes.grid()

        # directory for saving data
        images_dir = os.path.join(os.path.dirname(__file__), "..", Visualize.image_dir_name)
        os.makedirs(images_dir, exist_ok=True)

        # save data, no need for plt.show() in this project
        figure.savefig(os.path.join(images_dir, "box_plot.png"))
