import speech_recognition as sr
import PyAudio

r = sr.Recognizer()

with sr.Microphone() as source:
    print('Speak anything ')
    audio = r.listen(source,timeout=1,phrase_time_limit=10)

    try:
        text=r.recognize_google(audio)
        print('you said : {}'.format(text))
    except:
        print('Sorry Unable to hear your voice')