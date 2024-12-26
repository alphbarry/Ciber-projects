import string
import secrets

def get_configuration():
    """Prompt and validate the settings for password generation."""
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            raise ValueError("The length must be a positive number.")

        include_letters = input("Include letters? (y/n): ").strip().lower() == 'y'
        include_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
        include_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

        characters = ""
        if include_letters:
            characters += string.ascii_letters
        if include_numbers:
            characters += string.digits
        if include_symbols:
            characters += string.punctuation

        if not characters:
            raise ValueError("You must select at least one type of character.")

        return length, characters
    except ValueError as e:
        print(f"Error: {e}")
        exit()

def generate_password(length, characters):
    """Generate a secure password."""
    return ''.join(secrets.choice(characters) for _ in range(length))

def main():
    """Main function to run the program."""
    try:
        length, characters = get_configuration()
        password = generate_password(length, characters)
        print(f"The generated password is: {password}")

        save = input("Would you like to save the password to a file? (y/n): ").strip().lower()
        if save == 'y':
            with open("password.txt", "w") as file:
                file.write(password)
            print("Password saved to 'password.txt'")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()

