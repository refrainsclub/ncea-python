import random
import input


def main():
    questions = input.get_int("how many questions would you like to answer? ")
    time_tables = list(range(1, input.get_int("how many times tables do you want? ") + 1))
    answered = 0
    print("")

    while answered < questions:
        first_number = random.choice(time_tables)
        second_number = random.choice(time_tables)

        equation = f"{first_number} × {second_number}"
        answer = first_number * second_number

        user_answer = 0
        while user_answer != answer:
            user_answer = input.get_int(f"what does {equation} equal? ")

            if user_answer != answer:
                print(f"incorrect! ✕\n")
            else:
                print("correct! ✓\n")
                break

        answered += 1

    print("you are done!")


if __name__ == "__main__":
    main()
