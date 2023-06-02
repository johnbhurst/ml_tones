#!/usr/bin/env python

import numpy as np
import sys
from pydub import AudioSegment
from pydub.silence import split_on_silence


# Load your audio file
audio_file = sys.argv[1]
base_filename = audio_file.split('.')[0]
audio = AudioSegment.from_wav(audio_file)

# Convert audio to numpy array (needed for scipy)
samples = np.array(audio.get_array_of_samples())

# Check if sample width is 2
if audio.sample_width == 2:
    samples = np.frombuffer(samples, dtype=np.int16)
elif audio.sample_width == 4:
    samples = np.frombuffer(samples, dtype=np.int32)

# Where the clip is silent, the sample value is zero. So we split the audio where sample is zero
chunks = split_on_silence(audio, min_silence_len=100, silence_thresh=-64)

# Save each chunk to separate files
for i, chunk in enumerate(chunks):
    chunk.export(f"{base_filename}_{i}.wav", format="wav")
