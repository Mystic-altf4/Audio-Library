import speech_recognition
def s():
    mic = speech_recognition.Microphone()
    record = speech_recognition.Recognizer()

    with mic as ses:
        record.adjust_for_ambient_noise(ses)
        echo = record.listen(ses)
    try:    
        return record.recognize_google(echo,language = "tr-TR")
    except:
        return "Anlamadım"

def l():
    mic = speech_recognition.Microphone()
    record = speech_recognition.Recognizer()

    with mic as ses:
        record.adjust_for_ambient_noise(ses)
        echo = record.listen(ses)
    try:    
        return record.recognize_google(echo,language = "en-US")
    except:
        return "?"
if __name__ == "__main__":
    print("KONUŞ KÖLE")
    x = s()
    print(x)
