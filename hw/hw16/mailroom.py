
def main_menu():
    """Enter the loop:
            Presents *main menu* interface as a dictionary.
            Validates user *input*.
            Calls actions: *thank_you_letter*, *print_report* or *quit*.
            Break the loop upon quit command.
            If user input not in the *main_menu* -- print: "Unknown command!"
    """
    cmd = {"t": (thank_you_letter, "Send a (T)hank You"),
           "r": (print_report, "Create a (R)eport"),
           "f": (print_to_file, "Print Thank You Letters to (F)iles"),
           "quit": (lambda: False, "Quit the program"), }
    print("\nWelcome to 'Mailroom Madness'\n")
    while True:
        print("Choose from the following:")
        prompts = sorted(["{} - {}".format(k, v[1]) for k, v in cmd.items()])
        for p in prompts:
            print(p)
        command = input(">")
        command = command.lower()
        if command in cmd:
            if not cmd[command][0]():
                break
        else:
            print("Unknown command!")


# List of donors already consists of some people:
donators_list = {
    "Bill Gates": (100, 2), "Peter Thiel": (1000, 5), "J J": (77, 1)}


def print_donor_to_file(d):
    """ Write a full set of letters to everyone to individual files on disk.
    """
    filename = "{}.txt".format(d[0].replace(" ", "_"))
    f = open(filename, 'w')
    letter = letter_thankyou(d)
    f.write(letter)
    f.close()


def print_to_file():
    """Print Tank You Letter to correspondent with donor file.
    """
    for d in donators_list.items():
        print_donor_to_file((d[0], d[1][0]))
    return True


def thank_you_letter():
    """Inputs <donor name>.
        If user inputs *quit* command, return to the *main_menu*.
        If user inputs *list* command, prints the list of donors.
        Call *input_donation*.
        Call *update_donors_list*.
        Call *letter_thankyou*.
    """
    while True:
        print("Please enter a name, or choose from the following:")
        print("list - print a list of previous donors.")
        print("quit - return to *main_menu*.")
        v = input(">")
        if v == 'quit':
            break
        if v == "list":
            print_list()
        else:
            donation = input_donation(v)
            update_donors_list(donation)
            letter = letter_thankyou(donation)
            print(letter)
    return True


def update_donors_list(donation):
    """ Validates:
        If <name> not in donors list -- updates list with
        name and correspondent donation amount.
        If <name> in the list -- adds an other amount of donation
        to already existing donor.
    """
    name = donation[0]
    if name in donators_list:
        v = donators_list[name]
        donators_list[name] = (v[0]+donation[1], v[1]+1)
    else:
        donators_list[name] = (donation[1], 1)


def print_list():
    """Prints list of donors.
    """
    for donor in list(donators_list):
        print(donor)


def print_report():
    """String formatting applied to the report layout.
        Sort *donators_list* by total donation amount and prints
        formated report.
        Compute historical amount and average amount of donation per donor.
        Prints report.
        Quits to the *main_menu* by input: 'Press ENTER to continue'.
    """
    print("{:<20.20s} |  {:<10.10s} | {:<5.5s} |  {:<10.10s}".format("Name", "Total", "#", "Average"))
    print("_______________________________________________________")
    for name in list(donators_list):
        v = donators_list[name]
        amount = v[0]
        number_of_donations = v[1]
        fmt = "{:<20.20s} | ${:<10.2f} | {:<5d} | ${:<10.2f}"
        print(fmt.format(name, amount, number_of_donations,
              amount / number_of_donations))
    input("Press Enter to Continue")
    return True


def validate_amount(amt):
    """ Validates input donors amount.
    """
    try:
        v = float(amt)
        return v > 0
    except ValueError:
        return False


def validate_name(name):
    """ Validates input <name> -- if all symbols in the <name> are alphabetic.
    """
    for s in name:
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
        print("Please enter a donation amount:")
        donation = input(">")
        # Checking if a string contains numerics only:
        condition2 = not validate_amount(donation)
        if condition2:
            print(donation, "Not a number. \nTry again...")
        else:
            if donation == " ":
                print(donation, "Not a number. \nTry again...")
    return (name, float(donation))


def letter_thankyou(donation):
    """ Prints Thank You Letter for particular donor and his/her donation.
    """
    temp_letter = ("\n\nDear {},\n\nWe are writing to express our deepest "
                   "thanks for your recent donation of ${:.2f} to "
                   "'Millenium Foundation'. Generous gifts from "
                   "donors like you provide the financial and moral "
                   "support needed to continue our mission. With your"
                   " faithful financial contributions over the years,"
                   " you have demonstrated your deep commitment to "
                   "our work of providing shelter for the homeless "
                   "people.\nWe look forward to a continuing "
                   "partnership with you.\n\nSincerely,\n\n'Millenium"
                   " Foundation'\n\n")
    letter = temp_letter.format(donation[0], donation[1])
    return letter

if __name__ == "__main__":
    main_menu()
