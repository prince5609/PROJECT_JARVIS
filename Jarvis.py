import pyttsx3  # pip install pyttsx3
import datetime
import speech_recognition as sr  # pip install speechRecognition
import wikipedia  # pip install wikipedia
import webbrowser
import os
import random
import smtplib
import requests
from bs4 import BeautifulSoup
import operator

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # This is inbuilt voices in our windows


def speak(audio):  # This will help to speak
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 12 > hour >= 0:
        speak("Good Morning sir!")

    elif 17 > hour >= 12:
        speak("Good Afternoon sir!")

    else:
        speak("Good Evening sir!")

    speak("I Am Jarvis.")
    speak("How May I Help You?")


def sentEmail(to, content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmail.com", "password")
    server.sendmail("youremail@gmail.com", to, content)
    server.close()


def takeCommand():  # It takes microphone input from user and returns it as string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1  # This means it will stop for 1 sec after user stop speaking
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
    query = takeCommand().lower()
    if "wake up" in query:
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
                speak("My name is Jarvis")

            elif "who are you" in query:
                speak("I am Jarvis")

            elif "the time" in query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"the time is {strTime}")

            elif "how are you" in query:
                speak("i am all well. what about you?")
                query = takeCommand().lower()
                if "i am good" in query or "i am also good" in query or "i am fine" in query:
                    speak("wao! that sound good")

                elif "i am not good" in query or "i am not fine" in query:
                    speak("ohh. i feel bad for that")

            elif "what is your age" in query:
                speak("sir i am just 25")

            elif "how old are you" in query:
                speak("o dear! age is just a number so forget it")

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

            elif "get lost" in query:
                speak("oh my dear! maybe you got angry with me, anyway goodbye!, take care")
                break

            elif "good night" in query:
                speak("good night sir, have sweet dreams")
                break

            elif "i am getting bored" in query:
                speak("But why. you can spend time with me. or can read books or play games or whatever makes you "
                      "happy... "
                      "should i do something for you?")

            elif "what do you do" in query:
                speak("i just makes people happy")

            elif "will you marry me" in query:
                speak("No i am job less")

            elif "today is my birthday" in query:
                speak("that's a great day then. wish you a very very happy returns of the day dear. happy birthday")

            elif "play video songs" in query:
                video_add = "G:\VIDEO SONGS"
                songs = os.listdir(video_add)
                songs_num = random.randint(0, len(songs) - 1)
                os.startfile(os.path.join(video_add, songs[songs_num]))

            elif "open github" in query:
                webbrowser.open("www.github.com")

            elif "will you be my boyfriend" in query:
                speak("well! who are you? i mean what do you do for living?")
                query = takeCommand()
                speak("ok. i will think of you later")

            elif "kya kr rahe ho" in query or "kya kar rahe ho" in query:
                speak("kuch nahi. tum batao")

            elif "what are you doing" in query:
                speak("i was just thinking, that i were a prime minister. i would have changed the nation")

            elif "i am not feeling well today" in query:
                speak("oo i feel bad for you. have you taken your breakfast or dinner?")
                query = takeCommand()
                if "no" in query:
                    speak("then you should have it. may be you will start feeling good after it")
                elif "yes" in query:
                    speak("that's really good, i think you should go for a walk than, maybe it can help!")

            elif "who is prince" in query:
                speak("well you are asking me about a lovely person, anyway he is my creator, so he is smart")

            elif "play party songs" in query:
                webbrowser.open("www.youtube.com/results?search_query=party+songs")

            elif "play romantic songs" in query:
                webbrowser.open("www.youtube.com/results?search_query=romantic+songs")

            elif "temperature" in query:
                search = "temperature in ghaziabad"
                url = f"https://www.google.com/search?q={search}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(f"current {search} if {temp}")

            elif "thank you" in query:
                speak("your most welcome sir")

            elif "google" in query:
                url = f"http://www.google.com/search?q={query}"
                r = requests.get(url)
                data = BeautifulSoup(r.text, "html.parser")
                temp = data.find("div", class_="BNeawe").text
                speak(temp)

            elif "do calculation" in query or "can you calculate" in query:
                try:
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        speak("sure. what you want to calculate, for example 5 multiplied by 5")
                        print("listening...")
                        r.adjust_for_ambient_noise(source)
                        audio = r.listen(source)
                    my_string = r.recognize_google(audio)
                    print(my_string)


                    def get_operator_fn(op):
                        return {"+": operator.add,
                                "-": operator.sub,
                                "x": operator.mul,
                                "divided": operator.__truediv__,
                                }[op]

                    def eval_binary_expr(op1, oper, op2):
                        op1, op2 = int(op1), int(op2)
                        return get_operator_fn(oper)(op1, op2)
                    speak("your result is")
                    speak(eval_binary_expr(*(my_string.split())))
                except:
                    continue
