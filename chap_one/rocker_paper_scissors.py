from random import randint

idx = randint(0, 2)
opt_list = ["rock", "paper", "scissors"]

player = input("player 1, make your move...")
bot = opt_list[idx]
# can just think of one player, tie and, else the other win,
if bot == player:
    print("tied")
elif bot == "rock" and player == "scissors":
    print(f"bot is {bot}, player is {player}, bot won")
elif bot == "paper" and player == "rock":
    print(f"bot is {bot}, player is {player}, bot won")
elif bot == "scissors" and player == "paper":
    print(f"bot is {bot}, player is {player}, bot won")
else:
    print(f"bot is {bot}, player is {player}, player won")
