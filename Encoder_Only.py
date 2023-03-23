# Yakub Mungai
def encode(password):
    # Input: "12345555"
    # Output: "45678888"
        # For each elem in Input
            # Convert elem to int and add 3 to it, then change back to string
            # (Must ensure that when we add 3 to the elem, it is still in range 0 - 9)
            # Add encoded elem to Output string
        #Return the encoded password
    enc_password = ""
    for digit in password:
        enc_digit = str(int(digit) + 3)
        single_enc_digit = str(int(enc_digit) % 10)
        enc_password += single_enc_digit
    return enc_password

#Jacob Mungai
def decode(password):
    # Input: "00009962"
    # Output: "33332295"
        # For each elem in Input
            # Convert elem to int and subtract 3, then change back to string
            # (Must ensure that when we subtract 3 to elem, it is still within range 0 - 9
            # Add encoded elem to Output string
        # Return the decoded password
    dec_password = ""
    for digit in password:
        dec_digit = str(int(digit) - 3)
        single_dec_digit = str(int(dec_digit) % 10)
        dec_password += single_dec_digit
    return dec_password


def main():
    while True:
        print("\nMenu\n-------------\n1. Encode\n2. Decode\n3. Quit")

        option = int(input("\nPlease enter an option: "))

        if option == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
        elif option == 2:
            print(f"The encoded password is {encode(password)}, and the original password is {password}.")
        elif option == 3:
            break



if __name__ == "__main__":
    main()