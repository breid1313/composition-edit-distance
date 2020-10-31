import numpy as np
import simpleaudio as sa
from scipy.io.wavfile import read
from os import path
import wave
import time

# levenshtein function
from levenshtein import levenshteinDP

fs = 44100

# Read file to get buffer                                                                                               
figaro1_wav = wave.open('./data/_01. Act 1 - Overture.wav')
figaro2_wav = wave.open('./data/The Marriage of Figaro.wav')

# get the size of the sample for figaro1
f1_samples = figaro1_wav.getnframes()
# read all frames in the sample
f1_audio = figaro1_wav.readframes(f1_samples)
# get the number of channels
f1_channels = figaro1_wav.getnchannels()
# get the number of bytes per channel
f1_width = figaro1_wav.getsampwidth()


# do the same for figaro2
f2_samples = figaro2_wav.getnframes()
# read all frames in the sample
f2_audio = figaro2_wav.readframes(f2_samples)
# get the number of channels
f2_channels = figaro2_wav.getnchannels()
# get the number of bytes per channel
f2_width = figaro2_wav.getsampwidth()

#44100 is the standard sample rate
fs = 44100

# play the first sample
#sa.play_buffer(f1_audio, f1_channels, f1_width, fs)
# listen for 10 seconds
#time.sleep(10)
# stop once we've heard enough
sa.stop_all()

# play the second sample
#sa.play_buffer(f2_audio, f2_channels, f2_width, fs)
# listen for 10 seconds
#time.sleep(10)
# stop once we've heard enough
sa.stop_all()

# Convert buffer to float32 using NumPy for f1                                                                               
f1_np_int16 = np.frombuffer(f1_audio, dtype=np.int16)
f1_np_float32 = f1_np_int16.astype(np.float32)

# Convert buffer to float32 using NumPy for f2                                                                               
f2_np_int16 = np.frombuffer(f1_audio, dtype=np.int16)
f2_np_float32 = f2_np_int16.astype(np.float32)

# Normalize float32 arrays so that values are between -1.0 and +1.0                                                      
max_int16 = 2**15
f1_normalised = f1_np_float32 / max_int16
f2_normalised = f2_np_float32 / max_int16
# NOTE: at this point we can no longer play the music in its current form
# since we have manipualted the array data, the audio values no longer directly correspond to sound
# instead they are representative of the audio from which they were derived
# this way they are easier to compare across all cases

# uncomment if you want to work with way smaller normalize samples
# takes a ten second sample starting at a variable time
start_second = 15 # change this as you wish
start_byte = start_second * fs
sample_len_second = 1/2 # change this as you wish
sample_len_byte = sample_len_second * fs
end_byte = start_byte + int(sample_len_byte)

f1_normalised_short = f1_normalised[start_byte:end_byte]
f2_normalised_short = f2_normalised[start_byte:end_byte]

distance = levenshteinDP(f1_normalised_short, f2_normalised_short)
print(distance)