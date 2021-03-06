def main():
    number = input("Enter a number: ")
    modulus = input("Enter a modulus: ")
    (quotient, remainder) = divmod(int(number), int(modulus))
    print(number, "mod", modulus, "=", remainder)


if __name__ == "__main__":
    # execute only if run as a script
    main()
