import random
import time

class DeckofCards:
    def __init__(self, color, values):
        #Creates a Deck of Cards and shuffles
        self.cards = [f"{color} {value}" for value in values]
        random.shuffle(self.cards)

    def draw_card(self):
        #Draws top most Card, removes it from the Stack and returns it
        return self.cards.pop(0) if self.cards else None #returns None if no Cards left

    def place_under_stack(self, card):
        #places Card under the Stack
        self.cards.append(card)

    def has_cards(self):
        #Checks whether the Stack ist not empty
        return len(self.cards) > 0

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

def show_gameboard(player, enemy, player_card, enemy_card): #will be deleted later
    #shows "background" in letters and Emoji for now. Later sprites
    print("\n" + "🌊" * 15)
    print(f"🛳 {enemy.name} is at sea!")
    print(f"[{enemy_card}] " + "🂠 " * (len(enemy.deck.cards) - 1))
    print("\n" + "-" * 30)
    print(f"🚢 {player.name} sails into battle!")
    print(f"[{player_card}] " + "🂠 " * (len(player.deck.cards) - 1))
    print("\n" + "🌊" * 15)
    print(f"{player.name}: ⚫ {player.cannonballs} cannonballs")
    print(f"{enemy.name}: ⚫ {enemy.cannonballs} cannonballs")

def battle_setup(player, enemy, player_card, enemy_card):
    #sets up logic & data necessary for battle_step
    cardSpeed = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "Jack": 6, "Queen": 6, "King": 6, "Ace": 7}
    player_value = player_card.split()[1]
    enemy_value = enemy_card.split()[1]

    if cardSpeed[player_value] > cardSpeed[enemy_value]:
        first, second = player, enemy
    elif cardSpeed[enemy_value] < cardSpeed[player_value]:
        first, second = enemy, player
    else:print("FEHLER BEI VERGLEICH")

    if player_value in ["2", "3", "4", "5", "6"] and first == player:
        attack_first = int(input(f"{first.name}, how many cannonballs do you want to fire?"))
    elif player_value in ["2", "3", "4", "5", "6"] and player_value == enemy_value:
        print("⚔ Tie! Both of you fire one cannonball!")
        return battle_step(player, enemy, 1, 1)

    elif player_value == "Jack":
        print("🛠 The cabin boy is on deck! Choose an action:")
        print("1: Retrieve all cannonballs from the sea!")
        print("2: Repair my fastest destroyed cannon!")
        choice = int(input("Your choice: "))

        if choice == 1:
            player.cannonballs = 5
            print(f"⚓ {player.name}, your cabin Boy has retrieved your cannonballs!")

        elif choice == 2:
            destroyed_cannons = [card for card in player.world_of_the_dead if card.split()[1] in ["2", "3", "4", "5", "6"]]
            if destroyed_cannons:
                repaired_cannon = max(destroyed_cannons, key=lambda x: int(x.split()[1]))
                player.world_of_the_dead.remove(repaired_cannon)
                player.DeckofCards.place_under_stack(repaired_cannon)
                print(f"🔧 {player.name}, your cabin boy has repaired the {repaired_cannon} and placed it under your stack!")
            else:
                print("❌ No Cannons to repair! Your Cannonballs will be retrieved")
                player.cannonballs = 5  #automatically if there are no destroyed cannons

            return battle_step(enemy, player, 1, 0)  #enemy attacks automatically with 1 cannonball

    elif player_value == "Queen":
        print("🧙‍♀️ The Witch brings back the Dead! Choose a Crewmember to revive!:")
        print("1: Cabin boy")
        print("2: Captain")
        print("3: Kraken")
        choice = int(input("Your Choice: "))

        if choice == 1 and "Jack" in [card.split()[1] for card in player.world_of_the_dead]:
            card_back = next(card for card in player.world_of_the_dead if "Jack" in card)
        elif choice == 2 and "King" in [card.split()[1] for card in player.world_of_the_dead]:
            card_back = next(card for card in player.world_of_the_dead if "King" in card)
        elif choice == 3 and "Ace" in [card.split()[1] for card in player.world_of_the_dead]:
            card_back = next(card for card in player.world_of_the_dead if "Ace" in card)
        else:
            print("❌ There is no matching Crewmember in the world of the Dead! The Witch disappears...")
            return "Queen"

        player.world_of_the_dead.remove(card_back)
        player.deck.place_under_stack(card_back)
        print(f"💀 {card_back} has been brought back from the Dead!")

        return "Continue"

    elif player_value == "King":
        print(f"👑 {player.name}'s Captain orders to attack with all bullets!")
        attack = player.cannonballs  #Fires all Canonballs
        result = battle_step(player, enemy, attack, 0)

        #The Captain retrieves all 5 Canonballs, regardless of whether he wins or loses
        player.cannonballs = 5
        print(f"⚓ {player.name}'s Captain has retrieves all Canonballs from the Sea!")

        return result

    elif player_value == "Ace":
        print("🌊 The Kraken destroys both Cards! 🌊")
        player.world_of_the_dead.append(player_card)
        enemy.world_of_the_dead.append(enemy_card)
        return "Kraken"

values = ["2", "3", "4", "5", "6", "Jack", "Jack", "King", "Ace"]
player = Player("Cleo", DeckofCards("of Hearts", values))
enemy = Player("Tinybeart", DeckofCards("of Clubs", values))



show_gameboard(player, enemy, "2 of Hearts", "4 of Clubs")