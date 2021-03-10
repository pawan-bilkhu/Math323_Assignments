import string

abet = list(string.ascii_lowercase)
abetDict = {chr(i + 97): i for i in range(0, 26)}


def letters(x):
    text = list()
    for index in x:
        text.append(abet[index])
    return text


def ltable(text):
    ptext = list()
    for character in text:
        # print(character, " : ", abetDict[character])
        ptext.append(abetDict[character])
    return ptext


def encrypt(x, b):
    ctext = list()
    for num in x:
        (q, r) = divmod(num + b, 26)
        ctext.append(r)
    return ctext


def main():
    cipherText = "ufimeftqnqefarfuyqeufimeftqiadefarfuyqe"
    # print(abetDict)
    ctext = ltable(cipherText)
    for i in range(0, 26, 1):
        ptext = encrypt(ctext, -i)
        ptext = letters(ptext)
        print(i, ":", "".join(ptext))


if __name__ == "__main__":
    main()
