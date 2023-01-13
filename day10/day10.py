

from earsketch import *
init()
#can be run at https://earsketch.gatech.edu/earsketch2/
#prompt is generative music
setTempo(90)
for i in range(2):
 start = i*15
 fitMedia (AK_UNDOG_ACOUSTIC_GUITAR_1, 1, 1+start, 4+start)
 fitMedia (AK_UNDOG_ACOUSTIC_GUITAR_3, 2, 3+start, 5+start)
 setEffect(3, VOLUME, GAIN, -7.0)
 fitMedia (AK_UNDOG_ACOUSTIC_GUITAR_1, 3, 5+start, 8+start)
 fitMedia (AK_UNDOG_PAD_1, 5, 9+start, 12+start)
 fitMedia (AK_UNDOG_PAD_2, 6, 6+start, 12+start)
 fitMedia (AK_UNDOG_PIANO_1, 7, 9+start, 14+start)
 fitMedia (AK_UNDOG_BASS_2, 2, 13+start, 16+start)
 fitMedia (AK_UNDOG_BASS_3, 9,16+start,17+start)
finish()