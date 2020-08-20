from conversions import *
from audio_cleanup import *
import pyaudio
import wave
import array
from datetime import datetime, timedelta
import numpy as np
import aubio
from matplotlib import pyplot as plt


class AudioRecorder:
    def __init__(self, chunk=512, py_format=pyaudio.paFloat32,
                 channels=2, rate=44100, file_name="Recording.wav"):
        self.chunk = chunk
        self.format = py_format
        self.channels = channels
        self.rate = rate
        self.file_name = file_name
        self.min_Hz = 200
        self.max_Hz = 1500

    def get_min_max(self):
        self.min_Hz = input("Enter minimum pitch in Hz: ")
        self.max_Hz = input("Enter maximum pitch in Hz: ")

    def write_audio_to_file(self, frames, sampwidth):
        # Write To File
        wav_file = wave.open(self.file_name, 'wb')
        wav_file.setnchannels(self.channels)
        wav_file.setsampwidth(sampwidth)
        wav_file.setframerate(self.rate)
        wav_file.writeframes(b''.join(frames))  # Append Frames to File
        wav_file.close()

    @staticmethod
    def plot_pitch_data(pitch_data):
        plt.plot(pitch_data)
        plt.show()

    def record_audio(self, record_time=10, record=True):
        record_seconds = record_time
        timestamp = datetime.now()

        # Instantiate PyAudio
        p = pyaudio.PyAudio()

        # Initialize pitch detection.
        p_detection = aubio.pitch("default", 2048, 1024, 44100)
        p_detection.set_unit("Hz")
        p_detection.set_silence(-40)

        # Open Stream
        stream = p.open(format=self.format,
                        channels=self.channels,
                        rate=self.rate,
                        input=record,
                        frames_per_buffer=self.chunk)

        # Record Data
        frames = []
        numpy_data = []
        last_good = 0
        last_good_time = datetime.now()
        min_pitch, max_pitch = 5000, 5

        for i in range(0, int(self.rate / self.chunk * record_seconds)):
            data = stream.read(self.chunk)
            data_chunk = array.array('h', data)
            samples = np.frombuffer(data, dtype=aubio.float_type)
            real_pitch = p_detection(samples)[0]
            pitch = filter_bad(last_good, last_good_time, real_pitch)
            if min_pitch > pitch > 100:
                min_pitch = pitch
            if pitch > max_pitch:
                max_pitch = pitch
            if is_silent(data_chunk) and datetime.now() < timestamp + timedelta(0, 5):
                frames.append(data)
            else:  # Noise encountered
                frames.append(data)
                timestamp = datetime.now()
                if real_pitch > 200:  # Good threshold of input pitch
                    last_good, last_good_time = pitch, timestamp
            numpy_data.append(pitch)

        # Write Audio to file
        # self.write_audio_to_file(frames, p.get_sample_size(self.format))

        # Stop Stream
        stream.stop_stream()
        stream.close()
        p.terminate()

        # Plot Data
        # self.plot_pitch_data(numpy_data)

        return min_pitch, max_pitch
