def get_ranged_int(prompt: str, minimum: int, maximum: int):
    while 1:
        try:
            result = int(input(prompt))
            if minimum <= result <= maximum:
                return result
        except ValueError:
            continue


def get_int(prompt: str):
    while 1:
        try:
            return int(input(prompt))
        except ValueError:
            continue
