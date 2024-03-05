import speech_recognition as sr

def voice_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the audio source
    with sr.Microphone() as source:
        print("Say something:")
        audio_data = recognizer.listen(source)

        try:
            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio_data)
            print(f"Text: {text}")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    voice_to_text()
