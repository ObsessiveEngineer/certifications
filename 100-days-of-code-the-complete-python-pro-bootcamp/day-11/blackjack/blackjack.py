import random

base = [
    {
        "id": "A",
        "value": {"1": 1, "11": 11}
    },
    {
        "id": "2",
        "value": 2
    },
    {
        "id": "3",
        "value": 3
    },
    {
        "id": "4",
        "value": 4
    },
    {
        "id": "5",
        "value": 5
    },
    {
        "id": "6",
        "value": 6
    },
    {
        "id": "7",
        "value": 7
    },
    {
        "id": "8",
        "value": 8
    },
    {
        "id": "9",
        "value": 9
    },
    {
        "id": "10",
        "value": 10
    },
    {
        "id": "J",
        "value": 10
    },
    {
        "id": "Q",
        "value": 10
    },
    {
        "id": "K",
        "value": 10
    },
]


def create_deck(structure):
    deck = structure.copy()
    deck.extend(structure)
    deck.extend(structure)
    deck.extend(structure)
    return deck


def draw_card(deck: list):
    random_card = random.choice(deck)
    deck.remove(random_card)
    return random_card

def hand(hand: list):
    values = []

    for card in hand:
        if card["id"] == "A":
            values.append(card["value"]["11"])
        else:
            values.append(card["value"])
            
    if sum(values) > 21 and values.count(11):
            values[values.index(11)] = 1
    return values