import pyttsx3

engine = pyttsx3.init()
# text = "हर्षित एक पालतू कुत्ता है"
text="hell"

engine.say(text)
engine.runAndWait()