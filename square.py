 # square.py

def square(number):
    return number * number


def main():
    number = int(input("Enter a number: "))
    result = square(number)
    print("The square of", number, "is", result)


if __name__ == "__main__":
    main()
