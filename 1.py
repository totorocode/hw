#!/usr/bin/python
import random

def menu():
# Ask player for numbers
    user_numbers = get_player_number()

# Calculate lottery numbers
    lottery_numbers = create_lottery_numbers()

# Print out the winnings
    matched_numbers = user_numbers.intersection(lottery_numbers)
    print "you won ${}!".format(100 ** len(matched_numbers))

def get_player_number():
    number_csv = input("Enter 6 numbers separated by commas: ")
    number_list = number_csv.split(",")
    integer_set = {int (number) for number in number_list}
    return integer_set

# Lottery calculates 6 random numbers (between 1 & 20)

def create_lottery_numbers():
    values = set()
    while len(values) < 6:
        values.add(random.randint(1,20))
    return values

menu()
