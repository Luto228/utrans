# utrans

This is my first project based on Linux. The project is designed for translating messages using Google Translate.

## Description

utrans is a simple Python-based CLI tool for Ubuntu that instantly opens Google Translate in your browser with the provided word or message.

## Installation

1. Make sure you have Python 3 installed.
2. Clone the repository or download the files.
3. Run `python3 main.py <word or "sentence">`

> [!WARNING]
> **Space bug**
> For now, if you want to translate individual words, it's all good. However, if you are translating a sentence, THEN it is MANDATORY to enclose it in quotes, it will be fix.

## Usage

- To translate a word: `trans word`
- To translate a sentence: `trans "Your sentence here"`
- To translate to a specific language, use: `trans <word or "sentence"> <language>` (where language is the first 2 letters as used in Google Translate, e.g., 'es' for Spanish, 'fr' for French)

## Examples

- `trans hello`
- `trans "Hello, how are you?"`

---
*Built with ❤️ and code*