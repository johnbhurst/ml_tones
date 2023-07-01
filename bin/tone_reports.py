#!/usr/bin/env python
# Copyright 2023 John Hurst
# John Hurst (john.b.hurst@gmail.com)
# 2023-06-20

import argparse
import os

parser = argparse.ArgumentParser(description='Create voice reports')
parser.add_argument('--save-dir', type=str, default='data/reports/tone_reports', help='Directory to save reports to')
parser.add_argument('tone_waveform_dirs', nargs=argparse.REMAINDER, help='Folders containing tone waveforms')
args = parser.parse_args()

os.makedirs(args.save_dir, exist_ok=True)
for tone in range(36, 94):
    print(f"Tone {tone}")
    basename = f"tone_{tone}"
    with open(f"{args.save_dir}/{basename}.md", "w") as f:
        print(f"# Tone {tone}", file=f)
        print("", file=f)
        for tone_waveform_dir in args.tone_waveform_dirs:
            path = os.path.basename(tone_waveform_dir)
            print(f"## {tone_waveform_dir}", file=f)
            print("", file=f)
            print(f"<div style='display: flex; justify-content: space-around;'>", file=f)
            print(f"    <img src='../../tone_waveforms/{path}/{tone}_1start.png' width='30%'>", file=f)
            print(f"    <img src='../../tone_waveforms/{path}/{tone}_2mid.png' width='30%'>", file=f)
            print(f"    <img src='../../tone_waveforms/{path}/{tone}_3end.png' width='30%'>", file=f)
            print(f"</div>", file=f)
            print("", file=f)