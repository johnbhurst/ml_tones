#!/usr/bin/env python

import os
import argparse
import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile

def plot_waveform(audio_data, sr, file_name):
    time = np.arange(0, len(audio_data)) / sr
    plt.figure(figsize=(10, 4))
    plt.plot(time, audio_data)
    plt.savefig(file_name)
    plt.close()

def process_folder(folder, save_dir):
    files = os.listdir(folder)
    wav_files = [f for f in files if f.endswith('.wav')]

    for wav_file in wav_files:
        file_name = os.path.splitext(wav_file)[0]  # Remove the .wav extension
        sr, audio_data = wavfile.read(os.path.join(folder, wav_file))

        start_data = audio_data[:sr//10]  # First 100 ms
        mid_data = audio_data[len(audio_data)//2 - sr//20 : len(audio_data)//2 + sr//20]  # Middle 100 ms
        end_data = audio_data[-sr//10:]  # Last 100 ms

        if not os.path.exists(save_dir):
            os.makedirs(save_dir)

        plot_waveform(start_data, sr, os.path.join(save_dir, file_name + '_1start.png'))
        plot_waveform(mid_data, sr, os.path.join(save_dir, file_name + '_2mid.png'))
        plot_waveform(end_data, sr, os.path.join(save_dir, file_name + '_3end.png'))

def main():
    parser = argparse.ArgumentParser(description='Plot waveforms of audio files in a directory.')
    parser.add_argument('folders', type=str, nargs='+', help='List of folders containing the audio files')
    parser.add_argument('--save-dir', default='data/tone_waveforms', type=str, help='Directory to save the waveforms')
    args = parser.parse_args()

    for folder in args.folders:
        print(folder)
        output_folder = os.path.join(args.save_dir, os.path.basename(folder))
        process_folder(folder, output_folder)

if __name__ == "__main__":
    main()
