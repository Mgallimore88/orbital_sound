import sounddevice as sd
import numpy as np
import math


class SinGen:
    def __init__(self, frequency=500):
        self.frequency = frequency  # cycles per second
        self.sample_frequency = 44100  # Hz
        self.sampling_interval = 1 / self.sample_frequency  # secs
        self.length_secs = 1
        self. num_of_samples = round(self.sample_frequency * self.length_secs)

    def make_sin(self):
        self.time = 0
        self.sample_array = [0] * self.num_of_samples

        for n in range(self.num_of_samples):
            self.sample_array[n] = math.sin(2 * math.pi * self.frequency *
                                            self.time)
            self.time += self.sampling_interval
        
        sd.play(self.sample_array, self.sample_frequency)
        sd.wait()
