import random

class Player:
    def __init__(self, name, color, values):
        self.name = name
        self.deck = [f"{value} {color}" for value in values]  # Create deck for the player
        self.shuffle()  
        self.cannonballs = 5  
        self.world_of_the_dead = []  # Stores destroyed cards

    def shuffle(self):
        """ Shuffles deck using Fisher-Yates Algorithm """
        n = len(self.deck)
        for i in range(n - 1, 0, -1):
            j = random.randint(0, i)
            self.deck[i], self.deck[j] = self.deck[j], self.deck[i]

    def draw_card(self):
        """ Draws top card, removes it from the stack, and returns it """
        return self.deck.pop(0) if self.deck else None  # Returns None if empty

    def place_under_stack(self, card):
        """ Places a card (survived fight, repaired, revived) under the stack """
        self.deck.append(card)

    def has_cards(self):
        """ Checks if the player has cards left """
        return len(self.deck) > 0

    def roll_dice(self, amount_cannonballs):
        """ Rolls the selected number of dice and returns results """
        if amount_cannonballs == 0:
            return 0, []
        diceroll = [random.randint(1,6) for _ in range(amount_cannonballs)]
        return max(diceroll), diceroll  # Return highest and all rolls


def show_gameboard(player, enemy, player_card, enemy_card):
    """ Displays the game board with text-based visualization """
    print("\n" + "🌊" * 15)
    print(f"🛳 {enemy.name} is at sea!")
    print(f"[{enemy_card}] " + "🂠 " * (len(enemy.deck) - 1))
    print("\n" + "-" * 30)
    print(f"🚢 {player.name} sails into battle!")
    print(f"[{player_card}] " + "🂠 " * (len(player.deck) - 1))
    print("\n" + "🌊" * 15)
    print(f"{player.name}: ⚫ {player.cannonballs} cannonballs")
    print(f"{enemy.name}: ⚫ {enemy.cannonballs} cannonballs")


def battle_setup(player, enemy, player_card, enemy_card):
    """ Determines who acts first and how many cannonballs each side fires """
    try:
        cardSpeed = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "Jack": 6, "Queen": 6, "King": 6, "Ace": 7}
        player_value = player_card.split()[0]
        enemy_value = enemy_card.split()[0]

        # Determine turn order
        if cardSpeed[player_value] > cardSpeed[enemy_value]:
            first, second = player, enemy
        elif cardSpeed[enemy_value] > cardSpeed[player_value]:
            first, second = enemy, player
        else:
            print("⚔ Tie! Both of you fire one cannonball!")
            return player, enemy, 1, 1  # Default to a single cannonball each

        # First player selects attack
        max_attack_first = min(first.cannonballs, 5)
        attack_first = int(input(f"{first.name}, how many cannonballs do you want to fire? (1-{max_attack_first}): "))

        # Second player selects attack
        max_attack_second = min(second.cannonballs, 5)
        attack_second = int(input(f"{second.name}, how many cannonballs do you want to fire? (1-{max_attack_second}): "))

        return first, second, attack_first, attack_second  # Return battle details

    except ValueError:
        print("Invalid input! Please enter a number.")
        return player, enemy, 1, 1  # Default values in case of error


def battle_step(attacker, defender, attack, defense):
    """ Executes the combat phase based on chosen cannonballs """
    if attack > attacker.cannonballs:
        attack = attacker.cannonballs

    if defense > defender.cannonballs:
        defense = defender.cannonballs

    attacker.cannonballs -= attack
    defender.cannonballs -= defense

    att_roll, att_rolls = attacker.roll_dice(attack)
    def_roll, def_rolls = defender.roll_dice(defense)

    print(f"{attacker.name} shoots: {att_rolls} 🎲 Highest Roll: {att_roll}")
    print(f"{defender.name} shoots: {def_rolls} 🎲 Highest Roll: {def_roll}")

    if att_roll > def_roll:
        print(f"💥 {defender.name}'s card was destroyed!")
        defender.world_of_the_dead.append(defender.draw_card())  # Corrected card removal
    elif att_roll < def_roll:
        print(f"💥 {attacker.name}'s card was destroyed!")
        attacker.world_of_the_dead.append(attacker.draw_card())  # Corrected card removal
    else:
        print("⚔ Tie! Repeat the fight!")
        return battle_step(attacker, defender, attack, defense)  # Fixed spelling

    return "End"


# Game Setup
values = ["2", "3", "4", "5", "6", "Jack", "Queen", "King", "Ace"]
player = Player("Cleo", "of Hearts", values)
enemy = Player("Tinybeart", "of Clubs", values)

# Main game loop
while player.has_cards() and enemy.has_cards():
    player_card = player.draw_card()
    enemy_card = enemy.draw_card()

    show_gameboard(player, enemy, player_card, enemy_card)

    first, second, attack, defense = battle_setup(player, enemy, player_card, enemy_card)  # Store battle data

    battle_step(first, second, attack, defense)  # Execute the battle

print("🎉 Game Over! 🎉")
