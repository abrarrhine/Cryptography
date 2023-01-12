'''
@Caesar's Cipher@
Comments:
Author: Abrar Rhine
Date: 01/12/2023
'''

# Alphabet
A = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'k', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Input values
text = input('\nInput text: ').upper()
key = int(input('\nInput key: '))


# Encryption proccess
result = ''
for t in text:
    if A.count(t) != 0:
        pos = A.index(t)
        pos = pos + key  
        if pos >= len(A):
            pos -= len(A)
        result += A[pos]
    else:
        result += t


# Output values
print('\nEncrypted text:', result)