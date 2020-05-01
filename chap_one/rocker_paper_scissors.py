player1 = input("player 1, make your move...")
player2 = input("player 2, make your move...")
# can just think of one player, tie and, else the other win,
if player1 == player2:
    print("tied")
elif player1 == "rock" and player2 == "scissors":
    print(f"player1 is {player1}, player is {player2}, player1 won")
elif player1 == "paper" and player2 =="rock":
    print("player1 won")
elif player1 == "scissors" and player2 == "paper":
    print("player1 won")
else:
    print("player2 won")
