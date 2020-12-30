from pyfiglet import figlet_format
from termcolor import colored


def strong_07(name):
    members = ("Bantu", "Tutu", "Opobo", "Nelsen")

    if name not in members:
        print(f"Sorry {name} military zone, KEEP OFF!!!")
    else:
        the_wise = figlet_format(f"Welcome wise man {name}")
        strong_name = colored(the_wise, color="yellow")
        print(strong_name)


name = input("Who goes there(Your name please)? ")
strong_07(name)



