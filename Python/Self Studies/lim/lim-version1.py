import random

# GLOBAL
gameField = []


def generate_game_field(game_field):
    """
    randomizing number of asterisks in array
    """
    for _i in range(0, 3):
        game_field.append(random.randint(1, 6))


def draw_game_field(game_field):
    """
    drawing game field based  on numbers
    """
    for i in range(0, 3):
        print "{}.{}\n".format(i + 1, game_field[i] * "*")


def update_game_field(game_field, line_number, asterisks_number):
    """
    :param game_field: list
    :param line_number: line to update
    :param asterisks_number: number of asterisks to remove
    :return:
    """
    game_field[line_number] = (game_field[line_number]) - asterisks_number


def user_input():
    valid_input = False
    while not valid_input:
        """
        Line number validation
        """
        print "Please choose a line to remove asterisks from\n"
        line_number = int(raw_input())
        if line_number <= 0 or line_number > len(gameField):
            print "invalid input!"
            print "please enter a value between {} and {}".format(1, len(gameField))
            continue

        """
        EMPTY line validation
        """
        if (gameField[line_number - 1]) == 0:
            print "Invalid input, this line is empty !"
            print "Choose another line!"
            continue

        else:
            valid_input = True

    valid_input = False

    while not valid_input:

        """
        The case where we have only 1 line left
        """
        anti_cheating_flag = False  # my best shot at last line problem
        if gameField[0] == 0 and gameField[1] == 0 or gameField[0] == 0 and \
                        gameField[2] == 0 or gameField[1] == 0 and gameField[2] == 0:
            print "Looks like this is a FINAL row\n"
            print "Keep in mind that removing all asterisks is STRICTLY forbidden !!!\n"
            anti_cheating_flag = True  # this was annoying!

        print "Please type a number of asterisks to remove \n"
        asterisks_number = int(raw_input())

        if anti_cheating_flag and asterisks_number == gameField[line_number - 1]:
            """
            LAST LINE SCENARIO
            """
            print "Cheating !!! YOU CANNOT REMOVE ALL asterisks "
            valid_input = False
            continue

        if asterisks_number <= 0 or asterisks_number > gameField[line_number - 1]:
            """
            asterisks input validation
            """
            print "Invalid input! asterisk number not valid ! "
            valid_input = False
            continue
        else:
            valid_input = True

    return line_number - 1, asterisks_number


def did_i_really_win(game_field):
    """
    WINNING CONDITION CASE
    """

    if (game_field[0] + game_field[1] + game_field[2]) == 1:
        return True
    else:
        return False


def main():
    game_over = False
    generate_game_field(gameField)
    draw_game_field(gameField)
    turn_number = 1

    while not game_over:
        """
        GAME LOOP
        """

        if turn_number % 2 == 0:
            """
            PLAYER COUNTER
            """
            player_counter = 2
        else:
            player_counter = 1
        print "Player {} , its your turn ".format(player_counter).upper()

        player_answer = user_input()
        update_game_field(gameField, player_answer[0], player_answer[1])
        draw_game_field(gameField)

        if did_i_really_win(gameField):
            print "You WON!"
            game_over = True

        turn_number += 1


if __name__ == '__main__':
    main()
