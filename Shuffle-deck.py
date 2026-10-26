import random

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]

deck = [(rank, suit) for suit in suits for rank in ranks]

random.shuffle(deck)

print(f"Cards in the deck: {len(deck)}")
print("Top five cards after shuffling:")

for rank, suit in deck[:5]:
    print(f"{rank} of {suit}")
