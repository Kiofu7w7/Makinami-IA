import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
mic = sr.Microphone()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-30)

text = ''

def talk(text):
     engine.say(text)
     engine.runAndWait()


while text != 'puerta de madera':
    with mic as source:
            text= ''
            try:
                audio = recognizer.listen(source)
                text = recognizer.recognize_google(audio, language = 'ES')
            except sr.exceptions.UnknownValueError:
                print("nada")
            if text == 'Hola':
                talk('Hola mijo como esta')
            print(f'Has dicho: {text}')
