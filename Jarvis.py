import pyttsx3    # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install speechRecognition
import wikipedia    # pip install wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)  # This is inbuilt voices in our windows


def speak(audio):  # This will help to speak
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 12 > hour >= 0:
        speak("Good Morning")

    elif 17 > hour >= 12:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I Am Myra. Please Tell Me What Can I Do For You")


def sentEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "password")
    server.sendmail("youremail@gmail.com", to, content)
    server.close()


def takeCommand():  # It takes microphone input from user and returns string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # This means it will stop for 1 sec after user speak
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("Say That Again Please...")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("Searching wikipedia for You")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=1)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")

        elif "open google" in query:
            webbrowser.open("www.google.co.in")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir = "G:\Songs"
            songs = os.listdir(music_dir)
            song_num = random.randint(0, len(songs) - 1)
            os.startfile(os.path.join(music_dir, songs[song_num]))

        elif "what is your name" in query:
            speak("I am Myra")

        elif "who are you" in query:
            speak("I am Myra")

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif "how are you" in query:
            speak("i am all all well. what about you?")

        elif "i am good" in query:
            speak("wao that sound good")

        elif "i am also good" in query:
            speak("wao that sound good")

        elif "i am fine" in query:
            speak("wao that sound good")

        elif "i am not good" in query:
            speak("ohh i feel sorry for that")

        elif "i am not fine" in query:
            speak("ohh i feel sorry for that")

        elif "what is your age" in query:
            speak("are you thinking of marrying me, ohhhh that's the bad idea")

        elif "how old are you" in query:
            speak("o dear age is just a number so forget it")

        elif "open zoom" in query:
            zoom_path = "C:\\Users\\PRINCE\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
            os.startfile(zoom_path)

        elif "send email" in query:
            try:
                speak("what should i send?")
                content = takeCommand()
                to = "your email.com"
                sentEmail(to, content)
                speak("email has been sent!")
            except Exception as e:
                speak("sorry yar, i am not able to send this email")

        elif "stop" in query:
            break

        elif "bye" in query:
            speak("good bye dear, have a nice time")
            break
