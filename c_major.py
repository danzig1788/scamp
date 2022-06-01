from scamp import *

s = Session()
s.tempo = 120

# Set up the parts
piano = s.new_part('piano')

piano.play_note(60,1,1)