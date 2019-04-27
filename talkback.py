from gtts import gTTS
import speech_recognition as sr
import os
import webbrowser
from pydub import AudioSegment
from pydub.playback import play



def talktome(audio):
    print(audio)
    tts = gTTS(text=audio, lang="en")
    tts.save('audio.wav')

    song = AudioSegment.from_mp3("audio.wav")
    play(song)

#listen

def myCommand():
    r = sr.Recognizer()
    
    with sr.Microphone() as source:
        print('I am ready for you next command')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration= 1)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        print("You said" + command + "\n")
    
    #loop back

    except sr.UnknownValueError:
        assistant(myCommand())

    return command

#if

talktome("hey")






print("Program exited sucessfully")