import random

secrets = ["vanessa", "tarot", "reading"]


def get_letter(status, guesses_available):
    print(status)
    print(f"Guesses available: {guesses_available}")
    letter = input("Guess a letter: ")
    letter = letter.lower()
    return letter


def check_letters(status, answer, letter):
    replaced = 0
    for index, char in enumerate(answer):
        if char == letter:
            status[index] = letter
            replaced += 1

    if replaced:
        print("Number of positions matched: " + str(replaced))

    else:
        print('No, the letter ' + letter + ' is not in my word')


def main(secrets):
    answer = random.choice(secrets)
    status = ["_"] * len(answer)
    guesses_available = len(answer) * 2
    print("Hi this is hangman version alpha, I am thinking of a word, you will be guessing letters.")

    while True:
        letter = get_letter(status, guesses_available)
        check_letters(status, answer, letter)
        guesses_available -= 1

        if not guesses_available:
            print("You have lost! The word was" + answer)
            break
        if '_' not in status:
            print("The word is: " + answer)
            print("Congrats you have won in " + str(guesses_available) + " guesses!")
            break


main(secrets)
