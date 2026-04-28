# utrans

This is my first project based on Linux. The project is designed for translating messages using Google Translate.

## Description

utrans is a simple Python-based CLI tool for Ubuntu that instantly opens Google Translate in your browser with the provided word or message.

## Installation

1. Make sure you have Python 3 installed.
2. Clone the repository or download the files.
3. Make the script executable: `chmod +x main.py`
4. Create an alias for easy use: `alias trans='python3 /path/to/main.py'` (add this to your `~/.bashrc` or `~/.zshrc`)

> [!NOTE]
> **Update is ready!**
> Now you can write sentences without quotes! The space handling has been fixed.

> [!TIP]
> If you don't set up the alias and executable permissions, you can still run the tool with: `python3 main.py "hello world" ru`

## Usage

- To translate a word: `trans word`
- To translate a sentence: `trans Your sentence here`
- To translate to a specific language, use: `trans <text> <language_code>` 
  - Where `language_code` is the 2-letter language code as used by Google Translate (e.g., 'es' for Spanish, 'fr' for French, 'ru' for Russian)

## Examples

- `trans hello`
- `trans Hello how are you?`
- `trans Hello how are you? es` (translates to Spanish)

## Setting up Alias

To use the `trans` command easily instead of typing the full path:

1. Open your shell configuration file:
   - For bash: `nano ~/.bashrc`
   - For zsh: `nano ~/.zshrc`

2. Add this line at the end of the file (replace `/path/to/utrans/` with the actual path to your utrans folder):
   ```
   alias trans='python3 /path/to/utrans/main.py'
   ```

3. Save the file and exit the editor (Ctrl+X, then Y, then Enter in nano)

4. Reload the configuration:
   ```
   source ~/.bashrc
   ```
   or
   ```
   source ~/.zshrc
   ```

Now you can use `trans hello` directly from any terminal!

To use the `trans` command easily instead of typing the full path:

---
*Built with ❤️ and code*