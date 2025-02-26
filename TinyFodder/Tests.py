import random

class DeckofCards:
    def __init__(self, color, values):
        #Creates a Deck of Cards and shuffles
        self.cards = [f"{value} {color}" for value in values]
        self.shuffle()

    def shuffle(self):
        # Implementing a Fisher-Yates shuffle algorithm
        n = len(self.cards)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.cannonballs = 5  #Everybody starts with 5
        self.world_of_the_dead = []  #Lost cards are stored here

    def roll_dice(amount_cannonballs):
        #throws the amount of dice player and opponent had chosen
        if amount_cannonballs == 0:
            return 0, []
        diceroll = [random.randint(1,6) for _ in range(amount_cannonballs)]
        return max(diceroll), diceroll


values = ["2", "3", "4", "5", "6", "Jack", "Jack", "King", "Ace"]
player = Player("Cleo", DeckofCards("of Hearts", values))
enemy = Player("Tinybeart", DeckofCards("of Clubs", values))

print("Player: ", player.deck.cards)
print("Enemy: ", enemy.deck.cards)