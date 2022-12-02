ROCK = 1
PAPER = 2
SCISSORS = 3

LOOSE = 0
DRAW = 3
WIN = 6

def to_int(input: str):
    return {'A': ROCK, 'B': PAPER, 'C': SCISSORS, 'X': ROCK, 'Y': PAPER, 'Z': SCISSORS}[input[0]]

def to_int_part_2(input: str):
    return {'A': ROCK, 'B': PAPER, 'C': SCISSORS, 'X': LOOSE, 'Y': DRAW, 'Z': WIN}[input[0]]

def score(input: tuple[int, int]):
    return {
        (ROCK, ROCK): 3,
        (ROCK, PAPER): 6,
        (ROCK, SCISSORS): 0,
        (PAPER, ROCK): 0,
        (PAPER, PAPER): 3,
        (PAPER, SCISSORS): 6,
        (SCISSORS, ROCK): 6,
        (SCISSORS, PAPER): 0,
        (SCISSORS, SCISSORS): 3
    }[input] + input[1]

def score_part_2(input: tuple[int, int]):
    return {
        (ROCK, LOOSE): SCISSORS,
        (ROCK, DRAW): ROCK,
        (ROCK, WIN): PAPER,
        (PAPER, LOOSE): ROCK,
        (PAPER, DRAW): PAPER,
        (PAPER, WIN): SCISSORS,
        (SCISSORS, LOOSE): PAPER,
        (SCISSORS, DRAW): SCISSORS,
        (SCISSORS, WIN): ROCK
    }[input] + input[1]

def main():
    with open("Puzzle 02.txt") as f:
        matches = [tuple(map(to_int_part_2, f.split(" "))) for f in f.readlines()] 
        # print(matches)

        matches_score = list(map(score_part_2, matches))
        # print(matches_score)

        print(f"According to the strategy guide, the total score is {sum(matches_score)}.")

if __name__ == "__main__":
    main()