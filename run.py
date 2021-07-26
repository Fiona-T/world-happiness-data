# import Pyfiglet library for text to fonts functionality
from pyfiglet import Figlet
# import Termcolor library for text colours
from termcolor import colored


def print_banner_msg(text):
    font = Figlet(font="ogre")
    print("-" * 40)
    print(colored(font.renderText(text), "yellow"))
    print("-" * 40)


def print_smiley():
    print("-" * 40)
    print(" " * 10 + "_" * 8)
    print(" " * 7 + "_'" + " " * 10 + "'_")
    print(" " * 5 + "." + " " * 16 + ".")
    print(" " * 4 + "/" + " " * 5 + "." + " " * 7 + "." + " " * 5 + "\\")
    print(" " * 3 + ":" + " " * 21 + ":")
    print(" " * 3 + "|" + " " * 21 + "|")
    print(" " * 3 + ":" + " " * 3 + "\\" + " " * 13 + "/" + " " * 3 + ":")
    print(" " * 4 + "\\" + " " * 3 + "`. _______ .'" + " " * 3 + "/")
    print(" " * 5 + "`." + " " * 15 + ".'")
    print(" " * 7 + "`_" + " " * 11 + "_'")
    print(" " * 10 + "' " + "-" * 6 + " '")
    print("-" * 40)


print_banner_msg("Welcome")
print_smiley()
