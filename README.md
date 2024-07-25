
## Caesar Cipher Encryption and Decryption

This Python program allows users to encrypt and decrypt text using the Caesar Cipher algorithm. The Caesar Cipher is a simple substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet.

### Features

- **Encrypt Text**: Users can input a message and a shift value to encrypt the message.
- **Decrypt Text**: Users can input an encrypted message and a shift value to decrypt the message back to its original form.
- **Flexible Shift Value**: The shift value can be positive or negative, allowing for both forward and backward shifts.

### How to Use

1. **Clone the Repository**: Clone this repository to your local machine using `git clone`.
2. **Run the Program**: Execute the Python script `caesar_cipher.py` to start the program.
3. **Input Message and Shift**: Follow the on-screen prompts to input your message and the shift value.
4. **View Results**: The program will display the encrypted or decrypted message based on your input.

### Example Usage

```python
# Example of encryption
Enter your message: hello
Enter shift value: 3
Encrypted message: khoor

# Example of decryption
Enter your encrypted message: khoor
Enter shift value: 3
Decrypted message: hello
```

### Requirements

- Python 3.x

### Code Example

Here is a basic implementation of the Caesar Cipher in Python:

```python
def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def decrypt(text, shift):
    return encrypt(text, -shift)

if __name__ == "__main__":
    choice = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ").strip().lower()
    message = input("Enter your message: ")
    shift = int(input("Enter shift value: "))

    if choice == 'encrypt':
        print("Encrypted message:", encrypt(message, shift))
    elif choice == 'decrypt':
        print("Decrypted message:", decrypt(message, shift))
    else:
        print("Invalid choice!")
