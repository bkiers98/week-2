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
    '''
    This function takes an array of names and scores, and returns
    the name of the student with the lowest score.
    '''
    lowest_score_name = names[np.argmin(scores)]

    return(lowest_score_name)


def sort_names(names, scores):
    '''
    This function takes an array of names and scores, and returns
    an array of students' names in descending order.
    '''
    sorted_names = [(n, s) for n, s in zip(names, scores)]
    sorted_names.sort(reverse=True, key=lambda x : x[1])

    return (sorted_names)