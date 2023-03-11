import speech_recognition
import pyttsx3
recognizer=speech_recognition.Recognizer()
while True:
    try:
        with speech_recognition.Microphone() as mic:
            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio=recognizer.listen(mic)
            text=recognizer.recognize_google(audio)
            text=text.lower()
            print(f"Recognised {text}")
    except speech_recognition.UnknownValueError():

        recognizer=speech_recognition.Recognizer()
        continue
        //import speech_recognition as s
#create a object of Recognizer
sr=s.Recognizer()
print("i am your script and listening you...........................")
with s.Microphone() as m:
    audio=sr.listen(m)
    query=sr.recognize_google(audio,language='eng-in')
    print(query)//
