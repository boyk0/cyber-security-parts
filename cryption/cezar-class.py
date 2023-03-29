from spellchecker import SpellChecker


class Cezar:
    min_chr = 0
    max_chr = 0x110000

    def __init__(self):
        self.operations = {
            'cryption': self.cryption,
            'encryption': self.encryption,
            'brut_force': self.brut_force
        }
        self.format_print = {
            'cryption': lambda string: 'Crypt string is {}'.format(string),
            'encryption': lambda string: 'Encrypted string is {}'.format(string),
            'brut_force': lambda string: 'Brut forced strings are {}'.format(string)
        }
        self.spell = SpellChecker()

    def cryption(self, string: str = '', step: int = 3):
        crypto_string = ''
        for char in string:
            crypto_string += chr(self.get_char_number(char, step))
        return crypto_string

    def get_char_number(self, char: str = '', step: int = 3):
        n = ord(char)
        if n + step < self.min_chr or n + step > self.max_chr:
            return abs(self.max_chr - abs(n + step))
        return n + step

    def encryption(self, string: str = '', step: int = 3):
        encrypted_string = ''
        for char in string:
            encrypted_string += chr(self.get_char_number(char, -step))
        return encrypted_string

    def brut_force(self, string: str = '', step: int = 0):
        encrypted_strings = []
        for i in range(-74, 74):
            encrypted_string = ''
            for char in string:
                encrypted_string += chr(self.get_char_number(char, -i))
            if ' ' in encrypted_string or self.is_word_exists(encrypted_string):
                encrypted_strings.append(encrypted_string)
        return encrypted_strings

    def is_word_exists(self, string: str = None):
        if string:
            if string == self.spell.correction(string):
                return True
            words = string.split(' ')
            for word in words:
                if word == self.spell.correction(word):
                    return True
        return False


cezar = Cezar()

operation_type = input(
    f'Input operation type or press Enter for cryption by default\nOperation types: {cezar.operations.keys()}\n')
operation_type = operation_type if operation_type in cezar.operations else 'cryption'

step = 3
if operation_type != 'brut_force':
    try:
        step = int(input('Input step or press Enter for set 3 by default\n'))
    except Exception:
        pass

string = input(f'Input string for {operation_type}\n')

print(cezar.format_print[operation_type](cezar.operations[operation_type](string, step)))
