def first():
    with open("input.txt", "r") as f:
        shapes = {
            "A": 1,  # Rock
            "B": 2,  # Paper
            "C": 3,  # Scissors
            "X": 1,  # Rock
            "Y": 2,  # Paper
            "Z": 3,  # Scissors
        }

        outcomes = {
            "Win": 6,
            "Draw": 3,
            "Lose": 0,
        }

        rounds = f.read().splitlines()

        total_score = 0

        for round in rounds:
            opponent, choice = round.split(' ')
            print(opponent, choice)

            opponent_score = shapes[opponent]
            choice_score = shapes[choice]

            outcome = ""
            if (choice == "Z" and opponent == "B") or (choice == "Y" and opponent == "A") or (choice == "X" and opponent == "C"):
                outcome = "Win"
            elif (choice == "Z" and opponent == "A") or (choice == "Y" and opponent == "C") or (choice == "X" and opponent == "B"):
                outcome = "Lose"
            else:
                outcome = "Draw"

            outcome_score = outcomes[outcome]
            print("outcome", outcome_score)
            round_score = choice_score + outcome_score
            print(round_score)
            total_score += round_score

        print(total_score)


def second():
    with open("input.txt", "r") as f:
        shapes = {
            "A": 1,  # Rock
            "B": 2,  # Paper
            "C": 3,  # Scissors
        }
        
        win_shapes = {
            "A": "B",
            "B": "C",
            "C": "A"
        }
        loss_shapes = {
            "A": "C",
            "B": "A",
            "C": "B"
        }

        outcomes = {
            "X": 0,
            "Y": 3,
            "Z": 6,
        }

        rounds = f.read().splitlines()

        total_score = 0

        for round in rounds:
            opponent, outcome = round.split(' ')

            choice_score = 0
            if outcome == "X":
                choice_score += shapes[loss_shapes[opponent]]
            elif outcome == "Y":
                choice_score += shapes[opponent]
            elif outcome == "Z":
                choice_score += shapes[win_shapes[opponent]]

            outcome_score = outcomes[outcome]
            total_score += outcome_score + choice_score

        print(total_score)
        

second()