# a function which can encrypt string
# need a key to encrypt string and using that key(can be positive and negative whole number) to decrypt that string
# number operator % mean mod divide
# number operator // means floor divide , rounded to the next smallest whole number

# 英文字母个数 english character count
ENGCNT = 26


def encryptString(str1, password):
    password = password % ENGCNT + ENGCNT
    strEncrypt = ''
    for i in str1:
        if 'A' <= i <= 'Z':
            strEncrypt += chr((ord(i) - ord('A') + password) %
                              ENGCNT + ord('A'))
        if 'a' <= i <= 'z':
            strEncrypt += chr((ord(i) - ord('a') + password) %
                              ENGCNT + ord('a'))
        else:
            strEncrypt += i
    return strEncrypt

# and a function to decrypt the secret


def decryptString(str1, password):
    strDecrypt = ''
    for i in str1:
        if i != ' ':
            strDecrypt += chr(ord(i) - password)
        else:
            strDecrypt += ' '
    return strDecrypt


#strOrigin = 'I love you'
strOrigin = 'a'
strEncrypt = encryptString(strOrigin, -24)
print("strOrigin after encrypt is: {0:>20}.".format(strEncrypt))

strAfterDecrypt = decryptString(strEncrypt, 2)
print('strOrigin is : {0:>20}.'.format(strAfterDecrypt))

#str1 = 'a normal string'
# str after encrypt : 'b opsnbm tusjoh'
# print(dir(str))

# print(len(str))

#i = 0
#password = 1
#strEncrypt = ''

# charAfterEncrypt = chr(ord(str[i]) + password)
# print('charAfterEncrypt is : {0:5}.'.format(charAfterEncrypt))

# if i < len(str):
#    strEncrypt = str[i] + password
# for ch in str1:
#    if ch != ' ':
#        strEncrypt += chr(ord(ch) + password)
#    elif ch == ' ':
#        strEncrypt += ' '
#    else:
#        raise(NameError("Something Unusual happened"))


# print("encrypt is : {0:^10}.".format(
#    str('b opsnbm tusjoh' == strEncrypt)))
