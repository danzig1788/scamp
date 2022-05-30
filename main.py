from scamp import *

s = Session()

#s.print_default_soundfont_presets()

clarinet = s.new_part('clarinet')
oboe = s.new_part('oboe')

# Play note takes 3 arguments: 1=midi pitch; 2=vol (range is 0 to 1): 3=duration (in seconds by default)
for pitch in range(65,77):
    clarinet.play_note(pitch,.8,.25)
    oboe.play_note(pitch,.8,.25)