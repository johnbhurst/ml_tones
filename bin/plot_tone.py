#!/usr/bin/env python

import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import os

# Set up command-line argument parsing
parser = argparse.ArgumentParser(description="Plot a portion of a WAV file")
parser.add_argument("filenames", nargs="+", help="The WAV files to read")
parser.add_argument("--startMs", type=int, default=0, help="The start time in milliseconds")
parser.add_argument("--endMs", type=int, default=None, help="The end time in milliseconds")
parser.add_argument("--width", type=float, default=10, help="Width of the plot")
parser.add_argument("--height", type=float, default=4, help="Height of the plot")
parser.add_argument("--nodisplay", action='store_true', help="Do not display the plot")
parser.add_argument("--savefile", nargs='?', const=True, default=False, help="Save the plot to a file")
args = parser.parse_args()

# Process each file
for filename in args.filenames:
    # Read the WAV file
    sample_rate, data = wavfile.read(filename)

    # Convert start and end times from milliseconds to samples
    start_sample = int(args.startMs / 1000.0 * sample_rate)
    end_sample = None if args.endMs is None else int(args.endMs / 1000.0 * sample_rate)

    # Extract the portion of the waveform to plot
    data_to_plot = data[start_sample:end_sample]

    # Generate the time values for the portion of the waveform to plot
    times = np.arange(start_sample, start_sample + len(data_to_plot)) / float(sample_rate)

    # Create the plot
    plt.figure(figsize=(args.width, args.height))
    plt.plot(times, data_to_plot)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title(f"Waveform of {filename} from {args.startMs}ms to {args.endMs}ms")
    plt.grid(True)

    # Save the plot to a file if requested
    if args.savefile is not False:
        save_filename = args.savefile
        if args.savefile is True:
            base, ext = os.path.splitext(filename)
            save_filename = f"{base}_{args.startMs}ms_{args.endMs}ms.png"
        plt.savefig(save_filename)

    # Display the plot, unless suppressed
    if not args.nodisplay:
        plt.show()

    # Close the plot to free up memory
    plt.close()
