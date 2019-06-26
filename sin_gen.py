import sounddevice as sd
import numpy as np
import math
import soundcard as sc


class SinGen:
    def __init__(self, frequency=500):
        self.frequency = frequency  # cycles per second
        self.sample_frequency = 10  # Hz
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
        numpy_sin_array = np.array(self.sample_array)
        print(numpy_sin_array)
        
        def sounddevice_play(self):
            sd.play(self.sample_array, self.sample_frequency)
            sd.wait()

        def soundcard_play(self):