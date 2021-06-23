"""
Demonstrate matplotlib animation of random values.

Draw samples from a normal distribution and dynamically
graph frequencies of the samples.


"""

from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sys
import random

def show_bar_chart(title, x_label, y_label, x_values, y_values, bar_toppers):
    """
    Display a bar chart.
    @param title the chart title.
    @param x_label the label for the x axis
    @param y_label the label for the y axis
    @param x_values the x values to plot
    @param y_values the y values to plot
    @param bar_toppers the text above each bar
    """

    plt.cla()  # clear old contents


    axes = sns.barplot(x_values, y_values, color='blue')
    axes.set_title(title)
    axes.set(xlabel=x_label, ylabel=y_label)


    # Scale the y-axis by 10% to make room for text above the bars.
    axes.set_ylim(top=1.10*max(y_values))

    # Display the topper text above each patch (bar).
    for bar, topper in zip(axes.patches, bar_toppers):
        text_x = bar.get_x() + bar.get_width()/2
        text_y = bar.get_height()
        axes.text(text_x, text_y, topper,
                  fontsize=8, fontstyle='italic', fontweight='semibold',ha='center', va='bottom')

def update_frame(frame_number, event_count, values, frequencies):
    """
    Update the bar plot contents for each animation frame.
    @param frame_number the frame number.
    @param event_count the count of experiments per frame.
    @param values the random values.
    @param frequencies the list of value frequencies.
    """

    # Draw samples 'event_count' times and update the frequencies of the values.
    for _ in range(event_count):
        while True:
            index = int(np.random.normal(12.5, 4.1))
            if 0 <= index < len(frequencies):
                frequencies[index] += 1
                break


    # Set the percentages for the bar tops.
    freq_sum = sum(frequencies)
    topper = [f'{freq:,}\n{freq/freq_sum:.1%}' for freq in frequencies]

    # Display the bar chart for this frame.
    show_bar_chart(f'Frequencies of {freq_sum:,} Normally Distributed Random Values ' +
                   f'(Frame {frame_number + 2})\n  µ = 12.5 and ß = 4.1',
                   'Value', 'Frequency',
                   values, frequencies, topper)

# Read command-line arguments for the number of frames
# and the number of experiments per frame.
number_of_frames = int(sys.argv[1])
events_per_frame  = int(sys.argv[2])

# Create the figure for the animation.
sns.set_style('whitegrid')  # white background with gray grid lines
figure = plt.figure('Normal Distribution')

values = list(range(1, 21))
frequencies = [0]*20        #list of frequencies of values

# Configure and start the animation that calls function update_frame.
binomial_animation = animation.FuncAnimation(
    figure, update_frame,repeat=False,
    frames=number_of_frames-1, interval=10,
    fargs=(events_per_frame, values, frequencies))

plt.show()
