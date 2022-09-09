import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)
engine.setProperty('rate', 180)


def speak(audio):
    engine.say(audio)  # engines will speak the audio string.
    engine.runAndWait()  # just to wait
    print("Louie: " + audio)


def Takecommand():
    speak("Hola")

def TaskExe():

    while True:

        querySpanish = Takecommand()

