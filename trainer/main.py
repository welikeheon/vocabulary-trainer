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
   

def insert():
    while True:
        french = raw_input("French word: ")
        
        if french == "#":
            return 
        
        english = raw_input("English word: ")
        
        if english == "#":
            return 
        
        entries.append(Entry(french, english))
        backup_wordpairs()
        
def query():
    total = 0
    right = 0
    wrong = 0
    
    while True:
        i = random.randint(0, len(entries) - 1)
        french = raw_input("French translation of " + entries[i].english + ": ")
        
        # TODO: Add a statistics which is displayed before leaving (x of y correct. Equal z percent).
        if french == "#":
            percentage = (right  * 100) / total
            print("You answered " + str(right) + " question out of " + str(total) + " correct.")
            print("Percentage: " + str(percentage) + " %")
            return 
        
        total = total + 1
        
        if french.strip() == entries[i].french.strip():
            print("Correct.")
            right = right + 1
        else:
            print("Wrong!")
            wrong = wrong + 1

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
        insert()
    elif command == "test":
        query()
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
    