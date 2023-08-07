import streamlit as st

# Permanent Variables
MORSE_CODE_DICT = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
    'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
    'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
    'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
    'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', " ": "  "
}

CHAR_LIST = [chr(i) for i in range(ord('a'), ord('z')+1)] + [str(i) for i in range(10)] + [" "]

def ask_input():
    '''Ask user for input and make string lowercase and list'''
    string = st.text_input("What is the text to translate to morse? Please use alphanumeric characters (A-Z, 0-9)").lower()
    string_list = [char for char in string]
    return string_list

def main():
    st.title("Text to Morse Code Translator")
    
    string_list = ask_input()
    
    # Verify if there are symbols in the list. If not, repeat loop for asking input.
    good_to_go = False
    while not good_to_go:
        if any(char not in CHAR_LIST for char in string_list):
            st.warning("No symbols allowed.")
            string_list = ask_input()
        else:
            good_to_go = True

    # Step 3: Verify list against dictionary
    morse_txt = " ".join([MORSE_CODE_DICT[char] for char in string_list])
    st.write(f"Translated Morse Code: {morse_txt}")


if __name__ == "__main__":
    main()
