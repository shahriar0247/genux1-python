

#inheriting stuf

import speech_recognition as sr
import os
import webbrowser
import subprocess



#making r meaningful

r = sr.Recognizer()

#getting the microphone and printing "Say Something" after getting it

with sr.Microphone() as source:
    print("Say Something")
    #making audio the thing we said (in sound)
    audio = r.listen(source)

#makind said the thing we said (in text)

said = r.recognize_google(audio)
said = said.lower()

#what will happen if said is a certain thing 
print("You have said " + said)


if "search" in said:
    if "google" in said:
        said = said.replace("search in google for", "")
        said = said.replace("search google", "")
        said = said.replace("search in google", "")
        said = said.replace("search google for", "")
        said = said.replace(" ", "+")
        webbrowser.open("https://www.google.com/search?q=" + said)