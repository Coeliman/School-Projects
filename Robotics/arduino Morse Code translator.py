from tkinter import messagebox
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
while True:
    if string[num] == "/":
        print("delay(3500); ///NEWWORD")
        #7 units
    elif string[num] == " ":
        #3 units
        print("delay(1500); ///SPACE")
    elif string[num] == ".":
        #1 unit
        print("digitalWrite(13,HIGH);")
        print("delay(500);")
        print("digitalWrite(13,LOW);")
        print("delay(500); ///SHORT")
    elif string[num] == "-":
        #3 units
        print("digitalWrite(13,HIGH);")
        print("delay(1500);")
        print("digitalWrite(13,LOW);")
        print("delay(500); ///LONG")
    elif string[num] == "A":
            messagebox.showinfo('Arduino Translator', 'Morse Code Successfully Translate')
            break
    num=num+1