# start original Udacity project here:
# !/usr/bin/env python3

"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""
# <<< end original Udacity project

# start my code here:
import random

# <<< end my code

# start original Udacity project here:

moves = ["rock", "paper", "scissors"]

"""The Player class is the parent class for all of the Players
in this game"""


class Player:
    def move(self):
        return "rock"

    # Just method signature here
    def learn(self, my_move, their_move):
        pass


def beats(one, two):
    return (
        (one == "rock" and two == "scissors")
        or (one == "scissors" and two == "paper")
        or (one == "paper" and two == "rock")
    )


# <<< end original Udacity project


# start my code here:
# random player class
class RandomPlayer(Player):
    def move(self):
        return random.choice(moves)


# human player class
class HumanPlayer(Player):
    def move(self):
        while True:
            move = input("Rock, Paper, or Scissors? ").lower()
            if move in moves:
                return move
            print("* Invalid move. Please choose rock, paper, or scissors.")


# <<< end my code


# start fix mentor's comment - folow code suggest, here:
# All Rock player class
class AllRockPlayer(Player):
    def move(self):
        return "rock"


# Reflect player class
class ReflectPlayer(Player):
    def __init__(self):
        super().__init__()
        self.last_opponent_move = None

    def move(self):
        if self.last_opponent_move:
            return self.last_opponent_move
        return random.choice(moves)

    def learn(self, my_move, their_move):
        self.last_opponent_move = their_move


# Cycle player class
class CyclePlayer(Player):
    def __init__(self):
        super().__init__()
        self.last_move_index = 0

    def move(self):
        self.last_move_index = (self.last_move_index + 1) % len(moves)
        return moves[self.last_move_index]

    def learn(self, my_move, their_move):
        pass


class Game:
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print("=====================")
        print(f"Player 1: {move1}  Player 2: {move2}")

        if move1 == move2:
            print("Tie!")
        elif beats(move1, move2):
            self.p1_score += 1
            print("Player 1 wins the round!")
        else:
            self.p2_score += 1
            print("Player 2 wins the round!")

        print(f"Player 1 score: {self.p1_score}")
        print(f"Player 2 score: {self.p2_score}")

        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Game start!")
        for round in range(3):
            print("=====================")
            print(f"Current round: {round + 1}")
            self.play_round()

        print("=====================")
        print(f"General scores: {round + 1}")
        print("=====================")
        print(f"Player 1 score: {self.p1_score}")
        print(f"Player 2 score: {self.p2_score}")

        # check score, Player 1 wins the game
        if self.p1_score > self.p2_score:
            print(">> Player 1 wins the game!")
        # check score, Player 2 wins the game
        elif self.p2_score > self.p1_score:
            print(">> Player 2 wins the game!")
        # Game draw
        else:
            print(">> Game draw!")


if __name__ == "__main__":
    players = {
        "1": AllRockPlayer,
        "2": RandomPlayer,
        "3": ReflectPlayer,
        "4": CyclePlayer,
        "5": HumanPlayer,
    }
    print("Player list:")
    for number, player in players.items():
        print(f"{number}. {player.__name__}")
    while (p1 := input("Choose player 1: ")) not in players.keys():
        print("Invalid choice, please select player 1 from the list.")
    while (p2 := input("Choose player 2: ")) not in players.keys():
        print("Invalid choice, please select player 2 from the list.")

    game = Game(players[p1](), players[p2]())
    game.play_game()
