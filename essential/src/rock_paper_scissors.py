from enum import Enum
import random

class Move(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

def winner(playerOneMove: Move, playerTwoMove: Move) -> int:
    if(playerOneMove == playerTwoMove): return 0

    playerOneWinScenarios = [
        (playerOneMove == Move.ROCK and playerTwoMove == Move.SCISSORS),
        (playerOneMove == Move.PAPER and playerTwoMove == Move.ROCK),
        (playerOneMove == Move.SCISSORS and playerTwoMove == Move.PAPER),
    ]

    return 1 if any(playerOneWinScenarios) else 2

def get_player_move() -> Move:
    while True:
        try:
            choice_str = input("Enter your choice (rock, paper, or scissors): ").upper()
            choice = Move[choice_str]
            return choice
        except KeyError:
            print("Invalid choice. Please try again.")

def announce_winner(win_res: int):
    messages ={
        0: "It's a tie, well played.",
        1: "Player 1 wins, congratulations!",
        2: "Player 2 wins, congratulations!"
    }
    
    print(messages[win_res], "\n")

def playRound():
    p1Move = get_player_move()
    p2Move = random.choice(list(Move))

    print(f"{p1Move.name} vs {p2Move.name}. Who's the winner?")
    res = winner(p1Move, p2Move)
    announce_winner(res)

def startGame():
    while True:
        playRound()
        user_input = input("Do you want to play another round? (yes/no): ")
        if user_input.lower() == "no":
            print("Thanks for playing with us today!")
            break