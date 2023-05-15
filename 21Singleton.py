import random

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        self.cards = []
        self.reset()

    def reset(self):
        self.cards = []
        for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']:
            for value in range(1, 14):
                self.cards.append(Card(value, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def get_score(self):
        score = 0
        has_ace = False
        for card in self.cards:
            if card.value == 1:
                has_ace = True
            score += min(card.value, 10)
        if has_ace and score <= 11:
            score += 10
        return score

    def should_draw_card(self):
        if self.get_score() == 21:
            print(f"{self.name} has 21!")
            return False
        elif self.get_score() > 21:
            print(f"{self.name} has busted!")
            return False
        response = input(f"{self.name}, do you want to draw another card? (y/n) ")
        return response.lower() == 'y'


class Game:
    def __init__(self, player_names):
        self.deck = Deck()
        self.deck.shuffle()
        self.players = [Player(name) for name in player_names]

    def deal_cards(self):
        for _ in range(2):
            for player in self.players:
                player.add_card(self.deck.draw_card())

    def is_game_over(self):
        return all(not player.should_draw_card() for player in self.players)

    def declare_winner(self):
        winner = None
        winning_score = 0
        for player in self.players:
            score = player.get_score()
            if score > winning_score and score <= 21:
                winner = player
                winning_score = score
        if winner is not None:
            print(f"The winner is {winner.name} with a score of {winning_score}.")
        else:
            print("There is no winner.")

def get_player_names():
    num_players = 0
    while num_players < 1 or num_players > 6:
        num_players = int(input("How many players? (1-6) "))
    player_names = []
    for i in range(num_players):
        name = input(f"What is the name of player {i+1}? ")
        player_names.append(name)
    return player_names

def draw_card(player):
    card = game.deck.draw_card()
    player.add_card(card)
    print(f"{player.name} drew the {card}")

def play_game():
    player_names = get_player_names()
    game = Game(player_names)
    game.deal_cards()

    while not game.is_game_over():
        for player in game.players:
            print(f"{player.name}, your current score is {player.get_score()}")
            while player.should_draw_card():
                draw_card(player)
                print(f"{player.name}, your current score is {player.get_score()}")

    game.declare_winner()

if __name__ == '__main__':
    play_game()
