from gtts import gTTS
import os
from playsound import playsound


def text_to_speech(text, language='en', filename='output.mp3'):
    tts = gTTS(text=text, lang=language)
    tts.save(filename)
    playsound(filename)
    os.remove(filename)
    #os.system(f"start {filename}") 
