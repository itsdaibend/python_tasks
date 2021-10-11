from random import choice
import string


class SimpleEncryptionAlgorithm:
    """
    This class represents simple way of encrypting, named like SEA.
    The main idea of this Algorithm is to generate a string of random values, 
    replacing the original text.
    """

    def __init__(self, incoming_data:str):
        self.incoming_data = incoming_data
        self.symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+-/\|()*&^%$#@!{~}<>,.;'[]:?=_^ 1234567890\""
    
    # This method creates new key for encryption, 
    # where key - a string of random characters.
    def generate_key(self):
        symbols_count = len(self.symbols)
        encrypted_symbols = ''

        while symbols_count > 0:
            temporary_symbol = choice(string.printable)

            if temporary_symbol not in encrypted_symbols:
                encrypted_symbols += temporary_symbol
                symbols_count-= 1
            
        return encrypted_symbols

    # This method creates dictionary of united symbols and their encrypted option, for example:
    # {'A': '&', 'B': 'm', 'C': '_', ... }
    # And encrypts the required data.
    # It's vital to have a special key to encrypt text.
    def encrypt(self, key):
        symbols_dict = dict(zip(list(self.symbols), list(key)))

        with open('simple.key', 'w') as file:
            file.write(''.join([symbols_dict[x] for x in self.incoming_data]))
    
    # Completly inversed encrypt method. Decrypts required data. 
    # It's vital to have a special key to decrypt text.
    def decrypt(self, key):
        with open('simple.key', 'r') as file:
            encrypted_data = file.read()
            symbols_dict = dict(zip(list(self.symbols), list(key)))

            result = ''
            for symbol in encrypted_data:
                for k, v in symbols_dict.items():
                    if v == symbol:
                      result += k  
            print(f'Encrypted data: {encrypted_data}, \nDecrypted data: {result}')


if __name__ == "__main__":
    while True:
        input_data = input('Enter text: ')
        SEA = SimpleEncryptionAlgorithm(input_data)

        special_key = SEA.generate_key()
        SEA.encrypt(special_key)
        SEA.decrypt(special_key)

        iteration = input('Make string backward again?[y/n]: ')
        if iteration.lower() not in ['y', 'yes']:
            break