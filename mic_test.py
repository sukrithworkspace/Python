
import speech_recognition as sr

recognizer = sr.Recognizer()

# Microphone settings
recognizer.energy_threshold = 200
recognizer.dynamic_energy_threshold = True

print("Checking microphone...")

try:
    with sr.Microphone() as source:

        print("Microphone connected!")

        print("Adjusting background noise...")
        recognizer.adjust_for_ambient_noise(
            source, duration=2
        )

        print("Speak now! Waiting for your voice...")

        audio = recognizer.listen(
            source,
            timeout=15,
            phrase_time_limit=10
        )

        print("Processing voice...")

        text = recognizer.recognize_google(audio)

        print("You said:", text)

except sr.WaitTimeoutError:
    print("No voice detected. Check your microphone.")

except sr.UnknownValueError:
    print("Sorry, voice not understood.")

except sr.RequestError:
    print("Internet connection problem.")

except Exception as e:
    print("Error:", e)
