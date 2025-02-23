# ---Encrypt or Decrypt your message using Caesar Cipher---

alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lower = alphabet_upper.lower()
special_chars = "!@#$%^&*()-_=+\\|[]{};:/?.>, "
numbers = "0123456789"

# Ask user what he wants to do
print("---Encrypt or Decrypt your message using Caesar Cipher---"
      "\n"
      "\nOptions of your input:"
      "\n\t1 - Encrypt message"
      "\n\t2 - Decrypt message"
      "\n\t3 - Exit the program"
      "\n\nPlease use only these options (from 1 to 3), "
      "\notherwise the program will return an error!")
user_choice = input("\nWhat do you want?: ")

program_active = True

while program_active:
    # Encrypting of user's message using Caesar Cipher
    if user_choice == "1":
        message = input("\nEnter your secret message: ")

        encrypted_message = ""
        index = 0
        new_index = 0

        for letter in message:
            # Skip special characters and numbers
            if letter in numbers or letter in special_chars:
                encrypted_message += letter

            # Encrypting lowercase letters
            if letter in alphabet_lower:
                index = alphabet_lower.index(letter)
                new_index = (index + 3) % len(alphabet_lower)
                encrypted_message += alphabet_lower[new_index]
            # Encrypting uppercase letters
            if letter in alphabet_upper:
                index = alphabet_upper.index(letter)
                new_index = (index + 3) % len(alphabet_upper)
                encrypted_message += alphabet_upper[new_index]

        print("\nHere is your encrypted message:")
        print(encrypted_message)

        user_choice = input("\nWhat do you want now?: ")

    # Decrypting of user's message using Caesar Cipher
    elif user_choice == "2":

        message = input("\nEnter your encrypted message: ")

        decrypted_message = ""
        index = 0
        new_index = 0

        for letter in message:
            # Skip special characters and numbers
            if letter in numbers or letter in special_chars:
                decrypted_message += letter

            # Encrypting lowercase letters
            if letter in alphabet_lower:
                index = alphabet_lower.index(letter)
                new_index = (index - 3) % len(alphabet_lower)
                decrypted_message += alphabet_lower[new_index]
            # Encrypting uppercase letters
            if letter in alphabet_upper:
                index = alphabet_upper.index(letter)
                new_index = (index - 3) % len(alphabet_upper)
                decrypted_message += alphabet_upper[new_index]

        print("\nHere is your decrypted message:")
        print(decrypted_message)

        user_choice = input("\nWhat do you want now?: ")

    # Exit the program
    elif user_choice == "3":
        print("\nThe end of the program...")
        program_active = False
        break
    # Print the error-message if the input is invalid
    else:
        print("\nThat was an error! Please enter a valid input.")
        user_choice = input("\nWhat do you want?: ")
