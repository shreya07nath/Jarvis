import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import subprocess as sp
import pywhatkit as kit
import smtplib

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wish():
    hour=int(datetime.datetime.now().hour)
    if(hour >= 0 and hour < 12):
        speak("Good Morning!")
        
    elif(hour >= 12 and hour < 18):
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak("I am Jarvis. How may I be of service to you Shreya?")

def command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening to you....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing what you just said...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You Said: {query}\n")

    except Exception as e:
        print("Shreya, could you please say that again?")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('put in your email here' , 'put in your password here')
    server.send('put in your email here' , to , content)

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

if __name__ == '__main__':
    wish()
    while True:
        query = command().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace("wikipedia", "")
            results=wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia...")
            print(results)
            speak(results)
        
        elif 'open youtube' in query:
            speak("Right away Shreya")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Sure thing Shreya")
            webbrowser.open("google.com")

        elif 'open facebook' in query:
            speak("Right away Shreya")
            webbrowser.open("facebook.com")

        elif 'open prime video' in query:
            speak("Right away Shreya")
            webbrowser.open("primevideo.com")

        elif 'open twitter' in query:
            speak("Opened it in a new tab Shreya")
            webbrowser.open("twitter.com")

        elif 'open instagram' in query:
            speak("Sure thing Shreya")
            webbrowser.open("instagram.com")

        elif 'open stackoverflow' in query:
            speak("Right away Shreya")
            webbrowser.open("stackoverflow.com")

        elif 'open spotify' in query:
            speak("Opened it in a new tab Shreya")
            webbrowser.open("spotify.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'open code' in query:
            speak("Right away Shreya")
            codePath = "C:\\Users\\KIIT\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'open discord' in query:
            speak("I am on it Shreya")
            discordPath = "C:\\Users\\KIIT\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Discord Inc\\Discord.lnk"
            os.startfile(discordPath)

        elif 'open camera' in query:
            sp.run('start microsoft.windows.camera:', shell=True)

        elif 'open cmd' in query:
             os.system('start cmd')
           
        elif "send whatsapp message" in query:
            speak('On what number should I send the message? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message?")
            message = command().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message.")

        elif 'email to shreya' in query:
            try:
                speak("What should I say?")
                content = command()
                to = "write in the email you want to send to"
                sendEmail(to, content)
                speak("Your email has been sent!!")
            except Exception as e:
                print(e)
                speak("Something went wrong! I could not send your email Shreya, please try again")

        elif 'bye' or 'exit' or 'quit' in query:
            speak("Goodbye Shreya!")
            os._exit(1)