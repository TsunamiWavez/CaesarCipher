# ---Encrypt or Decrypt your message using Caesar Cipher---

alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
alphabet_lower = alphabet_upper.lower()
special_chars = "!@#$%^&*()-_=+\\|[]{};:/?.>, "
numbers = "0123456789"
ignore_characters = special_chars + numbers


# Determine the number of characters to shift
def num_of_characters_to_shift():
    while True:
        try:
            user_choice = int(input("\nHow many characters should be "
                                    "shifted forward/backward? (1-25) "))
            break
        except ValueError:
            print("\nThat was an error. Please enter only numbers, not words!")
            continue

    return user_choice


# Message encrypting
def encrypt(input_message, num):
    encrypted_message = ""

    for letter in input_message:
        # Skip special characters and numbers
        if letter in ignore_characters:
            encrypted_message += letter

        # Encrypting lowercase letters
        if letter in alphabet_lower:
            index = alphabet_lower.index(letter)
            new_index = (index + num) % len(alphabet_lower)
            encrypted_message += alphabet_lower[new_index]
        # Encrypting uppercase letters
        if letter in alphabet_upper:
            index = alphabet_upper.index(letter)
            new_index = (index + num) % len(alphabet_upper)
            encrypted_message += alphabet_upper[new_index]

    print("\nHere is your encrypted message:")
    print(encrypted_message)


# Message decrypting
def decrypt(input_message, num):
    decrypted_message = ""

    for letter in input_message:
        # Skip special characters and numbers
        if letter in ignore_characters:
            decrypted_message += letter

        # Encrypting lowercase letters
        if letter in alphabet_lower:
            index = alphabet_lower.index(letter)
            new_index = (index - num) % len(alphabet_lower)
            decrypted_message += alphabet_lower[new_index]
        # Encrypting uppercase letters
        if letter in alphabet_upper:
            index = alphabet_upper.index(letter)
            new_index = (index - num) % len(alphabet_upper)
            decrypted_message += alphabet_upper[new_index]

    print("\nHere is your decrypted message:")
    print(decrypted_message)


# Ask user what he wants to do
print("---Encrypt or Decrypt your message using Caesar Cipher---"
      "\n"
      "\nOptions of your input:"
      "\n\t1 - Encrypt message"
      "\n\t2 - Decrypt message"
      "\n\t3 - Exit the program"
      "\n\nPlease use only these options (from 1 to 3), "
      "\notherwise the program will return an error!")
user_choice = input("\nWhat do you want to do?: ")

program_active = True

while program_active:
    # Encrypting of user's message using Caesar Cipher
    if user_choice == "1":
        message = input("\nEnter your secret message: ")

        num = num_of_characters_to_shift()

        encrypt(message, num)

        user_choice = input("\nWhat do you want to do now?: ")

    # Decrypting of user's message using Caesar Cipher
    elif user_choice == "2":

        message = input("\nEnter your encrypted message: ")

        num = num_of_characters_to_shift()

        decrypt(message, num)

        user_choice = input("\nWhat do you want to do now?: ")

    # Exit the program
    elif user_choice == "3":
        print("\nThe end of the program...")
        program_active = False
        break
    # Print the error-message if the input is invalid
    else:
        print("\nThat was an error! Please enter a valid input.")
        user_choice = input("\nWhat do you want to do?: ")
