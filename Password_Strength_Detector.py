import re
import random
import string

common_passwords = {
    "password", "123456", "123456789", "qwerty", "abc123", "letmein", 
    "111111", "123123", "password1", "admin", "welcome", "monkey"
}

def check_password_strength(password, username, birthdate):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    

    if username.lower() in password.lower():
        return False, "Password should not contain your username."

    if birthdate in password or birthdate[-4:] in password:
        return False, "Password should not contain your birth date or birth year."

    if password.lower() in common_passwords:
        return False, "Password is too common."

    if not re.search(r'[A-Z]', password):
        return False, "Password must contain at least one uppercase letter."

    if not re.search(r'\d', password):
        return False, "Password must contain at least one digit."

    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return False, "Password must contain at least one special character."

    return True, "Password is strong!"

def suggest_password(username, birthdate):
    while True:
        suggestion = ''.join(random.choices(
            string.ascii_letters + string.digits + "!@#$%^&*",
            k=random.randint(10, 14)
        ))
        valid, _ = check_password_strength(suggestion, username, birthdate)
        if valid:
            return suggestion

def main():
    username = input("Enter your username: ").strip()
    birthdate = input("Enter your birthdate (YYYYMMDD): ").strip()

    while True:
        password = input("Enter your password: ").strip()
        valid, message = check_password_strength(password, username, birthdate)
        print(message)
        if valid:
            break
        else:
            suggestion = suggest_password(username, birthdate)
            print(f"Suggested strong password: {suggestion}")

if __name__ == "__main__":
    main()
