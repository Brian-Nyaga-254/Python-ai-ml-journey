def main():
    yell("This is cs50")

def yell(*words):
    """ uppercased = [] """
    """ for word in words:
        uppercased.append(word.upper()) """
    uppercased = map(str.upper, words)
    print(*uppercased)

if __name__ == "__main__":
    main()

""" *words allows any number of arguments """
    