def cryption(string = '', step = 3):
    crypto_string = ''
    for char in string:
        crypto_string += chr(ord(char) + step)
    return crypto_string


def encryption(string = '', step = 3):
    encrypted_string = ''
    for char in string:
        encrypted_string += chr(ord(char) - step)
    return encrypted_string


operations = {
    'cryption': cryption,
    'encryption': encryption,
}

operation_type = input(
    f'Input operation type or press Enter for cryption by default\nOperation types: {operations.keys()}\n')
operation_type = operation_type if operation_type in operations else 'cryption'

step = input('Input step or press Enter for set 3 by default\n')
step = int(step) if step != '' else 3

string = input(f'Input string for {operation_type}\n')

print(
    f'{"Crypt" if operation_type == "cryption" else "Encrypted"} string is {operations[operation_type](string, step)}')
