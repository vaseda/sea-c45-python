
def Main_Menu():
    """Enter the loop:
            Presents Main Menu.
            Validates User input.
            Calls Actions: Thank_you_letter, Print_Report or Quit.
            Break the loop upon Quit command.
    """
    print("Welcome to Mail room Madness")
    while True:
        print("Choose from the following:")
        print("T - Send a (T)hank You")
        print("R - Creates (R)eport")
        print("quit - Quit the program")
        command = input(">")
        if command == "T":
            Thank_you_letter()
        if command == "R":
            Print_Report()
        if command == "quit":
            break

# List of donors already consists of two people:
donators_list = {"Bill Gates": (100, 2), "John Peter": (20, 3)}


def Thank_you_letter():
    """Inputs donor name.
        If user inputs Quit command, return to the Main Menu.
        If user inputs list command, prints the list of donors.
        Call input_donation().
        Call update_donors_list().
        Call letter_thankyou().
    """
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
    """ Validates:
        If name not in donors list -- updates list with
        name and correspondent donation amount.
        If name in the list -- adds an other amount of donation
        to already existing donor.
    """
    name = donation[0]
    if name in donators_list:
        v = donators_list[name]
        donators_list[name] = (v[0]+float(donation[1]), v[1]+1)
    else:
        donators_list[name] = (float(donation[1]), 1)


def print_list():
    """ Prints list of donors. """
    for donor in list(donators_list):
        print(donor)


def Print_Report():
    """String formatting applied to the (R)eport layout.
        Sorts donators_list by total donation amount and prints formated report
        Compute historical amount and average amount of donation per donor.
        Prints Report.
        Quits to the Main menu by input: 'Press ENTER to continue'.
    """
    print("{:<20.20s} |  {:<10.10s} | {:<5.5s} |  {:<10.10s}".format("Name", "Total", "#", "Average"))
    print("_______________________________________________________")
    for name in list(donators_list):
        v = donators_list[name]
        amount = v[0]
        number_of_donations = v[1]
        print("{:<20.20s} | ${:<10.2f} | {:<5d} | ${:<10.2f}".format(name, amount, number_of_donations, amount / number_of_donations))
    input("Press Enter to Continue")


def validate_amount(str):
    """ Validates input donors amount.
    """
    try:
        v = float(str)
        if v <= 0:
            return False
        return True
    except ValueError:
        return False


# Validates input name if all symbols in the name are alphabetic.
def validate_name(str):
    """ Validates input name -- if all symbols in the name are alphabetic.
    """
    for s in str:
        if s.upper() not in "ABCDEFGHIJKLMNOPQRSTUWXYZ ":
            return False
    return True


def input_donation(name):
    """ Validates name and donation.
    """
    condition1 = True
    while condition1:
        name = name.strip()
        condition1 = not validate_name(name)
        if condition1:
            print(name, "Not a name. \n Try again...")
            name = input(">")

    condition2 = True
    while condition2:
        print("Please enter a donation amount")
        donation = input(">")
        # Checking if a string contains numerics only:
        condition2 = not validate_amount(donation)
        if condition2:
            print(donation, "Not a number. \nTry again...")
        else:
            if donation == " ":
                print(donation, "Not a number. \nTry again...")
    return (name, donation)


# Prints Thank You Letter for particular donor and his/her donation.
def letter_thankyou(donation):
    temp_letter = ("Dear XXX,\nWe are writing to express our deepest "
                            "thanks for your recent donation of YYY$ to "
                            "'Millenium Foundation'. Generous gifts from "
                            "donors like you provide the financial and moral "
                            "support needed to continue our mission. With your"
                            " faithful financial contributions over the years,"
                            " you have demonstrated your deep commitment to "
                            "our work of providing shelter for the homeless "
                            "people.\nWe look forward to a continuing "
                            "partnership with you.\nSincerely,\n'Millenium "
                            "Foundation'\n")
    letter = temp_letter.replace("XXX", donation[0]).replace("YYY", donation[1])
    print(letter)

if __name__ == "__main__":
    Main_Menu()
