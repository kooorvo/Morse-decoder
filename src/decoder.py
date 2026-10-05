from morseCode import MORSE_TO_TEXT

def decode(morseInput):
    resultat = ""
    for morse in morseInput.split():
        if morse in MORSE_TO_TEXT:
            resultat += MORSE_TO_TEXT[morse]
    return resultat