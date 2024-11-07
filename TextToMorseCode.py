from wordAsMorseCode import wordAsMorseCode
# Python program to implement Morse Code Translator
 
'''
VARIABLE KEY
'cipher' -> 'stores the morse translated form of the english string'
'decipher' -> 'stores the english translated form of the morse string'
'citext' -> 'stores morse code of a single character'
'i' -> 'keeps count of the spaces between morse characters'
'message' -> 'stores the string to be encoded or decoded'
'''
 
# Dictionary representing the morse code chart
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

MORSE_CODE_DICT_TIMING = {
    'A': [1, 2, 3],       # '.-' -> dot (1), dash (2), letter space (3)
    'B': [2, 1, 1, 1, 3], # '-...' -> dash (2), dot (1), dot (1), dot (1), letter space (3)
    'C': [2, 1, 2, 1, 3], # '-.-.' -> dash (2), dot (1), dash (2), dot (1), letter space (3)
    'D': [2, 1, 1, 3],    # '-..' -> dash (2), dot (1), dot (1), letter space (3)
    'E': [1, 3],          # '.' -> dot (1), letter space (3)
    'F': [1, 1, 2, 1, 3], # '..-.' -> dot (1), dot (1), dash (2), dot (1), letter space (3)
    'G': [2, 2, 1, 3],    # '--.' -> dash (2), dash (2), dot (1), letter space (3)
    'H': [1, 1, 1, 1, 3], # '....' -> dot (1), dot (1), dot (1), dot (1), letter space (3)
    'I': [1, 1, 3],       # '..' -> dot (1), dot (1), letter space (3)
    'J': [1, 2, 2, 2, 3], # '.---' -> dot (1), dash (2), dash (2), dash (2), letter space (3)
    'K': [2, 1, 2, 3],    # '-.-' -> dash (2), dot (1), dash (2), letter space (3)
    'L': [1, 2, 1, 1, 3], # '.-..' -> dot (1), dash (2), dot (1), dot (1), letter space (3)
    'M': [2, 2, 3],       # '--' -> dash (2), dash (2), letter space (3)
    'N': [2, 1, 3],       # '-.' -> dash (2), dot (1), letter space (3)
    'O': [2, 2, 2, 3],    # '---' -> dash (2), dash (2), dash (2), letter space (3)
    'P': [1, 2, 2, 1, 3], # '.--.' -> dot (1), dash (2), dash (2), dot (1), letter space (3)
    'Q': [2, 2, 1, 2, 3], # '--.-' -> dash (2), dash (2), dot (1), dash (2), letter space (3)
    'R': [1, 2, 1, 3],    # '.-.' -> dot (1), dash (2), dot (1), letter space (3)
    'S': [1, 1, 1, 3],    # '...' -> dot (1), dot (1), dot (1), letter space (3)
    'T': [2, 3],          # '-' -> dash (2), letter space (3)
    'U': [1, 1, 2, 3],    # '..-' -> dot (1), dot (1), dash (2), letter space (3)
    'V': [1, 1, 1, 2, 3], # '...-' -> dot (1), dot (1), dot (1), dash (2), letter space (3)
    'W': [1, 2, 2, 3],    # '.--' -> dot (1), dash (2), dash (2), letter space (3)
    'X': [2, 1, 1, 2, 3], # '-..-' -> dash (2), dot (1), dot (1), dash (2), letter space (3)
    'Y': [2, 1, 2, 2, 3], # '-.--' -> dash (2), dot (1), dash (2), dash (2), letter space (3)
    'Z': [2, 2, 1, 1, 3], # '--..' -> dash (2), dash (2), dot (1), dot (1), letter space (3)
    '1': [1, 2, 2, 2, 2, 3],  # '.----' -> dot (1), dash (2), dash (2), dash (2), dash (2), letter space (3)
    '2': [1, 1, 2, 2, 2, 3],  # '..---' -> dot (1), dot (1), dash (2), dash (2), dash (2), letter space (3)
    '3': [1, 1, 1, 2, 2, 3],  # '...--' -> dot (1), dot (1), dot (1), dash (2), dash (2), letter space (3)
    '4': [1, 1, 1, 1, 2, 3],  # '....-' -> dot (1), dot (1), dot (1), dot (1), dash (2), letter space (3)
    '5': [1, 1, 1, 1, 1, 3],  # '.....' -> dot (1), dot (1), dot (1), dot (1), dot (1), letter space (3)
    '6': [2, 1, 1, 1, 1, 3],  # '-....' -> dash (2), dot (1), dot (1), dot (1), dot (1), letter space (3)
    '7': [2, 2, 1, 1, 1, 3],  # '--...' -> dash (2), dash (2), dot (1), dot (1), dot (1), letter space (3)
    '8': [2, 2, 2, 1, 1, 3],  # '---..' -> dash (2), dash (2), dash (2), dot (1), dot (1), letter space (3)
    '9': [2, 2, 2, 2, 1, 3],  # '----.' -> dash (2), dash (2), dash (2), dash (2), dot (1), letter space (3)
    '0': [2, 2, 2, 2, 2, 3],  # '-----' -> dash (2), dash (2), dash (2), dash (2), dash (2), letter space (3)
    ',': [2, 2, 1, 1, 2, 2, 3], # '--..--' -> dash (2), dash (2), dot (1), dot (1), dash (2), dash (2), letter space (3)
    '.': [1, 2, 1, 2, 1, 2, 3], # '.-.-.-' -> dot (1), dash (2), dot (1), dash (2), dot (1), dash (2), letter space (3)
    '?': [1, 1, 2, 2, 1, 1, 3], # '..--..' -> dot (1), dot (1), dash (2), dash (2), dot (1), dot (1), letter space (3)
    '/': [2, 1, 1, 2, 1, 3],    # '-..-.' -> dash (2), dot (1), dot (1), dash (2), dot (1), letter space (3)
    '-': [2, 1, 1, 1, 1, 2, 3], # '-....-' -> dash (2), dot (1), dot (1), dot (1), dot (1), dash (2), letter space (3)
    '(': [2, 1, 2, 2, 1, 3],    # '-.--.' -> dash (2), dot (1), dash (2), dash (2), dot (1), letter space (3)
    ')': [2, 1, 2, 2, 1, 2, 3]  # '-.--.-' -> dash (2), dot (1), dash (2), dash (2), dot (1), dash (2), letter space (3)
}



