coins = 21

while True:
    print("There are", coins, "coins left.")
    print("Enter the number of coins you want to pick (1, 2, 3, or 4):")
    player_choice = int(input())
    if player_choice not in [1, 2, 3, 4]:
        print("Invalid input. Please enter a number between 1 and 4.")
        continue
    coins -= player_choice
    if coins == 0:
        print("You lost the game.")
        break


    if coins > 4:
        ai_choice = 4

    elif coins == 4:
        ai_choice = 3

    elif coins == 3:
        ai_choice = 2

    elif coins == 2:
        ai_choice = 1

    else:
        ai_choice = coins -1

    print("AI choose ", ai_choice)

    coins -= ai_choice

    if coins == 0:
        print("AI won the game.")
        break
