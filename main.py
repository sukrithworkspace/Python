
import speech_recognition as sr
import pyttsx3

# Initialize voice engine
engine = pyttsx3.init()

# Speak function
def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()

# Listen function
def listen():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("\nListening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You:", text)
        return text.lower()

    except sr.UnknownValueError:
        speak("Sorry, I did not understand.")
        return ""

    except sr.RequestError:
        speak("Internet connection problem.")
        return ""

# Main program
def start_assistant():
    speak("Hello! I am your voice assistant.")
    speak("How can I help you?")

    while True:
        command = listen()

        if "hello" in command:
            speak("Hello! How are you?")

        elif "your name" in command:
            speak("I am your Python voice assistant.")

        elif "how are you" in command:
            speak("I am fine. Thank you!")

        elif "exit" in command or "stop" in command:
            speak("Goodbye! Have a nice day.")
            break

        elif command == "":
            continue

        else:
            speak("Sorry, I don't know that command.")

# Run assistant
if __name__ == "__main__":
    start_assistant()
