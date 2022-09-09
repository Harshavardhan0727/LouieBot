import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setproperty('voices', voices[0].id)


def speak(audio):
