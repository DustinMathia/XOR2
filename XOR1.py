'''Version 1:
    Encrypted message was only capitalized letters and no spaces.
    Key was only capitalized letters.'''
from random import randint

def create_key(m):
    k = ''
    for i in range(0, len(m)):
        k += chr(randint(65, 90))
    print 'The key is:\n%s\n' % k
    return k

def encrypt_t2t(m):
    print '\nThe message is:\n%s\n' % m
    k = create_key(m)
    e = []
    for i, p in enumerate(m):
        z = bin(ord(p) ^ ord(k[i]))
        z = z[2: len(z)]
        z = (8 - len(z)) * '0' + z
        e.append(z)
    e = ' '.join(e)
    print 'The encrypted message is:\n%s' % e

def decrypt_b2t(e, k):
    z = ''
    e = e.replace(' ', ' 0b')
    e = '0b' + e
    e = e.split(' ')
    for i, p in enumerate(e):
        z +=  chr(ord(k[i]) ^ int(p, 2))
    print '\nThe decrypted message is:\n%s\n' % z

def decrypt():
    e = raw_input('\nWhat is your encrypted message?\n\n')
    y = e
    e = e.replace(' ', '')
    for i in e:
        if i == '1' or i == '0':
            print '.'
        else:
            print '\nNot Valid character'
    if len(e) % 8 == 0:
        k = raw_input('\nWhat is your key?\n\n')
        k = k.upper()
        if len(e)/ len(k) == 8:
            decrypt_b2t(y, k)
        else:
            print '\nKey has to be the same length as the message'
    else:
        print '\nEncrypted message has to be divisible by 8'

def encrypt():
    m = raw_input('\nWhat is your message?\n\n')
    encrypt_t2t(m)

def menu():
    c = raw_input('Would you like to:\n\n1. Encrypt\n2. Decrypt\n\n')
    if c == '1':
        encrypt()
    elif c == '2':
        decrypt()
    else:
        print '\nChoose 1 or 2'
menu()