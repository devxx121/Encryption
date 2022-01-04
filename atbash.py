# Atbash cipher - all letters of the alphapet are reversed

# Dictionary matching opposite letters
atbashdict = {
    "a" : "z", "b" : "y", "c" : "x", "d" : "w", "e" : "v", "f" : "u", "g" : "t", "h" : "s", "i" : "r", "j" : "q", "k" : "p", "l" : "o", "m" : "n", "n" : "m", "o" : "l", "p" : "k", "q" : "j", "r" : "i", "s" : "h", "t" : "g", "u" : "f", "v" : "e", "w" : "d", "x" : "c", "y" : "b", "z" : "a"
}

def atbash(_message):
    encryptedmsg = ""
    for _ in _message:
        encryptedmsg += atbashdict[_]
    print("\nOriginal:  {}\nEncrypted: {}\n".format(_message,encryptedmsg))

def main():
    message = input("[Atbash Cipher]\n\nMessage to encrypt\decrypt: ")
    atbash(message)

main()
