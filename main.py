#iterable - an object/collection that can b iterated thru a loop
import time
from vosk import Model, KaldiRecognizer
import pyaudio 
#lists [], tuples (), sets {} are all iterable
#strings are also iterable
#dictionaries are iteranbe

#membership operators (in or not in) (string, list, tuple, set, dict)

#list comprehension in python = concise way to create lists
#for every value in an interable check if works

#formula = expression for value in iterable if condition <- optiona;

#matchcase statements or switch: execute code if value == case
#match name: case 1: .... case 2: .... case _: ...

#modules: a file containing code u want in ur program
#eg import time, math, etc

#variable scope: LEGB (local, enclosed, global, built in)

#if name==main:..if we dont run this program directly, dont do it

#object = a bundle of related attributes (variables) and 
#  methods (functions)
# object =  cup is object (liquid inside, temperature, attributes)
#           methods for cup is fill, drink and empty.
#           class is a blueprint used to design the structure and layout of object


model = Model(r"C:\Users\ayaan\OneDrive\Desktop\Assistive Project\vosk-model-small-en-us-0.15\vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()
stream = mic.open(format=pyaudio.paInt16, channels = 1, rate=16000, input = True, frames_per_buffer = 8192)

stream.start_stream()

while True:
    data = stream.read(4096)
    if len(data) ==0:
        break
    if recognizer.AcceptWaveform(data):
        text = recognizer.Result()
        print(text)
        print(text[14:-3])
        