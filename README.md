# utrans

This is my first project based on Linux. The project is designed for translating messages using Google Translate.

## Description

utrans is a simple Python-based CLI tool for Ubuntu that instantly opens Google Translate in your browser with the provided word or message.

## Installation

1. Make sure you have Python 3 installed.
2. Clone the repository or download the files.
3. Run `python3 main.py <word or sentence>`

> [!NOTE]
> **Update is ready!**
> Now you can write sentences without quotes! The space handling has been fixed.

## Usage

- To translate a word: `trans word`
- To translate a sentence: `trans Your sentence here`
- To translate to a specific language, use: `trans <text> <language_code>` 
  - Where `language_code` is the 2-letter language code as used by Google Translate (e.g., 'es' for Spanish, 'fr' for French, 'ru' for Russian)

## Examples

- `trans hello`
- `trans Hello how are you?`
- `trans Hello how are you? es` (translates to Spanish)

---
*Built with ❤️ and code*