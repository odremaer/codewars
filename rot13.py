import string
def rot13(message):
    res = ''
    for let in message:
        if let in string.ascii_lowercase:
            res += chr((ord(let) - ord('a') + 13) % 26 + ord('a'))
        elif let in string.ascii_uppercase:
            res += chr((ord(let) - ord('A') + 13) % 26 + ord('A'))
        else:
            res += let

    return res


print(rot13('madina beliy kotek'))