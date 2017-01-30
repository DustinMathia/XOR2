'''Version 1:
    Encrypted message was only capitalized letters and no spaces.
    Key was only capitalized letters.'''
'''Version 2:
    Key is now Unicode characters 21 - 126.
    Encrypted message is in Hexadecimal.
    Removed auto check.'''
#Note: Key is generated using randint
from random import randint

def create_key(m):
    k = ''
    for i in range(0, len(m)):
        k += chr(randint(0x21, 0x7E))
    print('The key is:\n%s\n' % k)
    return k

def encrypt_t2t(m):
    print('\nThe message is:\n%s\n' % m)
    k = create_key(m)
    e = []
    for i, p in enumerate(m):
        z = hex(ord(p) ^ ord(k[i]))
        z = z[2: len(z)]
        e.append(z)
    e = ' '.join(e)
    print('The encrypted message is:\n%s' % e)

def decrypt_b2t(e, k):
    z = ''
    e = e.replace(' ', ' 0x')
    e = '0x' + e
    e = e.split(' ')
    for i, p in enumerate(e):
        z +=  chr(ord(k[i]) ^ int(p, 16))
    print('\nThe decrypted message is:\n%s\n' % z)
def encrypt():
    m = input('\nWhat is your message?\n\n')
    encrypt_t2t(m)

def menu():
    c = str(input('Would you like to:\n\n1. Encrypt\n2. Decrypt\n\n'))
    if c == '1':
        encrypt()
    elif c == '2':
        e = str(input('\nWhat is your encrypted message?\n\n'))
        k = str(input('\nWhat is your key?\n\n'))
        decrypt_b2t(e, k)
    else:
        print('\nChoose 1 or 2')
menu()

#Decrypt this!
#6a 0 4b 3e a 3e 51 32 66 10 29 32 59 4a 48 57 3d 32 2f 76
#"a=[*X$\FuGQ+38#T\HW