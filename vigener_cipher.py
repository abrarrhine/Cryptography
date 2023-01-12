'''
@Vigener's Cipher@
Author: Abrar Rhine
Date: 01/12/2023
'''
# Alphabet
A = ['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'k', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Input values
text = input('\nInput text: ').upper()
key = input('\nInput key: ').upper()

# Encryption processes
i = 0
result = ''
for t in text:
    if A.count(t) != 0:
        if i == len(key):
            i = 0
        sm = A.index(key[i]) + 1
        pos = A.index(t) + sm    
        if pos >= len(A):
            pos -= len(A)
        result += A[pos]
        i += 1
    else:
        result += t

    
# Output values
print('\nEncrypted text:', result)