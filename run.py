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
    # for each list in the list of lists, excluding first one
    for sublist in data[1:]:
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


class Country:
    """
    creates an instance of Country class, for the chosen country.
    name is the country name
    scores is a list of tuples containing year, score
    """
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores

    def show_years(self):
        """
        creates a list of the available years,
        from the self.scores list of tuples (year, score)
        """
        years = []
        for data in self.scores:
            year = int(data[0])
            years.append(year)
        return years


def make_country(country, countries_dict):
    # get scores from dictionary, to be passed when creating Class instance
    country_scores = countries_dict.get(country)
    print(country_scores)
    # create instance of Country for the selected country
    c = Country(country, country_scores)
    # test print
    print(f"Name: {c.name}, scores: {c.scores}")
    # gets the list of available years from method of Country class
    available_years = c.show_years()
    print(f"The years available for {c.name} are: {available_years}")


def retrieve_country_data(country, dict):
    result = dict.get(country)
    print(f"Here is the data for {country}: {result}")


welcome_msg()
country = get_country()
countries_dict = create_countries_dict("data/world-happiness-report.csv")
# retrieve_country_data(country, countries_dict)
make_country(country, countries_dict)
