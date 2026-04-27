#!/usr/bin/env python3
import webbrowser
import sys
import os

def main():
    if len(sys.argv) == 2:
        command = sys.argv[1]

        try:
            webbrowser.open(f"https://translate.google.com/?sl=auto&tl=en&text={command}&op=translate")
        except webbrowser.Error as e:
            raise ValueError(f'Failed to open web browser: {e}')
    elif len(sys.argv) == 3:
        command = sys.argv[1]
        language = sys.argv[2]

        try:
            webbrowser.open(f"https://translate.google.com/?sl=auto&tl={language}&text={command}&op=translate")
        except webbrowser.Error as e:
            raise ValueError(f'Failed to open web browser: {e}')
    else:
        raise ValueError('Please write trans [text] or trans [text] [language]')
    
if __name__ == "__main__":
    main()