import numpy as np


# update/add code below ...

def ways(n):
    '''
    This function calculates the number of ways you can make change
    for a given amount of cents (n) using only pennies and nickels.
    '''

    #define initial return value and list of options
    num_ways = 0
    coin_combos = []

    #iterate through possible solutions, starting with least amount of nickels (0) and going to greatest amount
    for nickel in range(0, n+1, 5):
        combo = (int(nickel / 5), n - nickel)
        coin_combos.append(combo)

    num_ways = len(coin_combos)
    return (num_ways)


def lowest_score(names, scores):
    return None

def sort_names(names, scores):
    return None