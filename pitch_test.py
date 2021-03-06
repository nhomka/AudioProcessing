import math
from record_audio import *
import time
from random_functions import *
from conversions import *


def start():
    recorder = AudioRecorder()
    print "Recording calibration starts now!"
    recorder.get_min_max()
    low = convert_to_letter_pitch(recorder.min_Hz)
    high = convert_to_letter_pitch(recorder.max_Hz)

    print low, high, [(i, j) for i, j in pitches.items()], low[:-1]
    low_val = convert_letter_pitch_to_interval(low)
    high_val = convert_letter_pitch_to_interval(high)

    print low, high, low_val, high_val
    for _ in range(10):
        note = generate_random_note_in_interval(low_val, high_val)
        note_n = convert_interval_to_letter_pitch(note)
        print "This is your target note: {0}".format(note_n)
        time.sleep(5)
        print "recording pitch in... 3"
        time.sleep(1)
        print 2
        time.sleep(1)
        print 1
        time.sleep(1)
        print "GO"
        l, h = recorder.record_audio(1.5)
        l_n = convert_to_letter_pitch(l)
        h_n = convert_to_letter_pitch(h)
        print l_n, h_n, note_n
        print "YAY" if l_n == note_n or h_n == note_n else "NOOOO"
