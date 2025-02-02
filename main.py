
input_phrase = "I am going to be a software engineer"


def main():
    ''' This main function splits the input string by spaces and creates
    an acronym using the first letter of each word'''
    first_letters = []
    words = input_phrase.split(" ")
    for word in words:
        first_letter = word[0].capitalize()
        first_letters.append(first_letter)

    acronym = "".join(first_letters)
    print(f"Input Phrase: {input_phrase}\n")
    print(f"Acronym: {acronym}")


if __name__ == "__main__":
    main()