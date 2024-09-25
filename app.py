



verb1 = ""
verb2 = ""
noun = ""
number = 0
celebrity_guest = ""

verb1 = input("Enter your first verb: ")
verb2 = input("Enter your second verb: ")
noun = input("Enter your first noun: ")
celebrity_guest = input("Enter the name of a celebrity: ")

# Error handling for the positive integer input
while True:
    try:
        number = int(input("Enter a positive integer: "))
        if number <= 0:
            print("This integer is negative you noob")
            continue
        break
    except ValueError:
        print("That's not a valid number you noob, re-enter a POSITIVE INTEGER")

madlib = (f"Once upon a time, there was a person named {celebrity_guest}.\n"
          f"This person decided to {verb1} a {noun}.\n"
          f"Because of this, they also decided to {verb2} until it turned dark.\n"
          f"Because of the person's actions, they gained {number} coins.")


print(madlib)