# Function to encrypt the string
# according to the morse code chart
def encrypt(message : str) -> str:
    cipher = ''
    for letter in message.upper():
        if letter != ' ' and letter in MORSE_CODE_DICT.keys():
 
            # Looks up the dictionary and adds the
            # corresponding morse code
            # along with a space to separate
            # morse codes for different characters
            cipher += MORSE_CODE_DICT[letter] + ' '
        else:
            # 1 space indicates different characters
            # and 2 indicates different words
            cipher += ' '
 
    return cipher


def encryptAsTiming(message : str) -> str:
    cipher = wordAsMorseCode()
    for letter in message.upper():
        if letter != ' ':
            if letter in MORSE_CODE_DICT_TIMING.keys():
                cipher.addLetter(MORSE_CODE_DICT_TIMING[letter])
        else:
            cipher.addLetter([7])
    letters = cipher.letters
    tempChar = [7]
    for i in range(len(letters)):
        if letters[i] == tempChar:
            cipher.letters = letters[0:i]
            return cipher
        tempChar = letters[i]
        continue
    
    return cipher




# Function to decrypt the string
# from morse to english
def decrypt(message : str) -> str:
 
    # extra space added at the end to access the
    # last morse code
    message += ' '
 
    decipher = ''
    citext = ''
    for letter in message.upper():
 
        # checks for space
        if (letter != ' '):
 
            # counter to keep track of space
            i = 0
 
            # storing morse code of a single character
            citext += letter
 
        # in case of space
        else:
            # if i = 1 that indicates a new character
            i += 1
 
            # if i = 2 that indicates a new word
            if i == 2 :
 
                 # adding space to separate words
                decipher += ' '
            else:
 
                # accessing the keys using their values (reverse of encryption)
                decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                citext = ''
 
    return decipher


def removeBadChars(message : str) -> str:
    message = message.upper()
    keys = MORSE_CODE_DICT.keys()
    print("Removing unsupported characters from string...")
    for i in range(0, len(message)):
        if message[i] not in keys:
            message.replace(message[i], "")
            i -= 1
            print(message[i])

    print(f"done, finalized string: \n{message}")


# Hard-coded driver function to run the program
def main():
    message = "GEEKS-FOR-GEEKS"
    result = encrypt(message.upper())
    print (result)
 
    message = "--. . . -.- ... -....- ..-. --- .-. -....- --. . . -.- ... "
    result = decrypt(message)
    print (result)
 
# Executes the main function
if __name__ == '__main__':
    main()
