"""
author: alex kelso
program: average_scores.py
date: 9/14/2020

program purpose: get an average of scores input
"""


def average():
    score1 = input("Enter Grade: ")
    score2 = input("Enter Grade: ")
    score3 = input("Enter Grade: ")
    return (int(score1) + int(score2) + int(score3))/3


if __name__ == '__main__':
    first_name = input('What\'s your first name?: ')
    last_name = input('What\'s your last name?: ')
    age = input('How old are you?: ')

    average_scores = average()
    print('{} {}, Age: {}, Average Grade: {}'.format(first_name, last_name, age, average_scores))


