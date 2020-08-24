from play_frequency import play_single_frequency
import time
from random_functions import *
from conversions import *


def start():
    min_hz = input("Enter minimum pitch in Hz: ")
    max_hz = input("Enter maximum pitch in Hz: ")
    low = convert_to_letter_pitch(min_hz)
    high = convert_to_letter_pitch(max_hz)

    print low, high, [(i, j) for i, j in pitches.items()], low[:-1]
    low_val = convert_letter_pitch_to_interval(low)
    high_val = convert_letter_pitch_to_interval(high)

    print low, high, low_val, high_val
    score = 0
    rounds = 10
    for _ in range(rounds):
        note_hz = generate_random_note_in_interval(min_hz, max_hz)
        print "Note has been generated."
        time.sleep(1)
        print "playing pitch in... 3"
        time.sleep(1)
        print 2
        time.sleep(1)
        print 1
        time.sleep(1)
        print "GO.  Enter 'replay' to play again"
        choice = "replay"
        while choice.lower() == "replay":
            play_single_frequency(note_hz, .3)
            choice = str(raw_input("Enter the note & octave e.g. A#4: "))
        if choice == convert_to_letter_pitch(note_hz):
            score += 1
            print "nice"
        else:
            print "NOOOO: {0}".format(convert_to_letter_pitch(note_hz))
    print "Game over, you scored: {0} out of {1}".format(score, rounds)
