import math

pitches = {0: "C", 1: "C#", 2: "D", 3: "D#", 4: "E", 5: "F",
           6: "F#", 7: "G", 8: "G#", 9: "A", 10: "A#", 11: "B"}


def convert_to_letter_pitch(freq, middle_a=440):
    a_4 = middle_a
    c_0 = a_4 * pow(2, -4.75)
    # print freq, a_4, c_0
    h = round(12 * math.log(freq/c_0, 2))
    octave = h//12
    return pitches[h % 12] + str(int(octave))


def convert_interval_to_letter_pitch(interval):
    octave = interval // 12
    pitch = pitches[interval%12]
    return pitch+str(octave)


def convert_letter_pitch_to_interval(pitch):
    return int(pitch[-1]) * 12 + [i for i, j in pitches.items() if j == pitch[:-1]][0]
