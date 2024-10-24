import speech_recognition as sr
import pyaudio

reconocedor = sr.Recognizer()

with sr.Microphone() as mic:
    reconocedor.adjust_for_ambient_noise(mic, duration=1)
    audio = reconocedor.listen(mic)
    texto = reconocedor.recognize_google(audio)
    texto = texto.lower()
    print("Estas son tus palabras -->", texto)
