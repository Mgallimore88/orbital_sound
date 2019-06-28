import numpy as np
import soundcard as sc


class SinGen:
    def __init__(self, frequency=500):
        self.wave_frequency = frequency                     # Hz
        self.sample_frequency = 44100                       # Hz
        self.sampling_interval = 1 / self.sample_frequency  # secs
        self.length_secs = 0.5
        self. num_of_samples = round(self.sample_frequency * self.length_secs)

    def make_sin(self):
        self.time_array = np.linspace(0, self.length_secs, self.num_of_samples)
        self.waveform = np.sin(2 * np.pi * self.wave_frequency
                               * self.time_array)
        # # Debug
        # print(f'Waveform {self.waveform}')
        # print(f'array size error = {self.num_of_samples - self.time_array.size} samples')
        # print(f'sampling interval = {self.sampling_interval} secs')
        # print(f'2nd val in numpy array = {self.time_array[1]} secs')
        # print(f'sampling interval error = {self.sampling_interval - self.time_array[1]} secs')

    def soundcard_play(self):
        speaker = sc.default_speaker()
        speaker.play(self.waveform/np.max(self.waveform),
                     samplerate=self.sample_frequency)


'''All data passed in and out
of soundcard objects are frames × channels Numpy arrays.'''
