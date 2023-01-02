# Dict = {#: '# of suit'}
# discard = set()
# deal_card
# deal = random if not in {discard}
# discard.add(deal)
# if len(discard) = 52
#   shuffle()
# return deal
from random import randint


deck = {
        1 : ['Ace of Hearts', 11],
        2 : ['Two of Hearts', 2],
        3 : ['Three of Hearts', 3],
        4 : ['Four of Hearts', 4],
        5 : ['Five of Hearts', 5],
        6 : ['Six of Hearts', 6],
        7 : ['Seven of Hearts', 7],
        8 : ['Eight of Hearts', 8],
        9 : ['Nine of Hearts', 9],
        10 : ['Ten of Hearts', 10],
        11 : ['Jack of Hearts', 10],
        12 : ['Queen of Hearts', 10],
        13 : ['King of Hearts', 10],
        14 : ['Ace of Clubs', 11],
        15 : ['Two of Clubs', 2],
        16 : ['Three of Clubs', 3],
        17 : ['Four of Clubs', 4],
        18 : ['Five of Clubs', 5],
        19 : ['Six of Clubs', 6],
        20 : ['Seven of Clubs', 7],
        21 : ['Eight of Clubs', 8],
        22 : ['Nine of Clubs', 9],
        23 : ['Ten of Clubs', 10],
        24 : ['Jack of Clubs', 10],
        25 : ['Queen of Clubs', 10],
        26 : ['King of Clubs', 10],
        27 : ['Ace of Diamonds', 11],
        28 : ['Two of Diamonds', 2],
        29 : ['Three of Diamonds', 3],
        30 : ['Four of Diamonds', 4],
        31 : ['Five of Diamonds', 5],
        32 : ['Six of Diamonds', 6],
        33 : ['Seven of Diamonds', 7],
        34 : ['Eight of Diamonds', 8],
        35 : ['Nine of Diamonds', 9],
        36 : ['Ten of Diamonds', 10],
        37 : ['Jack of Diamonds', 10],
        38 : ['Queen of Diamonds', 10],
        39 : ['King of Diamonds', 10],
        40 : ['Ace of Spades', 11],
        41 : ['Two of Spades', 2],
        42 : ['Three of Spades', 3],
        43 : ['Four of Spades', 4],
        44 : ['Five of Spades', 5],
        45 : ['Six of Spades', 6],
        46 : ['Seven of Spades', 7],
        47 : ['Eight of Spades', 8],
        48 : ['Nine of Spades', 9],
        49 : ['Ten of Spades', 10],
        50 : ['Jack of Spades', 10],
        51 : ['Queen of Spades', 10],
        52 : ['King of Spades', 10],
        }

discard = set()

def deal_card(deal = 0):
    deal = randint(1, 53)
    if deal not in discard:
        discard.add(deal)
        return deck.get(deal)
    if len(discard) == 52:
        shuffle()
    return deal_card()

def shuffle():
    discard.clear()