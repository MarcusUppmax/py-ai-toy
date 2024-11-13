#!/bin/env python

def beskriv(text, model):
   print("nu kör vi ai")
   
   with model.chat_session():
     resultat = model.generate("Jo tjena",max_tokens=512)
     return resultat

   return "Hoppsan, inget ai"

import sys
from gpt4all import GPT4All

filnamn = sys.argv[1]
f = open(filnamn, "r")
beskrivning = f.read()

model = GPT4All("Meta-Llama-3-8B-Instruct.Q4_0.gguf")

resultat = beskriv(beskrivning, model)

print(resultat)