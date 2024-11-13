#!/bin/env python

def beskriv(text):
   print("nu kör vi ai")
   print(text)
   resultat = "klart"
   return resultat
import sys
filnamn = sys.argv[1]
f = open(filnamn, "r")
beskrivning = f.read()

resultat = beskriv(beskrivning)

print(resultat)