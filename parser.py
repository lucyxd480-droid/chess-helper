import re

def parse_game(text):
    moves = []
    my_turn = False

    for line in text.split("\n"):
        line = line.strip()

        if re.match(r"^\d+\.", line):
            parts = re.split(r"\d+\.", line)[1].strip().split()

            if len(parts) >= 1:
                moves.append(parts[0])

            if len(parts) >= 2:
                moves.append(parts[1])
            else:
                my_turn = True

    return moves, my_turn
