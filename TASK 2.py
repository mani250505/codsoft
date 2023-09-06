import random
import string


def generate_password(length, complexity):
    characters = ''

    if 'letters' in complexity:
        characters += string.ascii_letters
    if 'digits' in complexity:
        characters += string.digits
    if 'special' in complexity:
        characters += string.punctuation

    if not characters:
        return "Complexity level not selected"

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            complexity = input(
                "Choose complexity (letters, digits, special, or a combination, e.g., 'letters digits special'): ").lower()

            password = generate_password(length, complexity)

            if password:
                print("Generated Password:", password)

            another = input("Generate another password? (yes/no): ").lower()
            if another != "yes":
                break
        except ValueError:
            print("Invalid input. Please enter a valid length.")

    print("Thank you for using the Password Generator!")


if __name__ == "__main__":
    main()
