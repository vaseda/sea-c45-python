

def Main_Menu():
    print("Welcome to Mailroom Madness")
    while True:
        print("Choose from the following:")
        print("T - Send a (T)hank You")
        print("R - Create s (R)eport")
        print("quit - Quit the program")
        command = input(">")
        if command == "quit":
            break
        if command == "T":
            Thank_you_letter()
        if command == "R":
            Print_Report()
        else:
            print("Unknown command!")

donators_list = {"Bill Gates": (100, 2), "John Peter": (20, 3)}


def Thank_you_letter():
    while True:
        print("Please enter a name, or choose from the following:")
        print("list - Print a list of previous donors")
        print("quit - Return to main menu")
        v = input(">")
        if v == 'quit':
            break
        if v == "list":
            print_list()
        else:
            donation = input_donation(v)
            update_donors_list(donation)
            letter_thankyou(donation)


def update_donors_list(donation):
    name = donation[0]
    if name in donators_list:
        v = donators_list[name]
        donators_list[name] = (v[0]+float(donation[1]), v[1]+1)
    else:
        donators_list[name] = (float(donation[1]), 1)


def print_list():
    for donor in list(donators_list):
        print(donor)


def Print_Report():
    print("Report")
    print("{:<20.20s} |  {:<10.10s} | {:<5.5s} |  {:<10.10s} ".format("Name", "Total", "#", "Average"))
    print("_______________________________________________________")
    for name in list(donators_list):
        v = donators_list[name]
        amount = v[0]
        number_of_donations = v[1]
        print("{:<20.20s} | ${:<10.2f} | {:<5d} | ${:<10.2f} ".format(name, amount,
            number_of_donations, amount / number_of_donations))
    input("Press Enter to Continue")


def validate_amount(str):
    try:
        float(str)
        return True
    except ValueError:
        return False


def validate_name(str):
        for s in str:
            if s.upper() not in "ABCDEFGHIJKLMNOPQRSTUWXYZ ":
                return False
        return True


def input_donation(name):
    condition1 = True
    while condition1:
        name = name.strip()
        condition1 = not validate_name(name)
        if condition1:
            print(name, "Not a name. \n Try again...")
            name = input(">")

    condition2 = True
    while condition2:
        donation = input(">")
        # Checking if a string contains numerics only:
        condition2 = not validate_amount(donation)
        if condition2:
            print(donation, "Not a number. \nTry again...")
    return (name, donation)


def letter_thankyou(donation):
    temp_letter = "Dear XXX,\nThank you for YYY$.\nDonate more.\nQ Foundation"
    letter = temp_letter.replace("XXX", donation[0]).replace("YYY", donation[1])
    print(letter)


if __name__ == "__main__":
    Main_Menu()

