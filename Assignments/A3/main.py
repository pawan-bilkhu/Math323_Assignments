def main():
    residueClass = [1, 5, 7, 11, 13, 17]
    for residue in residueClass:
        generatorClass = []
        print("----", residue, "----")
        for i in range(0, 25, 1):
            (q, r) = divmod(residue * i, 18)

            if r not in generatorClass and r in residueClass:
                print(residue, "x", i, "is congruent to: ", r)
                generatorClass.append(r)
        generatorClass.sort()
        print(generatorClass)


if __name__ == "__main__":
    # execute only if run as a script
    main()
