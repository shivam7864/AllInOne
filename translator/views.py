from django.shortcuts import redirect, render
from googletrans import Translator, LANGUAGES
import pyttsx3

# Create your views here.

def index(request):
    langs = list(LANGUAGES.values())
    
    global text
    if request.method=="POST":
        text = request.POST['text']
        print(text)
        from1 = request.POST['from']
        to = request.POST['to']

        trans = Translator()
        trans1 = trans.translate(text, src=from1, dest=to)
        translated=trans1.text
        return render(request,"translator/index.html", {'translated':translated, 'langs':langs, 'text':text})

    
    return render(request, "translator/index.html", {'langs':langs})

# def speak(request):
#     if request.method=="POST":
#         engine = pyttsx3.init()
#         global text
#         while True:
#             engine.say(text)
#             engine.runAndWait()
            

#     return render(request,'translator/speak.html')