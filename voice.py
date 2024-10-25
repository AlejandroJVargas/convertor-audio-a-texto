import speech_recognition as sr
import pyaudio

reconocedor = sr.Recognizer()

while True:
    try:
        with sr.Microphone() as mic:
            reconocedor.adjust_for_ambient_noise(mic)
            print(
                "Ahora puedes decir unas palabras por un minuto: (Si queres salir, solo di 'salir')"
            )
            audio = reconocedor.listen(mic, timeout=120, phrase_time_limit=120)
            texto = reconocedor.recognize_google(audio, language="es-ES")
            texto = texto.lower()
            print("Estas son tus palabras -->", texto)

            if "salir" in texto:
                print("Haz terminado el programa...")
                break
    except sr.UnknownValueError:
        print(
            "Lo sentimos, no logramos comprender lo que dijiste. Intentalo nuevamente"
        )
    except sr.RequestError:
        print("Lo sentimos hubo un error de conexion con servidores de Google")
