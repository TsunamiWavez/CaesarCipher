# Caesar Cipher Encryption and Decryption

## Description
This is a simple Python program that allows users to encrypt or decrypt messages using the **Caesar Cipher** method. The Caesar Cipher is a substitution cipher where each letter in the plaintext is shifted a fixed number of places down or up the alphabet.

## Features
- Determine the number of characters to shift forward/backward
- Encrypt messages by shifting letters forward in the alphabet.
- Decrypt messages by shifting letters backward in the alphabet.
- Retains special characters, numbers, and spaces unchanged.
- User-friendly input and output interface.

## How to Use
1. Run the program.
2. Choose an option:
   - Enter `1` to encrypt a message.
   - Enter `2` to decrypt a message.
   - Enter `3` to exit the program.
3. Input your message.
4. Determine the number of characters to shift (from 1 to 25)
5. The program will output the encrypted or decrypted message.
6. Choose whether to exit or continue.

## Example Usage
```
---Encrypt or Decrypt your message using Caesar Cipher---

Options of your input:
	1 - Encrypt message
	2 - Decrypt message
	3 - Exit the program

Please use only these options (from 1 to 3), 
otherwise the program will return an error!

What do you want to do?: 1

Enter your secret message: Hello, World!

How many characters should be shifted forward/backward? (1-25): 7

Here is your encrypted message:
Olssv, Dvysk!

What do you want to do now?: 2

Enter your encrypted message: Olssv, Dvysk!

How many characters should be shifted forward/backward? (1-25): 7

Here is your decrypted message:
Hello, World!

What do you want to do now?: 3

The end of the program...
```

## Requirements
- Python 3.x

## License
This project is open-source and available under the MIT License.

