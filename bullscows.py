import random
secret_template = []


def generate_secret(secret=secret_template):
    while len(secret) < 4:
        rand_num = random.randrange(0, 10)
        if rand_num not in secret:
            secret.append(rand_num)
    return secret


def guess_numbers():
    chosen = False
    while not chosen:
        choice = input("Please enter a 4 digit number: ")
        if not choice.isnumeric():
            print("Only numbers allowed!")
        elif len(choice) != 4:
            print("Please enter exactly 4 digits!")
        else:
            chosen = True
    return list(choice)


def check_answer(guess, secret):
    bulls = 0
    cows = 0
    secret_copy = secret[:]
    for i in range(4):
        if int(guess[i]) == secret[i]:
            bulls += 1
            if int(guess[i]) in secret_copy:
                secret_copy.remove(int(guess[i]))
        elif int(guess[i]) in secret_copy:
            secret_copy.remove(int(guess[i]))
            cows += 1
    return bulls, cows


def play_game():
    game_over = False
    attempts = 0
    secret = generate_secret()
    print("Hello, we will be playing bulls and cows, I have generated a 4 digit number, all the digits are different, try and guess which one it is!\nBulls appear when the guess is in the correct position and number, a cow appears when the number is correct, but in the wrong position!")
    while not game_over:
        guess = guess_numbers()
        bulls_cows = check_answer(guess, secret)
        print("Bulls: {} \nCows: {}".format(*bulls_cows))
        if bulls_cows[0] == 4:
            print(f"Congratulations, you won in {attempts} attempts!")
            game_over = True
        else:
            attempts += 1


play_game()
