import speech_recognition as sr
import webbrowser

recognizer = sr.Recognizer()

with sr.Microphone() as san:
    print("Mic is ready to Listening...")
    audio = recognizer.listen(san)
    query = recognizer.recognize_google(audio)
    print(f"Finding : {query}")

    if "amazon" in query.lower():
        url = f"https://www.amazon.in/s?k= {query}"
    else:
        url = f"https://www.google.com/search?q= {query}"

webbrowser.open(url)


