import pyttsx3
import speech_recognition as sr
import os
import datetime
import smtplib
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

global assname
assname = 'Bixby'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greetings(an):
    hour = int(datetime.datetime.now().hour)
    speak('Hello! Warm Greetings')
    speak(f'This is your assistant {an}')
    if hour>= 0 and hour<12:
        speak("Good Morning!")
  
    elif hour>= 12 and hour<18:
        speak("Good Afternoon!")  
  
    else:
        speak("Good Evening!")

def username():
    speak("What should i call you?")
    uname = takeCommand()
    speak("Welcome!!")
    speak(uname)

def takeCommand():
     
    r = sr.Recognizer()
     
    with sr.Microphone() as source:
         
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
  
    try:
        print("Recognizing...")   
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")
  
    except Exception as e:
        print(e)   
        print("Unable to Recognize your voice.") 
        return "None"
     
    return query

def rename():
    an = takeCommand()
    global assname
    assname = an
    speak(f'Thank You for renaming me! I am {an}')

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
     
    # Enable low security in gmail
    server.login('email', 'password')
    server.sendmail('email', to, content)
    server.close()

clear = lambda: os.system('cls')
     
    # This Function will clean any
    # command before execution of this python file
clear()
greetings(assname)
username()

while True:
    query = takeCommand().lower()
    
    if 'open spotify' in query:
        speak('Opening Spotify')
        webbrowser.open('https://open.spotify.com/')
    elif 'open youtube' in query:
        speak('Opening YouTube')
        webbrowser.open('https://www.youtube.com/')
    elif 'exit' in query:
        speak('Bye!!')
        break
    elif 'open browser' in query:
        speak('Opening Brave')
        path = r'C:\Program Files\BraveSoftware\Brave-Browser\Application\Brave.exe'
        os.startfile(path)
    elif 'rename' in query:
        rename()
        greetings(assname)
    elif 'send a mail' in query:
        try:
            speak("What should I say?")
            content = takeCommand()
            speak("whom should i send")
            to = input()   
            sendEmail(to, content)
            speak("Email has been sent !")
        except Exception as e:
            print(e)
            speak("I am not able to send this email")
    elif 'how are you' in query:
        speak('I am fine!')
    elif 'who created you' in query:
        speak('Mr. Vedant Doshi')
    elif 'i love you' in query:
        speak('I Love You too!')
    elif 'set an alarm' in query:
        os.system('python alarm.py')
    elif 'play a game' in query:
        os.system('python flappy_bird.py')
    else:
        speak("Sorry I don't understand!")
    