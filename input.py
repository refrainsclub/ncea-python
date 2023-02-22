def get_ranged_int(prompt: str, minimum: int, maximum: int) -> int:
    """Asks the user for an integer that is inside the range"""
    while 1:
        try:
            result = int(input(prompt))
            if minimum <= result <= maximum:
                return result
        except ValueError:
            print("Invalid input!\n")
            continue


def get_int(prompt: str) -> int:
    """Asks the user for an integer"""
    while 1:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input!\n")
            continue


def get_float(prompt: str) -> float:
    """Asks the user for a float"""
    while 1:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input!\n")
            continue


def get_string(prompt: str, valid_choices: list) -> str:
    """Asks a user for a string that matches one of the valid choices"""
    while 1:
        answer = input(prompt)
        if answer in valid_choices:
            return answer
        print("Invalid input!\n")
        continue
