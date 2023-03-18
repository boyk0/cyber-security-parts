from random import randint


def generate_key(binary_array = None):
    array_key = []
    if binary_array:
        for b in binary_array:
            binary_key = '0b'
            for _ in range(2, len(b)):
                binary_key += str(randint(0, 1))
            array_key.append(binary_key)
    return array_key


def generate_key_string(binary_array_key = None):
    string_key = ''
    if binary_array_key:
        for b in binary_array_key:
            string_key += chr(int(b, 2))
    return string_key


def xor(a = None, b = None):
    if not a:
        a = []
    if not b:
        b = []
    result = []
    for i in range(len(a)):
        res = '0b'
        while len(a[i]) != len(b[i]):
            if len(a[i]) > len(b[i]):
                b[i] = '0b0' + b[i][2::]
            else:
                a[i] = '0b0' + a[i][2::]
        for j in range(2, len(a[i])):
            res += str(int(a[i][j], 2) ^ int(b[i][j], 2))
        result.append(res)
    return result


def cryption(string = ''):
    binary_array = [bin(ord(x)) for x in string]
    array_key = generate_key(binary_array)
    string_key = generate_key_string(array_key)
    crypt_array = xor(binary_array, array_key)
    crypt_string = ''
    for k in crypt_array:
        crypt_string += chr(int(k, 2))
    return {
        'crypt_array': crypt_array,
        'crypt_string': crypt_string,
        'array_key': array_key,
        'string_key': string_key,
    }


def encryption(string = '', key = ''):
    encrypt_string = ''
    binary_array_encrypt_string = [bin(ord(x)) for x in string]
    binary_array_key = [bin(ord(x)) for x in key]
    en_a = xor(binary_array_key, binary_array_encrypt_string)
    for k in en_a:
        encrypt_string += chr(int(k, 2))
    return encrypt_string


operations = {
    'cryption': cryption,
    'encryption': encryption,
}

string = input('Input string for cryption\n')
crypto = cryption(string)
print(crypto)
print(crypto['crypt_string'])
print(crypto['string_key'])
print(encryption(crypto['crypt_string'], crypto['string_key']))

crypt_string = input('Input crypt string\n')
key_string = input('Input key string\n')
print(encryption(crypt_string, key_string))
