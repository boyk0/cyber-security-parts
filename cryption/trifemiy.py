class Trifemiy:
    languages = {
        'EN': 'EN',
        'UA': 'UA',
    }

    alphabets = {
        languages['EN']: {
            'small': 'abcdefghijklmnopqrstuvwxyz',
            'capital': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
            'lettersCount': 26,
        },
        languages['UA']: {
            'small': 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя',
            'capital': 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ',
            'lettersCount': 33,
        },
    }

    def __init__(self):
        self.operations = {
            'cryption': self.cryption,
            'encryption': self.encryption
        }

    def cryption(self, string = '', k = 3, langauge = languages['EN']):
        m = 0
        crypted_string = ''
        while m != len(string):
            if string[m] in self.alphabets[langauge]['small']:
                idx = self.alphabets[langauge]['small'].find(string[m])
                l = (m + k + idx) % self.alphabets[langauge]['lettersCount']
                crypted_string += self.alphabets[langauge]['small'][l]
            elif string[m] in self.alphabets[langauge]['capital']:
                idx = self.alphabets[langauge]['capital'].find(string[m])
                l = (m + k + idx) % self.alphabets[langauge]['lettersCount']
                crypted_string += self.alphabets[langauge]['capital'][l]
            else:
                crypted_string += string[m]
            m += 1

        return crypted_string

    def encryption(self, string = '', k = 3, langauge = languages['EN']):
        m = 0
        encrypted_string = ''
        while m != len(string):
            if string[m] in self.alphabets[langauge]['small']:
                l = self.alphabets[langauge]['small'].find(string[m])
                encrypted_string += self.alphabets[langauge]['small'][
                    (l - (m + k)) % self.alphabets[langauge]['lettersCount']]
            elif string[m] in self.alphabets[langauge]['capital']:
                l = self.alphabets[langauge]['capital'].find(string[m])
                encrypted_string += self.alphabets[langauge]['capital'][
                    (l - (m + k)) % self.alphabets[langauge]['lettersCount']]
            else:
                encrypted_string += string[m]
            m += 1

        return encrypted_string


trifemiy = Trifemiy()

print(trifemiy.cryption('Hi everyone'))
print(trifemiy.encryption('Km kcmaizzr'))
