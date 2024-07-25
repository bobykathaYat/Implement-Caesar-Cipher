def caesar_cipher(message, shift):
    result = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                result += chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                result += chr((ord(char) - 97 + shift) % 26 + 97)
        else:
            result += char
    return result

def main():
    while True:
        print("Caesar Cipher Encryption and Decryption")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted = caesar_cipher(message, shift)
            print("Encrypted message:", encrypted)
        elif choice == '2':
            message = input("Enter the message to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted = caesar_cipher(message, -shift)
            print("Decrypted message:", decrypted)
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()