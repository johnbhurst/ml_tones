#!/usr/bin/env python

import argparse
import matplotlib.pyplot as plt
import numpy as np
import os
from numpy.fft import rfft, rfftfreq
from pydub import AudioSegment

parser = argparse.ArgumentParser(description='Generate stats for audio files')
parser.add_argument('--save-dir', type=str, default='data/voice_stats', help='Directory to save stats and graphs to')
parser.add_argument('raw_tones_folders', nargs=argparse.REMAINDER, help='Folders of tone WAVs to analyze')
args = parser.parse_args()

os.makedirs(args.save_dir, exist_ok=True)
for raw_tones_folder in args.raw_tones_folders:
    midi_nos = []
    freqs = []
    print(raw_tones_folder)
    csv_filename = args.save_dir + "/" + os.path.basename(os.path.normpath(raw_tones_folder)) + ".csv"
    with open(csv_filename, "w") as f:
        print("filename,duration,frequency", file=f)
        for filename in sorted(os.listdir(raw_tones_folder)):
            if filename.endswith(".wav"):
                midi_no = int(filename.split('.')[0])
                audio = AudioSegment.from_wav(raw_tones_folder + "/" + filename)
                samples = np.array(audio.get_array_of_samples())
                N = len(samples)
                yf = rfft(samples)
                xf = rfftfreq(N, 1 / audio.frame_rate)
                idx = np.argmax(np.abs(yf))
                freq = xf[idx]
                print(f"{midi_no},{audio.duration_seconds:.2f},{freq:.2f}", file=f)
                midi_nos.append(midi_no)
                freqs.append(freq)

    img_filename = args.save_dir + "/" + os.path.basename(os.path.normpath(raw_tones_folder)) + ".svg"
    plt.plot(midi_nos, freqs, 'o')
    plt.xlabel('MIDI number')
    plt.ylabel('Frequency (Hz)')
    plt.savefig(img_filename)
    plt.close()


