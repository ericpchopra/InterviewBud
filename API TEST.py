import speech_recognition as sr
import pyaudio
import pyttsx3

r= sr.Recognizer()
mic = sr.Microphone()

def Speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


p = pyaudio.PyAudio()
# for i in range(p.get_device_count()):
#     print(p.get_device_info_by_index(i))

# with sr.Microphone(1) as source:
#     r.adjust_for_ambient_noise(source, 1)  # Adjust for ambient
#     print("Say something!")
#     audio=r.listen(source)
# print("Runnnnnn")
# try:
#     print("Analyzing voice data  "+r.recognize_google(audio))
# except Exception:
#     print("Something went wrong")

Speak("yoyo yooo yoo yo")