import random
import os.path
import sys

FILE_PATH = "./words.txt"

class Entry:
    def __init__(self, deutsch, englisch):
        self.deutsch = deutsch
        self.englisch = englisch
        
eintraege = []

if os.path.isfile(FILE_PATH):
    words = open(FILE_PATH, "r")
    
    for line in words:
        words = line.split(",")
        eintraege.append(Entry(words[0].strip(), words[1].strip()))
   

def eingabe():
    while True:
        deutsch = raw_input("Deutsches Wort: ")
        
        if deutsch == "#":
            return 
        
        englisch = raw_input("Englisches Wort: ")
        
        if englisch == "#":
            return 
        
        eintraege.append(Entry(deutsch, englisch))
        backup_wordpairs()
        
def abfrage():
    while True:
        i = random.randint(0, len(eintraege) - 1)
        englisch = raw_input("Englische Uebersetzung von " + eintraege[i].deutsch + ": ")
        
        if englisch == "#":
            return 
      
        if englisch.strip() == eintraege[i].englisch.strip():
            print("Korrekt!")
        else:
            print("Falsch.")

def printall():    
    for i in range(len(eintraege)):
        print(eintraege[i].deutsch + " : " + eintraege[i].englisch)

def backup_wordpairs():
    woerter = open(FILE_PATH, 'w')
    
    for wort_paar in eintraege:
        woerter.write(wort_paar.deutsch + "," + wort_paar.englisch + "\n")
    
    woerter.close()

while True:
    befehl = raw_input("Befehl: ")
    
    if befehl == "eingabe":
        eingabe()
    elif befehl == "test":
        abfrage()
    elif befehl == "ende":
        break
    elif befehl == "liste":
        printall()
    else:
        print("Keine bekannte Ausgabe.")
    
print(" ------- Vocabulary becomes terminated. ----------  ")
sys.exit()
    