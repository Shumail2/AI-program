import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pywhatkit


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[0].id)







def speak(audio):
    
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour==0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!") 

    else:
        speak("Good night!")
    
    speak(" I am jarvis sir. please tell me how may i help you")
    
def takeCommand():
    #it takes microphone input from the user and returns tring output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
        
        
       

 
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
        
        

    except Exception as e:
        print("say that again please...")   
        return"None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('info.clothingmagnet.com','98183314Sa')
    server.sendmail('info.clothingmagnet.com',to, content)
    server.close()

if __name__== "__main__":
     wishMe()
     while 1:
    

        query = takeCommand().lower()

        #logic for executing taks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'play tu hi hai' in query:
            webbrowser.open("https://youtu.be/KyMNLIYRsR4")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")


         

        elif 'the time' in query:
            strTIme = datetime.datetime.now().strftime("%H,%M,%S")
            speak(f"Sir, the time is {strTIme}")

        elif 'open code' in query:
            codepath = "C:\\Users\\SHUMAIL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'email to subhan' in query:
            try:
                speak("what should  I say?")
                content = takeCommand()
                to = "ali9445sabir@gmail.com "
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("sorry shumyl. I am not able to send this email")
        
        elif 'play' in query:
          try:
            song= query.replace('play', '')

            
            speak(song)
            pywhatkit.playonyt(song)

          except: 
            pass 
            
        
            
       

takeCommand()



        
        
        
        
        


 

    

