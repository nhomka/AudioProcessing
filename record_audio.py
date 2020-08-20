from conversions import *
import pyaudio
import wave
import array
import datetime
import numpy as np
import aubio
import math
from matplotlib import pyplot as plt

CHUNK = 512
FORMAT = pyaudio.paFloat32
CHANNELS = 2
RATE = 44100
FILE_NAME = "Recording.wav"

pitches = {0: "C",
           1: "C#",
           2: "D",
           3: "D#",
           4: "E",
           5: "F",
           6: "F#",
           7: "G",
           8: "G#",
           9: "A",
           10: "A#",
           11: "B"}


def is_silent(audio_data):
    return max(audio_data) < 500


def filter_bad(last_good_freq, last_good_time, pitch):
    if last_good_time > datetime.datetime.now() - datetime.timedelta(seconds=.25):
        # print last_good_freq, last_good_time
        if last_good_freq != 0 and (last_good_freq-pitch) > pitch/2:
            # print "ya", last_good_freq, pitch
            pitch = last_good_freq
        if pitch < 200 or pitch > 1500:
            pitch = last_good_freq
    else:
        if pitch < 200 or pitch > 1500:
            pitch = 0
    return pitch


def record_audio(record_time = 10):
    record_seconds = record_time
    min_pitch = 5000
    max_pitch = 0
    timestamp = datetime.datetime.now()
    # Instantiate PyAudio
    p = pyaudio.PyAudio()
    p_detection = aubio.pitch("default", 2048, 1024, 44100)
    # Set unit.
    p_detection.set_unit("Hz")
    p_detection.set_silence(-40)

    # Open Stream
    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    frames_per_buffer=CHUNK)

    # Record Data
    frames = []
    numpy_data = []
    last_good = 0
    last_good_time = datetime.datetime.now()

    for i in range(0, int(RATE / CHUNK * record_seconds)):
        data = stream.read(CHUNK)
        data_chunk = array.array('h', data)
        samples = np.frombuffer(data, dtype=aubio.float_type)
        pitch = p_detection(samples)[0]
        real_pitch = pitch
        pitch = filter_bad(last_good, last_good_time, pitch)
        if min_pitch > pitch > 200:
            min_pitch = pitch
        if pitch > max_pitch:
            max_pitch = pitch
        if is_silent(data_chunk):
            if datetime.datetime.now() < timestamp + datetime.timedelta(0, 5):
                frames.append(data)
                # print("No Noise but still writing")
            else:
                1
                # print("No Noise")
        else:
            # print("Noise encountered")
            frames.append(data)
            timestamp = datetime.datetime.now()
            # snippet = snippet.reshape(-1, pitch.hop_size)
            # snippet = snippet.astype(aubio.float_type)
            # pitch_candidate = pitch(snippet)
            if real_pitch > 200:
                last_good = pitch
                last_good_time = datetime.datetime.now()
                # print convert_to_letter_pitch(pitch, 440)
        numpy_data.append(pitch)
        # print("\n")

    # Write To File
    wav_file = wave.open(FILE_NAME, 'wb')
    wav_file.setnchannels(CHANNELS)
    wav_file.setsampwidth(p.get_sample_size(FORMAT))
    wav_file.setframerate(RATE)
    wav_file.writeframes(b''.join(frames))  # Append Frames to File
    wav_file.close()

    # Stop Stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # plot data
    # plt.plot(numpy_data)
    # plt.show()

    return min_pitch, max_pitch

