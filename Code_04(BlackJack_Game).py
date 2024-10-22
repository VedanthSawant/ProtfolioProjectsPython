# Write a code for developing black jack game

import MyModule, random

def drawCards(card_dict):
    card_key, card_value = random.choice(list(card_dict.items()))
    return card_key, card_value

def calculateScore(card_value):
    if 11 in card_value and sum(card_value) > 21:
        card_value.remove(11)
        card_value.append(1)
        return sum(card_value)
    return sum(card_value)

def compareScore(user, comp):
    if user > 21 and comp > 21:
        return "YOU LOSE; you went over.😫"
    elif user == comp:
        return "DRAW 🤝"
    elif user > 21:
        return "YOU LOSE; you went over.😔"
    elif comp > 21:
        return "YOU WIN; computer went over.😄"
    elif user == 21:
        return "YOU WIN; BLACKJACK.😎"
    elif comp == 21:
        return "YOU LOSE; computer's BLACKJACK. 🥺"
    elif user > comp:
        return "YOU WIN!!! 🥳"
    else:
        return "YOU LOSE!!!"

def playBlackJack():
    print(MyModule.blackjack_logo)
    cards = {"Ace": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "King": 10,
             "Queen": 10, "Jack": 10}
    user_card_key, user_card_value, comp_card_key, comp_card_value = [], [], [], []
    comp_score = 0; user_score = 0
    for i in range(1, 5):
        key, val = drawCards(cards)
        if i % 2 == 0:
            user_card_key.append(key)
            user_card_value.append(val)
        else:
            comp_card_key.append(key)
            comp_card_value.append(val)
    is_game_over = False
    while not is_game_over:
        user_score = calculateScore(user_card_value)
        comp_score = calculateScore(comp_card_value)

        print(f"Your cards: [{', '.join(user_card_key)}], current score: {sum(user_card_value)}")
        print(f"Computer's first card: [{''.join(comp_card_key[0])}]")

        if user_score > 21 or comp_score > 21:
            is_game_over = True
        else:
            if input("Type 'y' to get another card, type 'n' to pass.: ").lower() == 'y':
                key, val = drawCards(cards)
                user_card_key.append(key)
                user_card_value.append(val)
            else:
                is_game_over = True

    while comp_score != 0 and comp_score < 17:
        key, val = drawCards(cards)
        comp_card_key.append(key)
        comp_card_value.append(val)
        comp_score = calculateScore(comp_card_value)

    print(f"Your final hand: [{', '.join(user_card_key)}], final score: {sum(user_card_value)}")
    print(f"Computer's final hand: [{', '.join(comp_card_key)}], final score: {sum(comp_card_value)}")
    print(compareScore(sum(user_card_value), sum(comp_card_value)))

while input("Do you want to a game of blackjack? Type 'y' or 'n'.: ").lower() == 'y':
    playBlackJack()