def main():
    age = int(input("what is your age? "))
    age_in_ten_years = age + 10
    graduate_age = 18

    print("in 10 years you will be " + str(age_in_ten_years))

    if age_in_ten_years < graduate_age:
        print("in 10 years you will be at school")


if __name__ == "__main__":
    main()
