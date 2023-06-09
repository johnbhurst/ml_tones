#!/usr/bin/env python

import argparse
import numpy as np
from numpy.fft import rfft, rfftfreq
from pydub import AudioSegment

parser = argparse.ArgumentParser(description='Generate stats for audio files')
parser.add_argument('audio_files', nargs=argparse.REMAINDER, help='Audio files to analyze')
args = parser.parse_args()

for audio_file in args.audio_files:
    audio = AudioSegment.from_wav(audio_file)
    samples = np.array(audio.get_array_of_samples())
    N = len(samples)
    yf = rfft(samples)
    xf = rfftfreq(N, 1 / audio.frame_rate)

    # Find the peak frequency
    idx = np.argmax(np.abs(yf))
    freq = xf[idx]

    print(f"{audio_file},{audio.duration_seconds:.2f},{freq:.2f}")

