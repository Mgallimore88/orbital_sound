from sin_gen import SinGen
import soundcard as sc

y = SinGen(500)

# get a list of all speakers:
speakers = sc.all_speakers()

'''All of these functions return Speaker and Microphone objects,
which can be used for playback and recording. All data passed in and out
of these objects are frames × channels Numpy arrays.'''
