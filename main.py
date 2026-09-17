from calculator import add, multiply, subtract


def main():
    first_number = 10
    second_number = 3

    print(f"Addition: {first_number} + {second_number} = {add(first_number, second_number)}")
    print(f"Subtraction: {first_number} - {second_number} = {subtract(first_number, second_number)}")
    print(f"Multiplication: {first_number} * {second_number} = {multiply(first_number, second_number)}")


if __name__ == "__main__":
    main()