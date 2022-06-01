from scamp import *

s = Session()
s.tempo = 120

# Set up the parts
piano = s.new_part('piano')

def custom_note( part, midi_pitch, vol, dur ):
    part.play_note( midi_pitch, vol, dur)

def g_3_minor( a_session, part, vol, dur ):
    a_session.fork( custom_note, args=[ part, 67, vol, dur ] )
    a_session.fork(custom_note, args=[part, 70, vol, dur])
    a_session.fork(custom_note, args=[part, 74, vol, dur])
    a_session.wait_for_children_to_finish()

def b_2_flat_major( a_session, part, vol, dur ):
    a_session.fork( custom_note, args=[ part, 58, vol, dur ] )
    a_session.fork(custom_note, args=[part, 62, vol, dur])
    a_session.fork(custom_note, args=[part, 65, vol, dur])
    a_session.wait_for_children_to_finish()

def e_3_flat_major( a_session, part, vol, dur ):
    a_session.fork( custom_note, args=[ part, 63, vol, dur ] )
    a_session.fork(custom_note, args=[part, 67, vol, dur])
    a_session.fork(custom_note, args=[part, 70, vol, dur])
    a_session.wait_for_children_to_finish()

g_3_minor( s, piano, 1, 1.5)
b_2_flat_major( s, piano, 1, 1.5)
e_3_flat_major( s, piano, 1, 1.5)
b_2_flat_major( s, piano, 1, 1.5)
#s.wait_for_children_to_finish()