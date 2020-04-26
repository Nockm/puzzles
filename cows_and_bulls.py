import random

NUM_DIGITS = 6
LOWER_BOUND = 10 ** (NUM_DIGITS - 1)
UPPER_BOUND = (10 ** NUM_DIGITS) - 1

def string_has_no_repeats(string):
    return len(string) == len(set(string))

def generate_new_answer_string():
    while True:
        answer_string = str(random.randint(LOWER_BOUND, UPPER_BOUND))
        if string_has_no_repeats(answer_string):
            return answer_string

def get_cows_and_bulls(guess_string, answer_string):
    cow_list = [1 if guess_string[x] == answer_string[x] else 0 for x in range(NUM_DIGITS)]
    bull_list = [1 if (guess_string[x] in answer_string and cow_list[x] == 0) else 0 for x in range(NUM_DIGITS)]
    return sum(cow_list), sum(bull_list)

def get_validation_error(string):
    if not string.isnumeric():
        return "Only numbers are allowed"
    elif not len(string) == NUM_DIGITS:
        return "Only {0} digits allowed".format(NUM_DIGITS)
    elif not string_has_no_repeats(string):
        return "Numbers must be unique"

def play_game(answer_string):
    while True:
        guess_string = input("Guess the {0}-digit number: ".format(NUM_DIGITS))
        error = get_validation_error(guess_string)

        if error:
            print(error)
        else:
            cows, bulls = get_cows_and_bulls(guess_string, answer_string)

            if cows != NUM_DIGITS:
                print("Cows: {0} | Bulls: {1}".format(cows, bulls))
            else:
                print("Congratulations you won!")
                return

def main():
    game_count = 0
    random.seed(95945)

    while True:
        answer_string = generate_new_answer_string()
        print("Game #{0}. (Answer is: {1})".format(game_count + 1, answer_string))
        play_game(answer_string)
        game_count += 1

if __name__ == "__main__":
    main()
