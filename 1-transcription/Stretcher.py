############################################
#########  TnT-TAP AUDIO STRETCHER  ########
#########      BBSLab Jun 2024      ########
############################################

import subprocess
import os
from audiostretchy.stretch import stretch_audio

# Input path and ratio
wma_path = os.path.normpath(input("Please, enter the audio to stretch path: ")).replace("'","").replace(" ","") # remove '' from string
stretch_ratio = float(input("Please, enter the stretching ratio (>1 == longer audio, <1 == shorter audio): "))

# Define wav and output path
wav_filename = os.path.basename(wma_path).split('.')[0] + '.wav'
wav_path = os.path.join(os.path.dirname(wma_path), wav_filename)

output_path = wav_path.split('.wav')[-2] + '_stretch-{}.wav'.format(str(stretch_ratio))

# Overwrite dialog
write = 'Y'
if os.path.isfile(output_path):
    overwrite_dialog = True
    while overwrite_dialog == True:
        write = input("File is already stretched. Overwrite? [Y/N] ")
        write = write.upper()
        if write == 'Y':
            os.remove(output_path)
            overwrite_dialog = False
        elif write == 'N':
            print("Audio {} was skipped.".format(os.path.basename(wma_path)))
            overwrite_dialog = False
        else:
            print("Please, enter a valid reponse.")

# Convert to wav and stretch
if write == 'Y':
    subprocess.run(r'ffmpeg -i {} {} -loglevel error'.format(wma_path, wav_path))
    stretch_audio(wav_path, output_path, ratio = stretch_ratio)
    os.remove(wav_path)
    print("Audio {} was sucessfully stretched to a {} ratio.".format(os.path.basename(wma_path), str(stretch_ratio)))