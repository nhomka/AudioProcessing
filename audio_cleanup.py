import datetime


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