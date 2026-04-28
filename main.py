#!/usr/bin/env python3
import webbrowser
import sys
import os

def main():
    if len(sys.argv) >= 2:
        command = sys.argv[1:]
        last_word = command[-1].lower()
        last_word_length = len(last_word)
        if last_word_length == 2 and len(command) > 1:
            command_string = " ".join(command[:-1])
            webbrowser.open(f"https://translate.google.com/?sl=auto&tl={last_word}&text={command_string}&op=translate")
        else:
            command_string = " ".join(command)
            webbrowser.open(f"https://translate.google.com/?sl=auto&tl=en&text={command_string}&op=translate")
if __name__ == "__main__":
    main()