# Snakes & Ladder
square = 1
while True:
    roll = int(input("Enter dice roll data: "))
    if square + roll == 100:
        print(f"You are now on square {square+roll}")
        print("You Win!")
        break
    elif square + roll < 100:
        new_position = square + roll
        game_dict = {
            9 : 34,
            54 : 19,
            40 : 64, 
            90 : 48, 
            67 : 86,
            99 : 77
        }
        if new_position in game_dict:
            square = game_dict[new_position]
        else:
            square += roll
        # if new_position == 9:
        #     square = 34
        # elif new_position == 54:
        #     square = 19
        # elif new_position == 40:
        #     square = 64
        # elif new_position == 90:
        #     square = 48
        # elif new_position == 67:
        #     square = 86
        # elif new_position == 99:
        #     square = 77
        
    print(f"You are on square {square}")