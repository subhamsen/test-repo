def main():

    print("Hello World")
    hungry = input("Are you hungry? ")
    if hungry.lower() == "yes" or hungry.lower() == "y":
        print("eat up.")
    elif hungry.lower() == 'no' or hungry.lower() == "n":
        print("stop bothering!")
    else:
        print("Way down we go!")
    print("Bye.")

if __name__ == "__main__":
    main()
