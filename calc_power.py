def compute_power(base, index):
    return base ** index


def main():
    base = int(input("Enter a number to calculate power: "))
    index = int(input("Enter the power for the number: "))
    print(f"{base} raised to the power {index} is {compute_power(base, index)}")

if __name__ == "__main__":
    main()
