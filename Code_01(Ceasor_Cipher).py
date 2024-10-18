import MyModule

print(MyModule.logo_encoding)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z']
action_YN = "Y"

def ceasar_cipher(msg, shift, encode_or_decode):
    new_letter = []
    for letter_no in range(len(msg)):
        if msg[letter_no].isalpha():
            for alpha_no in range(len(alphabet)):
                if alphabet[alpha_no] == msg[letter_no]:
                    if encode_or_decode == "encode":
                        position = alpha_no + shift
                    else:
                        position = alpha_no - shift
                    if position > 25:
                        new_letter += alphabet[position % 26]
                    else:
                        new_letter += alphabet[position]
        else:
            new_letter.append(msg[letter_no])
    print(f"Here's the {encode_or_decode}ed result: {''.join(new_letter)}")


while action_YN == "Y":
    user_action = input("Type 'ENCODE' to encrypt and 'DECODE' to decrypt:\n")
    if user_action.lower() == "encode" or user_action.lower() == "decode":
        user_msg = input("Type your message:\n").lower()
        shift_no = int(input("Type the shift number:\n"))
        ceasar_cipher(user_msg, shift_no, user_action)
    else:
        print("Please check the spelling!!!")
    action_YN = input("Type 'YES' if you want to go again. Otherwise type 'NO'.\n")
    if action_YN.lower() == "yes":
        action_YN = "Y"
    else:
        action_YN = "N"
