import random


def start_game():
    intro = "-" * 40
    welcome = "{}\n  Welcome to the Number Guessing Game! \n{}".format(
        intro, intro)
    print(welcome)

    solution = random.randint(1, 10)
    attempt = 1
    high_score = 0
    previous_game_score = 0

    while True:
        try:
            guessing = int(input("\nPick a number between 1 and 10: "))
            if guessing < 1 or guessing > 10:
                print(
                    "\n {} is not within range of 1-10. Please pick a number within range!\n".format(guessing))

            elif guessing > solution:
                print("\nIt's lower!")
                attempt += 1

            elif guessing < solution:
                print("\nIt's higher!")
                attempt += 1

            else:
                current_score = attempt
                if attempt == 1:
                    print("\nYou guessed it right in {} try!\n".format(attempt))
                    print("\nYour score is {}".format(
                        current_score))
                else:
                    print("\nYou guessed it right in {} tries!\n".format(attempt))
                    print("\nYour score is {}".format(
                        current_score))
                try:

                    another_try = input(
                        "\nWould you like to play again? Yes/No ")

                    if another_try.lower()[0] == "y":
                        previous_game_score = current_score
                        attempt = 1
                        high_score = min(previous_game_score, attempt)
                        solution = random.randint(1, 10)
                        print("\nScore to beat: {} ".format(
                            previous_game_score))

                    else:
                        high_score = attempt
                        if high_score < previous_game_score:
                            print(
                                "\nCongratulations! You broke the record!\n\nNew Score {}.\n\nOnly took you {} try. Till next time!\n".format(high_score, attempt))

                        else:
                            print("\nThank you for playing! Till next time!\n")
                        break

                except IndexError:
                    print("\nPlease only answer as Yes or No")

        except ValueError:
            print("\nOnly intergers or number! Not words or empty answers!")

        except TypeError as err:
            print("Only intergers or number! Not words or empty answers!")
            print("({})".format(err))


start_game()
