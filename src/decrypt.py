from cryptography.fernet import Fernet

key = open(input('  Encryption key file >> '), 'rb').read()
fernet = Fernet(key)
file = input('  File to decrypt >> ')
data = open(file, 'rb').read()
open(file, 'wb').write(fernet.decrypt(data))
print('Successfully decrypted ' + file + '!')
