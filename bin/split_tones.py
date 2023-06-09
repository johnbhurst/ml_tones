#!/usr/bin/env python

import argparse
import json
import os
from pydub import AudioSegment
from pydub.silence import split_on_silence

with open(os.path.join(os.path.dirname(__file__), 'config.json')) as f:
    config = json.load(f)

parser = argparse.ArgumentParser(description='Split audio file into chunks based on silence')
parser.add_argument('--keep-silence', type=int, default=100, help='Keep this much silence at the beginning and end of each chunk (in ms)')
parser.add_argument('--min-duration', type=float, default=0.5, help='Minimum duration of each chunk (in seconds)')
parser.add_argument('--min-silence-len', type=int, default=100, help='Minimum length of silence to split on (in ms)')
parser.add_argument('--silence-thresh', type=int, default=-64, help='Threshold of silence to split on (in dBFS)')
parser.add_argument('--save-dir', type=str, default='data/raw_tones', help='Directory to save chunks to')
parser.add_argument('audio_files', nargs=argparse.REMAINDER, help='Audio files to split')
args = parser.parse_args()

for audio_file in args.audio_files:
    conf = [rec for rec in config if rec['filename'] == audio_file] or [{}]
    keep_silence = conf[0].get('keep_silence', args.keep_silence)
    min_duration = conf[0].get('min_duration', args.min_duration)
    min_silence_len = conf[0].get('min_silence_len', args.min_silence_len)
    silence_thresh = conf[0].get('silence_thresh', args.silence_thresh)

    save_path = args.save_dir + "/" + os.path.basename(audio_file.split('.')[0])
    if not os.path.isdir(save_path):
        os.makedirs(save_path)

    audio = AudioSegment.from_wav(audio_file)
    chunks = split_on_silence(audio, min_silence_len=min_silence_len, silence_thresh=silence_thresh, keep_silence=keep_silence)
    midi_no = 36
    for i, chunk in enumerate(chunks):
        if chunk.duration_seconds > min_duration:
            chunk.export(f"{save_path}/{midi_no}.wav", format="wav")
            midi_no += 1
