
import speech_recognition as sr
import pyttsx3
import pywhatkit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)






def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    listener=sr.Recognizer()
    try:
        with sr.Microphone() as source:
            print("Listeneing")
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            engine = pyttsx3.init('sapi5')
            song= command.replace('play', '')

            
            speak(song)
            pywhatkit.playonyt(song)

    except:
        print("error")

takeCommand()
          