
import time
import keyboard

# Complete Morse code map including numbers and special digits/punctuation
MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', 
    
    # Numbers
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', 
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    
    # Special Digits and Punctuation
    '.': '.-.-.-',   # Period
    ',': '--..--',   # Comma
    '?': '..--..',   # Question Mark
    "'": '.----.',   # Apostrophe
    '!': '-.-.--',   # Exclamation Point
    '/': '-..-.',    # Slash / Forward Slash
    '(': '-.--.',    # Open Parenthesis
    ')': '-.--.-',   # Close Parenthesis
    '&': '.-...',    # Ampersand
    ':': '---...',   # Colon
    ';': '-.-.-.',   # Semicolon
    '=': '-...-',    # Equals sign
    '+': '.-.-.',    # Plus sign
    '-': '-....-',   # Hyphen / Minus
    '_': '..--.-',   # Underscore
    '"': '.-..-.',   # Quotation Mark
    '$': '...-..-',  # Dollar Sign
    '@': '.--.-.'    # At Sign
}

def execute_morse_wpm(text, wpm, target_key):
    # Calculate exact timings based on WPM
    unit_duration = 1.2 / wpm
    
    dot_duration = unit_duration
    dash_duration = unit_duration * 3
    symbol_gap = unit_duration
    letter_gap = unit_duration * 3
    word_gap = unit_duration * 7

    print(f"\n[Speed Set: {wpm} WPM | Target Key: '{target_key}']")
    print("-> Starting in 3 seconds... Quick! Click inside your game/app! <-")
    time.sleep(3)
    
    for char in text.upper():
        if keyboard.is_pressed('esc'): # Emergency stop button
            print("\nStopped by user.")
            break
            
        if char == ' ':
            time.sleep(word_gap - letter_gap) 
            continue
            
        if char in MORSE_DICT:
            morse_code = MORSE_DICT[char]
            
            for symbol in morse_code:
                # Check emergency stop inside the loop
                if keyboard.is_pressed('esc'):
                    break

                if symbol == '.':
                    keyboard.press(target_key)
                    time.sleep(dot_duration)
                    keyboard.release(target_key)
                elif symbol == '-':
                    keyboard.press(target_key)
                    time.sleep(dash_duration)
                    keyboard.release(target_key)
                
                time.sleep(symbol_gap)
                
            time.sleep(letter_gap - symbol_gap)
        else:
            # Skip completely unknown characters without freezing
            print(f"Skipping unsupported character: {char}")

if __name__ == "__main__":
    user_text = input("1. Enter the message you want to send: ")
    user_wpm = float(input("2. Enter the speed in WPM (e.g., 5, 15, 20): "))
    
    print("\n--- Key Names Guide ---")
    print("For letters or numbers, just type them (e.g., x, 1)")
    print("For special keys, type the name (e.g., space, enter, shift, ctrl)")
    user_key = input("3. Enter the key you want the bot to press: ").lower().strip()
    
    execute_morse_wpm(user_text, user_wpm, user_key)
    print("\n[Finished typing!]")
