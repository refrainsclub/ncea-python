# N
# 7534K66K72QK953769t859QK8A4J54Q7AQt42A23At8JJ29t83J6

POINTS = {
    "A": 4,
    "K": 3,
    "Q": 2,
    "J": 1,
}


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []


PLAYERS = [Player("N"), Player("E"), Player("S"), Player("W")]


def main():
    dealer = get_player("Enter the dealer: ")
    cards = get_cards("Enter the cards: ")

    player = dealer
    for i in range(52):
        index = (PLAYERS.index(player) + 1) % len(PLAYERS)
        player = PLAYERS[index]
        player.cards += cards[i]

    for d in PLAYERS:
        points = calculate_points(d.cards)
        print(f"{d.name} {points}", end=" ")


def get_player_by_name(name: str) -> Player:
    for d in PLAYERS:
        if d.name == name:
            return d
    raise ValueError("Player by that name does not exist")


def calculate_points(cards: list) -> int:
    points = 0
    for k, v in POINTS.items():
        count = cards.count(k)
        points += v * count
    return points


def get_player(prompt: str) -> Player:
    while 1:
        answer = input(prompt)
        try:
            dealer = get_player_by_name(answer)
            return dealer
        except ValueError:
            print(f"Please enter a valid choice!\nValid choices: N, E, S, W")


def get_cards(prompt: str) -> str:
    while 1:
        answer = input(prompt)
        if len(answer) == 52:
            return answer
        print("The string must be 52 characters in length!")


if __name__ == "__main__":
    main()
