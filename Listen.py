import speech_recognition as sr

def Listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening..")
        r.energy_threshold = 5000
        r.pause_threshold = 1
        audio = r.listen(source,0,3) #0,5

    try:
        print("=>Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said : {query}\n")

    except:
        return ""

    query = str(query)
    return query.lower()

