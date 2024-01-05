from pydub import AudioSegment
from pydub.playback import play
breakpoint()
song = AudioSegment.from_mp3(r"C:\ML Projects\JARVIS---AI-Assistant\output.mp3")
print('playing sound using  pydub')
play(song)