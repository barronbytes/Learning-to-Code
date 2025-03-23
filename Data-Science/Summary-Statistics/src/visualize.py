import matplotlib.pyplot as plt
import numpy as np
import os


class Visualize():

    image_dir_name = "images"
    
    @staticmethod
    def line_plot(data: list[int], time_increment: int) -> None:
        time = time_increment*len(data)

        # set data values
        x = np.arange(0.0, time, time_increment)
        y = data

        # plot data
        figure, axes = plt.subplots()
        axes.plot(x, y)

        # label data
        axes.set(xlabel='Time (minutes)', ylabel='Heart Rate (bpm)', title='Heart Rate Data')
        axes.grid()

        # ensure directory exists to save figure
        images_dir = os.path.join(os.path.dirname(__file__), "..", Visualize.image_dir_name)
        os.makedirs(images_dir, exist_ok=True)

        # save and display plot
        figure.savefig(os.path.join(images_dir, "lineplot.png"))
        plt.show()
