"""Functions for tracking poker hands and assorted card tasks.

Python list documentation: https://docs.python.org/3/tutorial/datastructures.html
"""

import math
def get_rounds(number):
    """Create a list containing the current and next two round numbers.

    :param number: int - current round number.
    :return: list - current round and the two that follow.
    """
    rounds =[number,number+1,number+2]
    
    
    return rounds
    


def concatenate_rounds(rounds_1, rounds_2):
    """Concatenate two lists of round numbers.

    :param rounds_1: list - first rounds played.
    :param rounds_2: list - second set of rounds played.
    :return: list - all rounds played.
    """

    newList = rounds_1 + rounds_2
    return newList


def list_contains_round(rounds, number):
    """Check if the list of rounds contains the specified number.

    :param rounds: list - rounds played.
    :param number: int - round number.
    :return: bool - was the round played?
    """
    if number in rounds:
        return True
    else:
        return False
    


def card_average(hand):
    """Calculate and returns the average card value from the list.

    :param hand: list - cards in hand.
    :return: float - average value of the cards in the hand.
    """
    length = len(hand)
    sums=sum(hand)
    avg=sums/length
    return avg
    


def approx_average_is_average(hand):
    """Return if the (average of first and last card values) OR ('middle' card) == calculated average.

    :param hand: list - cards in hand.
    :return: bool - does one of the approximate averages equal the `true average`?
    """
    actual_avg = card_average(hand)
    
    firstOne=hand[0]+hand[-1]
    avgOne= firstOne/2
    
    newlength=len(hand)
    middle=newlength//2
    
    if hand[middle] == actual_avg or avgOne == actual_avg:
        return True
    else:
        return False


def average_even_is_average_odd(hand):
    """Return if the (average of even indexed card values) == (average of odd indexed card values).

    :param hand: list - cards in hand.
    :return: bool - are even and odd averages equal?
    """

    even_numbers=hand[::2]
    avg_one=sum(even_numbers)/len(even_numbers)
    odd_numbers=hand[1::2]
    avg_two=sum(odd_numbers)/len(odd_numbers)
    if avg_one==avg_two:
        return True
    else:
        return False


def maybe_double_last(hand):
    """Multiply a Jack card value in the last index position by 2.

    :param hand: list - cards in hand.
    :return: list - hand with Jacks (if present) value doubled.
    """

    if hand[-1]==11:
        hand[-1]=22
    return hand
