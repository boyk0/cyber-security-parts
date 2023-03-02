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
        cryptedString = ''
        while m != len(string):
            if string[m] in self.alphabets[langauge]['small']:
                idx = self.alphabets[langauge]['small'].find(string[m])
                l = (m + k + idx) % self.alphabets[langauge]['lettersCount']
                cryptedString += self.alphabets[langauge]['small'][l]
            elif string[m] in self.alphabets[langauge]['capital']:
                idx = self.alphabets[langauge]['capital'].find(string[m])
                l = (m + k + idx) % self.alphabets[langauge]['lettersCount']
                cryptedString += self.alphabets[langauge]['capital'][l]
            else:
                cryptedString += string[m]
            m += 1

        return cryptedString

    def encryption(self, string = '', k = 3, langauge = languages['EN']):
        m = 0
        encryptedString = ''
        while m != len(string):
            if string[m] in self.alphabets[langauge]['small']:
                l = self.alphabets[langauge]['small'].find(string[m])
                encryptedString += self.alphabets[langauge]['small'][(l - (m + k)) % self.alphabets[langauge]['lettersCount']]
            elif string[m] in self.alphabets[langauge]['capital']:
                l = self.alphabets[langauge]['capital'].find(string[m])
                encryptedString += self.alphabets[langauge]['capital'][(l - (m + k)) % self.alphabets[langauge]['lettersCount']]
            else:
                encryptedString += string[m]
            m += 1

        return encryptedString

trifemiy = Trifemiy()

print(trifemiy.cryption('Hi everyone'))
print(trifemiy.encryption('Km kcmaizzr'))