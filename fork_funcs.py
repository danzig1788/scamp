from scamp import *

s = Session()

# Set up the parts
brass = s.new_part('brass')
trumpet = s.new_part('trumpet')

# Define the music functions
def beat_it_1( transposition, short_length, medium_length, long_length ):
    brass.play_note( 40 + transposition, 1, short_length )
    brass.play_note( 43 + transposition, 1, short_length )
    brass.play_note( 47 + transposition, 1, short_length )
    brass.play_note( 55 + transposition, 1, short_length )
    brass.play_note( 52 + transposition, 1, long_length )

def beat_it_2( transposition, short_length, medium_length, long_length ):
    brass.play_note( 54 + transposition, 1, medium_length )
    brass.play_note( 52 + transposition, 1, short_length )
    brass.play_note( 50 + transposition, 1, short_length )
    wait( short_length )
    brass.play_note( 50 + transposition, 1, short_length )
    wait( long_length )

def beat_it_full( transposition, short_length, medium_length, long_length ):
    beat_it_1( transposition, short_length, medium_length, long_length )
    beat_it_2( transposition, short_length, medium_length, long_length )

def top_part():
    trumpet.play_note( 71, 1, .25 )
    trumpet.play_note(71, 1, 1.75)
    trumpet.play_note(71, 1, .25)
    trumpet.play_note(71, 1, 1.5)
    trumpet.play_note(71, 1, .5)
    trumpet.play_note(71, 1, .25)
    trumpet.play_note(71, 1, .25)
    trumpet.play_note(71, 1, .25)
    trumpet.play_note(74, 1, .5)
    trumpet.play_note(71, 1, .25, {'articulation':'staccato'})
    trumpet.play_note(74, 1, .5)
    trumpet.play_note(71, 1, .25, {'articulation':'staccato'})

s.fork( beat_it_full, args=[ 0, .25, .5, .75 ] )
s.fork( beat_it_full, args=[ 12, .25, .5, .75 ] )
s.fork( beat_it_full, args=[ 24, .25, .5, .75 ] )
s.fork( top_part )
s.wait_for_children_to_finish()