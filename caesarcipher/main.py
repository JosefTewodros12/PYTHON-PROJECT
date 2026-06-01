import math
from caesarcipher_art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',  ' ', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=',
            '[', ']', '{', '}', '\\', '|', ';', ':', "'", '"', ',', '<', '.', '>',
            '/', '?', '`', '~']


def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    display = []
    last_digit = text[-1::]

    if (direction == 'decode'):
        shift_amount *= -1
    for char in start_text:
        if char not in alphabet:
            bullet = "•" * (len(start_text) - len(last_digit))
            display = bullet + last_digit
            print(" ".join(display))
            break
        else:
            position = alphabet.index(char)
            new_position = position + shift_amount
            new_letter = alphabet[new_position]
            end_text += new_letter
    print(f"Here's the {cipher_direction} result: {end_text}")


print(logo)
end_of_encrypt = True

while end_of_encrypt:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type you message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    shift = shift % 26

    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    message = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if (message == 'yes'):
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    else:
        print('Goodbye')
        end_of_encrypt = False


# def encrypt(plain_text, shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text is {cipher_text}")


# def decrypt(plain_text, shif_amount):
#     decrypt_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position - shif_amount
#         new_letter = alphabet[new_position]
#         decrypt_text += new_letter
#     print(f"The decoded text is {decrypt_text}")


# if direction == 'encode':
#     encrypt(plain_text=text, shift_amount=shift)
# elif direction == 'decode':
#     decrypt(plain_text=text, shif_amount=shift)
