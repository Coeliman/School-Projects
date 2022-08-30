from tkinter import messagebox
import os
DICT = { 'A':'.-', 'B':'-...',
    'C':'-.-.', 'D':'-..', 'E':'.',
    'F':'..-.', 'G':'--.', 'H':'....',
    'I':'..', 'J':'.---', 'K':'-.-',
    'L':'.-..', 'M':'--', 'N':'-.',
    'O':'---', 'P':'.--.', 'Q':'--.-',
    'R':'.-.', 'S':'...', 'T':'-',
    'U':'..-', 'V':'...-', 'W':'.--',
    'X':'-..-', 'Y':'-.--', 'Z':'--..',
    '1':'.----', '2':'..---', '3':'...--',
    '4':'....-', '5':'.....', '6':'-....',
    '7':'--...', '8':'---..', '9':'----.',
    '0':'-----', ', ':'--..--', '.':'.-.-.-',
    '?':'..--..', '-':'-....-',
    '(':'-.--.', ')':'-.--.-'}
def encrypt(msg):
    global cipher
    cipher = ''
    for letter in msg:
        if letter != ' ':
            cipher += DICT[letter] + ' '
        else:
            cipher += '/'
    #Space will seperate letters, / seperates words
print("Input string to encrypt")
wrd = input().upper()
encrypt(wrd)
num = 0
string = cipher
string = [*string]
string.append("A")
f = open("MorseCodeTranslate.txt", "w")
f = open("MorseCodeTranslate.txt", "a+")
f.seek(0)
f.write("///TRANSLATED INTO ARDUINO C++ BELOW\n")
while True:
    if string[num] == "/":
        f.write(f"delay(3500); ///NEWWORD\n")
        #7 units
    elif string[num] == " ":
        #3 units
        f.write("delay(1500); ///SPACE\n")
    elif string[num] == ".":
        #1 unit
        f.write("digitalWrite(13,HIGH)\n;")
        f.write("delay(500);\n")
        f.write("digitalWrite(13,LOW);\n")
        f.write("delay(500); ///SHORT\n")
    elif string[num] == "-":
        #3 units
        f.write("digitalWrite(13,HIGH);\n")
        f.write("delay(1500);\n")
        f.write("digitalWrite(13,LOW);\n")
        f.write("delay(500); ///LONG\n")
    elif string[num] == "A":
            f.write("//ENDPROGRAM\n")
            break
    num=num+1
f.close()
print('Success! The code is now located in MorseCodeTranslate.txt. This is located in the folder you currently have this python program in.')