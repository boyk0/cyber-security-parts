languages = {
    'EN': 'EN',
    'UA': 'UA'
}

alphabet = {
    languages['EN']: {
        'small': 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz',
        'capital': 'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ',
        'letter_count': 26,
    },
    languages['UA']: {
        'small': 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюяабвгґдеєжзиіїйклмнопрстуфхцчшщьюя',
        'capital': 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯАБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ',
        'letter_count': 33,
    },
}

def cryption(string = '', step = 3, language = 'EN'):
    crypto_string = ''
    for char in string:
        if char in alphabet[language]['small']:
            idx = alphabet[language]['small'].find(char)
            crypto_string += alphabet[language]['small'][idx + step]
            continue
        elif char in alphabet[language]['capital']:
            idx = alphabet[language]['capital'].find(char)
            crypto_string += alphabet[language]['capital'][idx + step]
            continue
        crypto_string += char
    return crypto_string

def encryption(string = '', step = 3, language = 'EN'):
    encrypted_string = ''
    for char in string:
        if char in alphabet[language]['small']:
            idx = alphabet[language]['small'].find(char)
            encrypted_string += alphabet[language]['small'][idx - step]
            continue
        elif char in alphabet[language]['capital']:
            idx = alphabet[language]['capital'].find(char)
            encrypted_string += alphabet[language]['capital'][idx - step]
            continue
        encrypted_string += char
    return encrypted_string

operations = {
    'cryption': cryption,
    'encryption': encryption,
}

language = input(f'Input languages or press Enter for EN by default\nlanguages: {languages.keys()}\n')
language = language if language in languages else 'EN'

operation_type = input(f'Input operation type or press Enter for cryption by default\nOperation types: {operations.keys()}\n')
operation_type = operation_type if operation_type in operations else 'cryption'

step = input('Input step or press Enter for set 3 by default\n')
step = int(step) if step != '' else 3

string = input(f'Input string for {operation_type}\n')

print(f'{"Crypt" if operation_type == "cryption" else "Encrypted"} string is {operations[operation_type](string, step, language)}')