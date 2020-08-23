import pyaudio
from numpy import sin, pi, arange, float32


def play_single_frequency(freq=440.0, volume=.5, duration=3.0):
    p = pyaudio.PyAudio()

    volume = volume      # range [0.0, 1.0]
    rate = 44100         # sampling rate, Hz, must be integer
    duration = duration  # in seconds, may be float
    freq = freq          # sine frequency, Hz, may be float

    # generate samples, note conversion to float32 array
    samples = (sin(2*pi*arange(rate*duration)*freq/rate)).astype(float32)

    # for paFloat32 sample values must be in range [-1.0, 1.0]
    stream = p.open(format=pyaudio.paFloat32,
                    channels=1,
                    rate=rate,
                    output=True)

    # play. May repeat with different volume values (if done interactively)
    stream.write(volume*samples)

    stream.stop_stream()
    stream.close()

    p.terminate()
