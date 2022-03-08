# 恺撒密码：是一种最简单且最广为人知的加密技术。它是一种替换加密的技术，明文中的所有字母都在字母表上向后（或向前）按照一个固定数目进行偏移后被替换成密文。例如，当偏移量是3的时候，所有的字母A将被替换成D，B变成E，以此类推。解密时的密钥就是3。
# 明文：THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG
# 密文：WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ
# 用python编写给定密钥凯撒密码的加密和解密函数，并对以下英文进行加密和解密，
# 给出明文和密文。

def encoder(s):
    res = ''
    for i in s:
        if i == ' ':
            res += i
        elif ord(i) >= ord('X'):
            res += chr(ord('A') + ord(i) - ord('X'))
        else:
            res += chr(ord(i) + 3)
    return res

def decoder(s):
    res = ''
    for i in s:
        if i == ' ':
            res += i
        elif ord(i) <= ord('C'):
            res += chr(ord('Z') + ord(i) - ord('C'))
        else:
            res += chr(ord(i) - 3)
    return res

print(encoder('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'))
print(decoder('WKH TXLFN EURZQ IRA MXPSV RYHU WKH ODCB GRJ'))
