#!/usr/bin/env python

import argparse
import os
import numpy as np
from numpy.fft import rfft, rfftfreq
from pydub import AudioSegment
from pydub.silence import split_on_silence

parser = argparse.ArgumentParser(description='Split audio file into chunks based on silence')
parser.add_argument('--keep-silence', type=int, default=100, help='Keep this much silence at the beginning and end of each chunk (in ms)')
parser.add_argument('--min-duration', type=float, default=0.5, help='Minimum duration of each chunk (in seconds)')
parser.add_argument('--min-silence-len', type=int, default=100, help='Minimum length of silence to split on (in ms)')
parser.add_argument('--silence-thresh', type=int, default=-64, help='Threshold of silence to split on (in dBFS)')
parser.add_argument('audio_files', nargs=argparse.REMAINDER, help='Audio files to split')
args = parser.parse_args()

keep_silence = args.keep_silence
min_duration = args.min_duration
min_silence_len = args.min_silence_len
silence_thresh = args.silence_thresh
audio_files = args.audio_files

for audio_file in audio_files:
    base_filename = audio_file.split('.')[0]
    if not os.path.isdir(base_filename):
        os.mkdir(base_filename)

    audio = AudioSegment.from_wav(audio_file)
    samples = np.array(audio.get_array_of_samples())

    if audio.sample_width == 2:
        samples = np.frombuffer(samples, dtype=np.int16)
    elif audio.sample_width == 4:
        samples = np.frombuffer(samples, dtype=np.int32)

    chunks = split_on_silence(audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh, keep_silence=keep_silence)
    chunk_no = 1
    for i, chunk in enumerate(chunks):
        if chunk.duration_seconds > min_duration:
            chunk.export(f"{base_filename}/{chunk_no}.wav", format="wav")

            chunk_samples = np.array(chunk.get_array_of_samples())
            N = len(chunk_samples)
            yf = rfft(chunk_samples)
            xf = rfftfreq(N, 1 / audio.frame_rate)

            # Find the peak frequency
            idx = np.argmax(np.abs(yf))
            freq = xf[idx]

            print(f"{chunk_no},{chunk.duration_seconds:.2f},{freq:.2f}")
            chunk_no += 1
