# This is Yuzhang Liu's main.py file

def encode(encode_string):
    decode_string = ''
    for char in encode_string:
        char = int(char) + 3
        decode_string += str(char)
    return decode_string


def menu():
    print("Menu")
    print("-------------")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    print()
    return

if __name__ == '__main__':
    menu()
    choice = 1
    while choice != 3:
        choice = int(input("Please enter an option: "))
        if choice == 1:
            encode_string = input("Please enter your password to encode: ")
            decode_string = encode(encode_string)
            print("Your password has been encoded and stored!")
            print()

