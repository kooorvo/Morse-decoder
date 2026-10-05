from morseCode import MORSE_CODE

def encode(morseInput):
    resultat = ""
    for lettre in morseInput.upper():
        if lettre in MORSE_CODE:
            resultat += MORSE_CODE[lettre] + " "
    return resultat