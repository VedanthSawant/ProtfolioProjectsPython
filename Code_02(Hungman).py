# Write python code for hungman game
# First the system will choose a random and user need to guess the correct word.
# User has 6 attempts
import random
import MyModule
print(MyModule.logo)

comp_guess = random.choice(MyModule.word_list).lower()
word_to_guess = []
word_to_guess_str = ""
life_remain = len(MyModule.stages) - 1
for i in range(len(comp_guess)):
    word_to_guess.append("_")

while life_remain > 0:
    print(f"Word to guess: {''.join(word_to_guess)}")
    user_guess = input("Guess the letter: ").lower()
    if user_guess in comp_guess:
        if user_guess in ''.join(word_to_guess):
            print(f"You have already guessed {user_guess}")
        else:
            for pos in range(len(comp_guess)):
                if comp_guess[pos] == user_guess:
                    word_to_guess[pos] = user_guess
        print(''.join(word_to_guess))
        if comp_guess == ''.join(word_to_guess):
            print("YOU WON!!")
            life_remain = 0
        else:
            print(MyModule.stages[life_remain])
            print(f"***********{life_remain}/{len(MyModule.stages) - 1} LIVES LEFT***********")
    else:
        print(f"You guessed {user_guess}, that's not in the word.")
        life_remain -= 1
        print(MyModule.stages[life_remain])
        print(f"***********{life_remain}/{len(MyModule.stages) - 1} LIVES LEFT***********")
        if life_remain == 0:
            print("YOU LOST")
