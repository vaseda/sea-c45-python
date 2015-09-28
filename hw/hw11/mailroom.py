
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

donators_list = {"Bill Gates": (100, 2), "John Pet": (20, 3)}


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
        donators_list[name] = (v[0]+int(donation[1]), v[1]+1)
    else:
        donators_list[name] = (int(donation[1]), 1)

def print_list():       
    for donor in list(donators_list):
        print(donor)


def Print_Report():
    print("Report")
    print("Name\t  Total \t # \t average")
    for name in list(donators_list):
        v = donators_list[name]
        print(name,"\t", "$", v[0],"\t ", "$", v[1], "\t", v[0]/v[1])
    input("Press Enter to Continue")


def input_donation(name):
    condition1 = True
    while condition1:
        condition1 = not(name.isalpha() or " " in name)
        if condition1:
            print(name, "Not a name. \n Try again...")
            name = input(">")

    condition2 = True
    while condition2:
        donation = input(">")
        # Checking if a string contains numerics only:
        condition2 = not(donation.isnumeric())
        if condition2:
            print(donation, "Not a number. \nTry again...")
    return (name, donation)


def letter_thankyou(donation):
    temp_letter = "Dear XXX,\nThank you for YYY$.\nDonate more.\nQ Foundation"
    letter = temp_letter.replace("XXX", donation[0]).replace("YYY", donation[1])
    print(letter)


Main_Menu()
