"""Functions to help play and score a game of blackjack.

How to play blackjack:    https://bicyclecards.com/how-to-play/blackjack/
"Standard" playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""

cards = {'J':10,'Q':10,'K':10,'A':1,
             '2':2,'3':3,'4':4,'5':5,'6':6,
             '7':7,'8':8,'9':9,'10':10}
def value_of_card(card):
    """Determine the scoring value of a card.

    :param card: str - given card.
    :return: int - value of a given card.  See below for values.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    
   
    return cards[card]

    


def higher_card(card_one, card_two):
    """Determine which card has a higher value in the hand.

    :param card_one, card_two: str - cards dealt in hand.  See below for values.
    :return: str or tuple - resulting Tuple contains both cards if they are of equal value.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 1
    3.  '2' - '10' = numerical value.
    """
    
    if cards[card_one]>cards[card_two]:
        return card_one
    elif cards[card_one]==cards[card_two]:
        return card_one,card_two
    else:
        return card_two
    


def value_of_ace(card_one, card_two):
    """Calculate the most advantageous value for the ace card.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: int - either 1 or 11 value of the upcoming ace card.

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if card_one =='A' or card_two == 'A':
        return 1
    elif (cards[card_one] + cards[card_two] + cards['A']<=11):
        return 11 
    else:
        return 1
    
      


def is_blackjack(card_one, card_two):
    """Determine if the hand is a 'natural' or 'blackjack'.

    :param card_one, card_two: str - card dealt. See below for values.
    :return: bool - is the hand is a blackjack (two cards worth 21).

    1.  'J', 'Q', or 'K' (otherwise known as "face cards") = 10
    2.  'A' (ace card) = 11 (if already in hand)
    3.  '2' - '10' = numerical value.
    """

    if (card_one=='A' ) and (card_two=='J' or card_two=='Q' or card_two=='K' or card_two=='10'):
       return True
    elif (card_two=='A') and (card_one=='J' or card_one=='Q' or card_one=='K' or card_one=='10'):
       return True
    else:
       return False


def can_split_pairs(card_one, card_two):
    """Determine if a player can split their hand into two hands.

    :param card_one, card_two: str - cards dealt.
    :return: bool - can the hand be split into two pairs? (i.e. cards are of the same value).
    """
    firstCard=cards[card_one]
    secondCard=cards[card_two]
    if firstCard==secondCard:
       return True
    else:
        return False
    


def can_double_down(card_one, card_two):
    """Determine if a blackjack player can place a double down bet.

    :param card_one, card_two: str - first and second cards in hand.
    :return: bool - can the hand can be doubled down? (i.e. totals 9, 10 or 11 points).
    """
    total = cards[card_one]+cards[card_two]
    if 9<=total<=11:
        return True
    else:
        return False
    

    
