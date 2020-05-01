#!/usr/bin/python3

#Exercise 2.3 from Owen's "Practical Signal Processing".
#Input is a wave file with 400Hz pure sine tone. Then, by
#keeping only N-th sample, we effectively reduce its sample
#frequency from 48k to 2k to get audible aliases, first
#of which is at 1.6kHz.

import wave

OUT_SECS = 10 #Max length of produced output
ZERO_8B_WAV = 127 #Zero in 8-bit wav format
NEW_FS = 2e3 #Desired new sample frequency

def print_params(f_params):
    print(f_params)
    print(f'Duration: {f_params.nframes/f_params.framerate}')

#Read file
rec = wave.open('aliasing.wav', 'r')
f_params = rec.getparams()
print_params(f_params)
no_frames_to_read = min(f_params.framerate * OUT_SECS, f_params.nframes)
data_in = rec.readframes(no_frames_to_read)
rec.close()

#Edit the data
data_out = []
samples_to_clear = int(f_params.framerate/NEW_FS)
print(f'To get f_s = {NEW_FS} with input f_s = {f_params.framerate}, '
      f'we need to keep only every {samples_to_clear}-th sample.')
for i in range(len(data_in)):
    if i % samples_to_clear > 0:
        data_out.append(ZERO_8B_WAV)
    else:
        data_out.append(data_in[i])
data_out = bytes(data_out)

#Write back data
filename = 'output.wav'
wrt = wave.open(filename, 'w')
wrt.setparams(f_params)
wrt.writeframes(data_out)
wrt.close()
print(f'Done, output: {filename}')
