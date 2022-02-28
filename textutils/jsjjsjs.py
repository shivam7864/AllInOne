import pywhatkit as pw
from pywhatkit.remotekit import start_server
from flask import Flask, request
txt=''' Besides web and software development, Python is used for data analytics, machine learning, and even design. We take a closer look at some of the uses of Python, as well as why it's such a popular and versatile programming language.'''
# piu=pw.sendwhatmsg("+918853546400", "Hi", 14, 41)


pw.text_to_handwriting(txt)
print("END")