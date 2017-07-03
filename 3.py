#!/usr/bin/python

def get_player_numbers():
    number_csv = input("Enter 6 numbers, separated by commas: ")
    print number_csv
    number_list(number_csv) 
    integer_set = {int(number) for number in number_list}
    return integer_set 

print get_player_numbers()

