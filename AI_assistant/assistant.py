import pyttsx3
import speech_recognition as sr

#initialize object variable thing
robo_speech = pyttsx3.init()
robo_is_listening = sr.Recognizer()

#listen
with sr.Microphone() as mic:
	print("Robo: I am ALWAYS listening...")
	robo_is_listening.adjust_for_ambient_noise(mic, duration=1)
	audio = robo_is_listening.listen(mic, timeout=3)
print("Robo: ...")
try:
	you = robo_is_listening.recognize_google(audio)
except:
	you = " "

print("The meat bag says: " + you)

#input tex
#text = input("Type text for the robo to say: ")

#talk!
#robo_speech.say("The meat bag says: " + you)
#robo_speech.runAndWait()
