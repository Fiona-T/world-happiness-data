# import Pyfiglet library for text to fonts functionality
from pyfiglet import Figlet
# import Termcolor library for text colours
from termcolor import colored
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
    print(country)


class RowData:
    """
    each row of the csv file
    """
    def __init__(self, country, year, score):
        self.country = country
        self.year = year
        self.score = score

    def description(self):
        return f"Country: {self.country}, Year: {self.year}, Score: {self.score}"


def create_countries_list(filepath):
    """
    Open the specified csv file, create a list of countries from 1st column
    """
    with open(filepath, "r") as f:
        data = list(csv.reader(f))
        # open the file and read it, convert it to list of lists
    countries_list = []
    # empty list to add countries to
    for row in data[1:]:
        # for each row except header
        country = row[0]
        year = row[1]
        score = row[3]
        countries_list.append(RowData(country, year, score))
        # create instance of RowData class, append to countries_list
    # below prints the country for each object in the countries list
    # for countries in countries_list:
    #     print(countries.country)
    # print first object from the countries list
    print(countries_list[1])
    # print country property of first object from the countries list
    print(countries_list[1].country)
    # print output of description function from RowData class
    print(countries_list[1].description())


welcome_msg()
get_country()
create_countries_list("data/world-happiness-report.csv")
