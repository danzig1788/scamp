

from scamp import *

s = Session()
s.tempo = 120

#s.print_default_soundfont_presets()

clarinet = s.new_part('clarinet')
oboe = s.new_part('oboe')

# Set up a series of pitches and corresponding durations
pitch_list = [60,64,66,69,67,64,60,57,54,54,54,55]
durs_list = [1.5,1.0,1.0,0.5,1.5,1.0,1.0,0.5,0.5,0.5,0.5,0.5]


# Play note takes 3 required arguments: 1=midi pitch; 2=vol (range is 0 to 1): 3=duration (in seconds by default)
# and an optional, all-purpose, 4th argument, "properties"
for pitch, duration in zip(pitch_list,durs_list):
    clarinet.play_note(pitch,.8,duration, 'staccato')
    #oboe.play_note(pitch,.8,duration)