import speech_recognition
import pyttsx3

recognizer = speech_recognition.Recognizer()

punctuations = ['.', '?']

while True:

    try:

        with speech_recognition.Microphone() as mic:

            recognizer.adjust_for_ambient_noise(mic, duration=0.2)
            audio = recognizer.listen(mic)

            text = recognizer.recognize_google(audio)
            text = text.lower()

            print(f"Recognized {text}")

    # except speech_recognition.UnknownValueError():
    except Exception as e:

        recognizer = speech_recognition.Recognizer()
        continue

