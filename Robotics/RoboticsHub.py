import arduinoMorseCodetranslator
print("Choose what you wish to continue to.")
print("A. Text to Arduino C++ Morse Code")
user_input = input().upper()
if user_input == "A":
    arduinoMorseCodetranslator.MORSE()
else: 
    print("Invalid input, quitting program")
#THIS IS A TEST