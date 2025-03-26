import random
from collections import Counter
class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
    def __str__(self):
        return f"{self.number} of {self.suit}"
def check_hand(hand):
    card_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
                   'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}
    numbers = [card.number for card in hand]
    suits = [card.suit for card in hand]
    number_counts = Counter(numbers)
    values = sorted(card_values[number] for number in numbers)
    count_values = sorted(number_counts.values(), reverse=True)

    flush = len(set(suits)) == 1
    values_set = set(values)
    straight = False
    if len(values_set) == 5:
        min_value = min(values)
        max_value = max(values)
        if max_value - min_value == 4:
            straight = True
        if values == [2, 3, 4, 5, 14]:
            straight = True
    if flush and straight and min(values) == 10:
        return "Royal Flush"
    if flush and straight:
        return "Straight Flush"
    if count_values == [4, 1]:
        return "Four of a Kind"
    if count_values == [3, 2]:
        return "Full House"
    if flush:
        return "Flush"
    if straight:
        return "Straight"
    if count_values == [3, 1, 1]:
        return "Three of a Kind"
    if count_values == [2, 2, 1]:
        return "Two Pair"
    if count_values == [2, 1, 1, 1]:
        return "Pair"
    return "High Card"
def calculate_percentages(poker_hands):
    hands = list(poker_hands.keys())
    counts = list(poker_hands.values())
    total_counts = sum(counts)
    percentages = [(count / total_counts) * 100 for count in counts]
    print("\nPoker Hands Percentages:")
    for hand, percentage in zip(hands, percentages):
        print(f"{hand}: {percentage:.5f}%")
def main():
    numbers = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    deck = [Card(number, suit) for number in numbers for suit in suits]
    poker_hands = {
        "High Card": 0, "Pair": 0, "Two Pair": 0, "Three of a Kind": 0,
        "Straight": 0, "Flush": 0, "Full House": 0, "Four of a Kind": 0,
        "Straight Flush": 0, "Royal Flush": 0
    }
    for i in range(10000):
        hand = random.sample(deck, 5)
        result = check_hand(hand)
        poker_hands[result] += 1
    print("Poker Hands Count:")
    for hand, count in poker_hands.items():
        print(f"{hand}: {count}")
    calculate_percentages(poker_hands)
if __name__ == "__main__":
    main()
