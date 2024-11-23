import random
import string

def generate_password(length=8, include_letters=True, include_digits=True, include_special_chars=True):
    """Generate a random password based on user preferences."""
    if length < 1:
        return "Password length must be at least 1."

    # Create a pool of characters based on user preferences
    char_pool = ""
    if include_letters:
        char_pool += string.ascii_letters  # Includes both uppercase and lowercase letters
    if include_digits:
        char_pool += string.digits         # Includes digits 0-9
    if include_special_chars:
        char_pool += string.punctuation    # Includes special characters

    if not char_pool:
        return "No character types selected. Please include letters, digits, or special characters."

    # Generate the password
    password = ''.join(random.choice(char_pool) for _ in range(length))
    return password

def main():
    """Main function to interact with the user."""
    print("Password Generator")
    try:
        length = int(input("Enter the desired password length (minimum 1): "))
        include_letters = input("Include letters? (yes/no): ").strip().lower() == "yes"
        include_digits = input("Include digits? (yes/no): ").strip().lower() == "yes"
        include_special_chars = input("Include special characters? (yes/no): ").strip().lower() == "yes"

        password = generate_password(length, include_letters, include_digits, include_special_chars)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Invalid input! Please enter numeric values for length.")

if __name__ == "__main__":
    main()
