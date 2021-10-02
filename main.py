import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import smtplib

import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# print(voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning!")
    elif hour >= 12 and hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good Evening!")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print(e)
        print("say that again please")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('', '')
    server.sendmail('', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()
        if 'what is' in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia..")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")


        elif 'how are you' in query:
            speak("I am fine sir..how about you?")

        elif 'coronavirus news' in query:
            speak("searching sir...")
            webbrowser.open("https://www.google.com/search?q=covid+status+mumbai&rlz=1C1CHBF_enIN874IN875&oq=covid+st&aqs=chrome.2.69i57j0i433i457i512j0i402l2j0i433i512l3j0i512l3.4472j0j15&sourceid=chrome&ie=UTF-8")

        elif 'open live cricket score' in query:
            speak("fetching sir...")
            webbrowser.open("https://www.google.com/search?q=cricket+live+score+india&rlz=1C1CHBF_enIN874IN875&sxsrf=AOaemvL2oYP7d_3cS1Op6VmtVy0m3ZhdgA%3A1633173979477&ei=20FYYcHBHI3dz7sPnsSr4AY&ved=0ahUKEwiBm5yXz6vzAhWN7nMBHR7iCmwQ4dUDCA4&uact=5&oq=cricket+live+score+india&gs_lcp=Cgdnd3Mtd2l6EAMyBQgAEIAEMggIABCABBCxAzIFCAAQgAQyBQgAEIAEMgUIABCABDILCAAQgAQQsQMQgwEyBQgAEIAEMgsIABCABBCxAxCDATIFCAAQgAQyBQgAEIAEOgcIABBHELADOgcIABCwAxBDOgoILhDIAxCwAxBDOhAIABCABBCxAxCDARBGEP0BSgUIOBIBMUoECEEYAFCwHVigMGCeMWgBcAJ4AIAB4wOIAY8NkgEHMi0yLjEuMpgBAKABAcgBD8ABAQ&sclient=gws-wiz")


        elif 'send email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "tejas.shinde8101@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send this email")

        else:
            speak("good bye sir!")



