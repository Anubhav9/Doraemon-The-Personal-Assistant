import speech_recognition as sr
import subprocess
import os
import webbrowser
from gtts import gTTS 
from playsound import playsound 
import pyttsx3
import signal

# Initialize recognizer class (for recognizing the speech)

r = sr.Recognizer()
engine = pyttsx3.init() 

# Reading Microphone as source
# listening the speech and store in audio_text variable
engine.say("Hello Anubhav, I am Doraemon and I am your personal assistant How may I help you today?")
engine.runAndWait()
with sr.Microphone() as source:
	print("Talk")
	audio_text = r.record(source,duration=5)
	print("Time over, thanks")
# recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
    
	u=r.recognize_google(audio_text)
	engine.say(u)
	engine.runAndWait()

		
u=u.split(" ")
print(u[0])
if(u[0]=='open'):
	if(u[1]=='Android'):
		engine.say("Opening Android Studio for you")
		engine.runAndWait()
		subprocess.Popen('/home/anubhav/android-studio/bin/studio.sh')
	elif(u[1]=='sublime'):
		engine.say("Opening Sublime Text")
		engine.runAndWait()
		os.system("/opt/sublime_text/sublime_text %F")
	elif(u[1]=='Google'):
		engine.say("What do you want to search")
		engine.runAndWait()
		with sr.Microphone() as source:
			audio_text=r.record(source,duration=5)
			u=r.recognize_google(audio_text)
		string1='https://www.google.com/search?q='
		string2=u
		string1=string1+string2
		webbrowser.open(string1) 
		exit()
	elif(u[1]=='Wikipedia'):
		engine.say("What do you want to search for Wikipedia")
		engine.runAndWait()
		with sr.Microphone() as source:
			audio_text=r.record(source,duration=5)
			u=r.recognize_google(audio_text)
		string1='https://en.wikipedia.org/wiki/'
		string2=u
		string1=string1+string2
		temp="searching Wikki for"+string2
		engine.say(temp)
		engine.runAndWait()
		webbrowser.open(string1)
	elif(u[1]=='YouTube'):
		engine.say("What do you want to search in YouTube")
		engine.runAndWait()
		with sr.Microphone() as source:
			audio_text=r.record(source,duration=5)
			u=r.recognize_google(audio_text)

    		
		string1='https://www.youtube.com/results?search_query='
		string2=u
		string1=string1+string2
		temp="searching youtube for"+string2
		engine.say(temp)
		engine.runAndWait()
		webbrowser.open(string1)
	elif(u[1]=='stack'):
		engine.say("What do you want to search in Stack Overflow")
		engine.runAndWait()
		with sr.Microphone() as source:
			audio_text=r.record(source,duration=5)
			u=r.recognize_google(audio_text)
		string1='https://stackoverflow.com/search?q='
		string2=u
		string1=string1+string2
		temp="searching stack overflow for"+string2
		engine.say(temp)
		engine.runAndWait()
		webbrowser.open(string1)  






