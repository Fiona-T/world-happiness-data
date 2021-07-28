# import Pyfiglet library for text to fonts functionality
from pyfiglet import Figlet
# import Termcolor library for text colours
from termcolor import colored
# import csv module to read the csv file
import csv


def print_banner_msg(text):
    """
    Print the text passed in, as a banner msg using Figlet font
    """
    font = Figlet(font="ogre")
    print("-" * 44)
    print(colored(font.renderText(text), "yellow"))
    print("-" * 44)


def print_smiley():
    """
    Print smiley face using ASCII characters
    """
    print("-" * 44)
    print(" " * 18 + "_" * 8)
    print(" " * 15 + "_'" + " " * 10 + "'_")
    print(" " * 13 + "." + " " * 16 + ".")
    print(" " * 12 + "/" + " " * 5 + "." + " " * 7 + "." + " " * 5 + "\\")
    print(" " * 11 + ":" + " " * 21 + ":")
    print(" " * 11 + "|" + " " * 21 + "|")
    print(" " * 11 + ":" + " " * 3 + "\\" + " " * 13 + "/" + " " * 3 + ":")
    print(" " * 12 + "\\" + " " * 3 + "`. _______ .'" + " " * 3 + "/")
    print(" " * 13 + "`." + " " * 15 + ".'")
    print(" " * 15 + "`_" + " " * 11 + "_'")
    print(" " * 18 + "' " + "-" * 6 + " '")
    print("-" * 44)


def welcome_msg():
    """
    Print banner msg, welcome text and smiley face
    """
    print_banner_msg("Welcome")
    print("Welcome to the World Happiness Data Tool\
        \nHere you can look up the Happiness Score \
        \nper country, for the years 2005 - 2020.\
            \nNote: For some countries data doesn't exist\
            \nfor every year in the range.")
    print_smiley()


def get_country():
    """
    Get country name from user
    """
    print("\nChoose the country you want to look up.")
    print("You will be shown the data for that country. \
        \nThen you can choose to view a graph of that data.")
    country = input(
        "Please enter the name of the country you want to look up:\n")
    print(f"You entered: {country}")
    return country


def create_countries_dict(filepath):
    """
    Open the specified csv file, create a list of countries from 1st column
    """
    with open(filepath, "r") as f:
        data = list(csv.reader(f))
        # open the file and read it, convert to list of lists
    country_dict = {}
    # for each list in the list of lists
    for sublist in data:
        # key is the first column (country), value is tuple of year and score
        key, value = sublist[0], tuple(sublist[1:3])
        # if the country is not already there, then add the corresponding value
        if key not in country_dict:
            country_dict[key] = value
        else:
            # if country exists, check if values are NOT a list, convert to list (1st time)
            if not isinstance(country_dict[key], list):
                country_dict[key] = [country_dict[key]]
            # append the new value to the exising list of values
            country_dict[key].append(value)
    print(country_dict)
    return country_dict


def retrieve_country_data(country, dict):
    result = dict.get(country)
    print(f"Here is the data for {country}: {result}")


welcome_msg()
country = get_country()
countries_dict = create_countries_dict("data/world-happiness-report.csv")
retrieve_country_data(country, countries_dict)
