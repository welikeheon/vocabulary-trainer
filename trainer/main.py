import random
import os
import sys

FILE_PATH = "./words.txt"

class Entry:
    def __init__(self, french, english):
        self.french = french
        self.english = english
        
entries = []

if os.path.isfile(FILE_PATH):
    words = open(FILE_PATH, "r")
    
    for line in words:
        words = line.split(",")
        entries.append(Entry(words[0].strip(), words[1].strip()))
   

def eingabe():
    while True:
        french = raw_input("French word: ")
        
        if french == "#":
            return 
        
        english = raw_input("English word: ")
        
        if english == "#":
            return 
        
        entries.append(Entry(french, english))
        backup_wordpairs()
        
def abfrage():
    while True:
        i = random.randint(0, len(entries) - 1)
        french = raw_input("French translation of " + entries[i].english + ": ")
        
        # TODO: Add a statistics which is displayed before leaving (x of y correct. Equal z percent).
        if french == "#":
            return 
        
        print(french.strip())
        print(entries[i].french.strip())
        
        if french.strip() == entries[i].french.strip():
            print("Correct.")
        else:
            print("Wrong!")

def printall():    
    if len(entries) == 0:
        print("No words stored.")
        return
    
    for i in range(len(entries)):
        print(entries[i].french + " : " + entries[i].english)

def backup_wordpairs():
    woerter = open(FILE_PATH, 'w')
    
    for wort_paar in entries:
        woerter.write(wort_paar.french + "," + wort_paar.english + "\n")
    
    woerter.close()
    
def reset_list():
    global entries
    
    entries = []
    
    if os.path.isfile(FILE_PATH):
        os.remove(FILE_PATH)
    
while True:
    command = raw_input("Please enter a command: ")
    
    if command == "add":
        eingabe()
    elif command == "test":
        abfrage()
    elif command == "list":
        printall()
    elif command == "end":
        break
    elif command == "reset":
        reset_list()
    else:
        print("No known command.")
    
print(" ------- Vocabulary becomes terminated. ----------  ")
sys.exit()
    