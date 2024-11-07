from Read import *
from Write import *
from TextToMorseCode import *

import time

global MORSE_CODE_DICT
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...',
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
                    '?':'..--..', '/':'-..-.', '-':'-....-',
                    '(':'-.--.', ')':'-.--.-'}

global displayScreen
displayScreen = """ Enter an option from the following: \n\n 
                    1. Write onto an RFID chip \n
                    2. Read data from an RFID chip \n
                    3. Convert data on an RFID chip into Morse Code \n
                    4. Play data on an RFID chip in Morse Code \n\n
                    Enter 'q' to quit.\n
                    """

def main() -> None:
    while True:
        textIn = input(displayScreen)
        if not textIn == "q":
            time.sleep(0.1)
            getOption(textIn)
            continue
        break
    return


def getOption(text : str) -> None:
    if text == "1":
        writeInput()
    elif text == "2":
        read()
    elif text == "3":
        RFIDToMorseCode()
    elif text == "4":
        Play_RFIDToMorseCode()


def RFIDToMorseCode() -> tuple[str, str]:
    data = read()

    id = data[0]
    text = data[1]

    morseCode = encrypt(text)

    print(f"Original Text: {text} \n Text as Morse Code: {morseCode}\n")
    
    return (id, morseCode)

def Play_RFIDToMorseCode() -> tuple[str, str]:
    
    data = RFIDToMorseCode()
    
    timings = encryptAsTiming(data[1])

    timings.playWord()
    
    print("Word Finished.")

    id = data[0]
    morseCode = data[1]

    print(f"(WIP), {id} --- {morseCode}\n")

    return (id, morseCode)


## run the program here
main()
