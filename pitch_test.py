import math
import record_audio
from random_functions import *
from conversions import *


def start():
    min_pitch, max_pitch = record_audio.record_audio(10)
    low = convert_to_letter_pitch(min_pitch)
    high = convert_to_letter_pitch(max_pitch)

    print low, high, [(i, j) for i, j in pitches.items()], low[:-1]
    low_val = convert_letter_pitch_to_interval(low)
    high_val = convert_letter_pitch_to_interval(high)

    print low, high, low_val, high_val
    for _ in range(10):
        print convert_interval_to_letter_pitch(
            generate_random_note_in_interval(low_val, high_val))

