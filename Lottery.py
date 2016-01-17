import random
import os


def main():

    # lottery_numbers = [32, 16, 19, 57, 34]
    # power_ball = 13
    # times_to_win(lottery_numbers, power_ball)

    generate_lotto_numbers(10)


def clear():
    os.system('clear')


def pwr_ball():
    x = random.randint(1, 26)
    return x


def times_to_win(args, x):
    # Call system clear
    clear()
    # Keep track of count
    count = 1
    # Infinite loop
    while True:
        clear()
        # Display goal until user presses Enter
        print("Goal Lottery Numbers: " + str(args) + " Power Ball: " + str(x))

        # Grab five non-repeating random numbers from x to y
        lottery_num = random.sample(range(13, 58, 1), 5)

        # Add Power Ball
        power_ball = pwr_ball()

        # Print out current attempt
        print("Attempt # " + str(count) + " - " + str(lottery_num) + " - Power Ball " + str(power_ball))

        # Test if the amount of like numbers = 5
        if len(set(lottery_num) & set(args)) == 5 and power_ball == x:
            print("It took " + str(count) + " times to win the lottery!")
            # Exit when found!
            exit()
        else:
            count += 1


def generate_lotto_numbers(amount):
    correct_amount = amount + 1
    for x in range(1, correct_amount):
        print('Lottery Numbers: ' + str(random.sample(range(1, 70, 1), 5)) + ' - Power Ball: ' + str(pwr_ball()))


main()
