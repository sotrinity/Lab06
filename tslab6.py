# main and encode function are by Trinity So

def menu():
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit')

def encode(password):
    new_password = ''
    for digit in password:
        new_password += str(int(digit) + 3)
    return new_password

def decode(password):
    original_password = ''
    for digit in password:
        original_password += str(int(digit) - 3)
    return original_password

if __name__ == '__main__':
    while True:
        menu()
        print('\nPlease enter an option:', end=' ')
        option = int(input())

        if option == 1:
            print('Please enter your password to encode:', end=' ')
            user_password = input()
            encoded_password = encode(user_password)
            print('Your password has been encoded and stored!')

        if option == 2:
            decoded_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')

        if option == 3:
            exit()

        print()

