import random, MyModule

def playGame(is_game_over):
    score = 0
    while not is_game_over:
        print(MyModule.high_low_logo)
        if score == 0:
            comp_dict_one = random.choice(list(MyModule.high_low_data))
        else:
            print(f"You're right! Current score: {score}")
            comp_dict_one = comp_dict_two
        print(f"Compare A: {comp_dict_one["name"]}, {comp_dict_one["description"]}, {comp_dict_one["country"]}")
        comp_count_one = comp_dict_one["follower_count"]
        print(MyModule.high_low_vs)
        comp_dict_two = random.choice(list(MyModule.high_low_data))
        print(f"Compare B: {comp_dict_two["name"]}, {comp_dict_two["description"]}, {comp_dict_two["country"]}")
        comp_count_two = comp_dict_two["follower_count"]
        user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        if user_choice == 'a':
            if comp_count_one > comp_count_two:
                is_game_over = False
                score += 1
            else:
                is_game_over = True
                print(f"Sorry, that's wrong. Final Score: {score}")
        elif user_choice == 'b':
            if comp_count_two > comp_count_one:
                is_game_over = False
                score += 1
            else:
                is_game_over = True
                print(f"Sorry, that's wrong. Final Score: {score}")
        else:
            print("Please type correctly!!!")

continue_YN = "y"
while continue_YN == "y":
    playGame(False)
    continue_YN = input("Do to want to continue playing this game? Type 'y' for YES and 'n' for NO: ")

