# 🔐 Password Strength Detector

A Python command-line tool that checks whether a password is strong, and suggests a strong password if it isn't.

## Overview

This project validates user passwords against a set of common security rules and flags weak passwords — including ones that reuse the username, birthdate, or a commonly used password. If the entered password fails, it automatically generates and suggests a strong alternative.

## Features

- ✅ Enforces a minimum password length of 8 characters
- 🚫 Rejects passwords containing the username
- 🚫 Rejects passwords containing the birthdate (or birth year)
- 🚫 Blocks common/weak passwords (e.g., `password`, `123456`, `qwerty`)
- 🔠 Requires at least one uppercase letter
- 🔢 Requires at least one digit
- 🔣 Requires at least one special character
- 💡 Automatically suggests a strong, randomly generated password if the input is weak

## Tech Stack

- Python 3
- Built-in libraries: `re`, `random`, `string` (no external dependencies)

## How It Works

1. The user enters their username, birthdate, and a password.
2. `check_password_strength()` validates the password against each rule in sequence, returning the first failure reason it finds.
3. If the password is weak, `suggest_password()` randomly generates candidate passwords (10–14 characters, mixing letters, digits, and symbols) until one passes all the strength checks.
4. The user is prompted to re-enter a password until a strong one is provided.

## Installation

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd <your-repo-folder>
   ```

2. No external dependencies are required — just Python 3.

## Usage

Run the script from the command line:

```bash
python Password_Strength_Detector.py
```

You'll be prompted to enter:
1. Your username
2. Your birthdate (in `YYYYMMDD` format)
3. A password to check

The tool will tell you whether the password is strong, and if not, why — along with a suggested strong password.

## Example

```
Enter your username: john_doe
Enter your birthdate (YYYYMMDD): 19950214
Enter your password: password123
Password is too common.
Suggested strong password: xQ7$mKp2LtR!
Enter your password: xQ7$mKp2LtR!
Password is strong!
```

## Project Structure

```
.
├── Password_Strength_Detector.py   # Main script
└── README.md                        # Project documentation
```

## Future Improvements

- Add a graphical or web-based interface (e.g., with Tkinter or Streamlit)
- Add a password strength score/meter instead of pass/fail
- Check passwords against a larger breached-password database
- Allow configurable rules (e.g., adjustable minimum length)
- Add unit tests for the validation logic

## License

This project is open source and available for personal or educational use.
