alphabet = {chr(i + 97): i for i in range(0, 26)}


def indexLookup(cipherText):
    cipherIndex = list()
    for character in cipherText:
        cipherIndex.append(alphabet[character])
    return cipherIndex


def letterLookup(cipherIndex):
    characters = list()
    for index in cipherIndex:
        characters.append(list(alphabet.keys())[index])
    return characters


def encrypt(cipherIndex, b):
    plaintextIndex = list()
    for index in cipherIndex:
        (quotient, shiftedIndex) = divmod(index + b, 26)
        plaintextIndex.append(shiftedIndex)
    return plaintextIndex


def search(cipherText):
    cipherIndex = indexLookup(cipherText)
    for i in range(1, 26, 1):
        plainIndex = encrypt(cipherIndex, -i)
        plainText = letterLookup(plainIndex)
        print(i, ":", "".join(plainText))


def main():
    cipherText = open("cipherText.txt", "r")
    cipherText = cipherText.readline()
    # print(alphabet)

    for word in cipherText.split(" "):
        print("--------", word, "---------")
        search(word.lower())


if __name__ == "__main__":
    main()
