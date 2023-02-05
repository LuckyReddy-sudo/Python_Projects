import random
import json

white_possibles = list(range(1, 70))
gold_possibles = list(range(1, 25))

tickets_per_drawing = int(input("Enter No of Tickets you want to buy: "))
no_of_drawings = int(input("Enter no of drawing you want to participate: "))

money_spent = 0
earnings = 0

times_won = {
    "5 + G": 0,
    "5": 0,
    "4 + G": 0,
    "4": 0,
    "3 + G": 0,
    "3": 0,
    "2 + G": 0,
    "1 + G": 0,
    "G": 0,
    "0": 0
}


def calc_win_amt(my_numbers, winning_numbers):
    win_amt = 0
    white_matches = len(winning_numbers["whites"].intersection(my_numbers["whites"]))
    gold_match = (winning_numbers["gold"] == my_numbers["gold"])

    if white_matches == 5:
        if gold_match:
            win_amt = 1_000_000_000
            times_won["5 + G"] += 1
        else:
            win_amt = 1_000_000
            times_won["5"] += 1
    elif white_matches == 4:
        if gold_match:
            win_amt =10_000
            times_won["4 + G"] += 1
        else:
            win_amt = 500
            times_won["4"] += 1
    elif white_matches == 3:
        if gold_match:
            win_amt = 200
            times_won["3 + G"] += 1
        else:
            win_amt = 10
            times_won["3"] += 1
    elif white_matches == 2 and gold_match:
        win_amt = 10
        times_won["2 + G"] += 1
    elif white_matches == 1 and gold_match:
        win_amt = 4
        times_won["1 + G"] += 1
    elif gold_match:
        win_amt = 2
        times_won["G"] += 1
    else:
        win_amt = 0
        times_won["0"] += 1
    return win_amt


for drawing in range(no_of_drawings):
    winning_whites = set(random.sample(white_possibles, k=5))
    winning_gold = random.choice(gold_possibles)

    winning_numbers = {"whites": winning_whites, "gold": winning_gold}
    for ticket in range(tickets_per_drawing):
        money_spent += 2
        my_whites = set(random.sample(white_possibles, k=5))
        my_gold = random.choice(gold_possibles)

        my_numbers = {"whites": my_whites, "gold": my_gold}

        win_amt = calc_win_amt(my_numbers, winning_numbers)
        earnings += win_amt


print(f'Total money spent: ${money_spent}')
print(f'Total earnings from MegaMillions: ${earnings}')

print(json.dumps(times_won, indent=2))

