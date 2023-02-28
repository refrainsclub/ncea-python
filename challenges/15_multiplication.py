import random
import input

TIMES_TABLES = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
QUESTIONS = 5


def main():
    answered = 0

    while answered < QUESTIONS:
        first_number = random.choice(TIMES_TABLES)
        second_number = random.choice(TIMES_TABLES)

        equation = f"{first_number} × {second_number}"
        answer = first_number * second_number

        user_answer = 0
        while user_answer != answer:
            user_answer = input.get_int(f"what does {equation} equal? ")

            if user_answer != answer:
                print(f"incorrect! try again\n")
            else:
                print("correct!\n")
                break

        answered += 1

    print("you are done!")


if __name__ == "__main__":
    main()
