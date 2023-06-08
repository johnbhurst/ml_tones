#!/usr/bin/env python

import argparse
import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# Set up command-line argument parsing
parser = argparse.ArgumentParser(description="Plot a portion of a WAV file")
parser.add_argument("filename", help="The WAV file to read")
parser.add_argument("--startMs", type=int, default=0, help="The start time in milliseconds")
parser.add_argument("--endMs", type=int, default=None, help="The end time in milliseconds")
args = parser.parse_args()

# Read the WAV file
sample_rate, data = wavfile.read(args.filename)

# Convert start and end times from milliseconds to samples
start_sample = int(args.startMs / 1000.0 * sample_rate)
end_sample = None if args.endMs is None else int(args.endMs / 1000.0 * sample_rate)

# Extract the portion of the waveform to plot
data_to_plot = data[start_sample:end_sample]

# Generate the time values for the portion of the waveform to plot
times = np.arange(start_sample, start_sample + len(data_to_plot)) / float(sample_rate)

# Create the plot
plt.figure(figsize=(10, 4))
plt.plot(times, data_to_plot)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title(f"Waveform of {args.filename} from {args.startMs}ms to {args.endMs}ms")
plt.grid(True)
plt.show()
