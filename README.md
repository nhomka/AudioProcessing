<h3>Current Implementation</h3>

Right now, you can run the main.py program,
which gives text outputs with relevant
information.

Running the script begins a quick little game.
First, 5 seconds of audio will be recorded from
your microphone.  The highest and lowest pitches
heard during this time will be recorded.
After this calibration, I display a plot
of frequency vs time to view the recorded
audio sample.  After closing, 10 random notes
in the relevant interval will be printed.
you will have 3 seconds to prepare for each,
and 1 second of audio will be recorded.
The goal is to match the written pitch.  
I've done this with whistling and violin,
both of which work well enough for now,
though there's plenty of room for
improvement.


<h3>Current Project</h3>

I'm working on expanding this to some
interesting music applications, the main 
achievable goal being scale intonation 
analysis.  The idea here is to be able 
to set a scale, play it a few times a day,
and get some sort of metric as to how
accurate your intonation was.  While I
don't think this will be of especially
great value to a musician with a good 
enough ear to hear their own mistakes, 
I'm curious to look at the resulting data. 