import speech_recognition as sr
import pyaudio
from .tts import text_to_speech

def speech_to_text():
    try : 
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print('Please say something')
            audio = r.listen(source)
        text = r.recognize_google(audio)
        return text
    except:
        text_to_speech('I cannot hear you, please try again or say i am satisfied with my care to quit')
        return 'none'