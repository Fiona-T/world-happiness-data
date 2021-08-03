# import Pyfiglet library for text to fonts functionality
from pyfiglet import Figlet
# import Termcolor library for text colours
from termcolor import colored
# import csv module to read the csv file
import csv
# import uniplot for graph display in terminal
from uniplot import plot


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
    di is dictionary with year as k, score as v
    """
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.di = dict(self.scores)

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

    def get_scores(self, choice):
        """
        creates dictionary of the year and score from self.scores
        prints the score for the selected year
        or prints year + score for all years if all selected
        """
        print(f"The score for {self.name} for {choice} is:")
        if choice == "all years":
            # print the key and value for each item in the dict
            [print(k, ":", v) for k, v in self.di.items()]
        else:
            print(self.di.get(choice))

    def show_graph(self):
        """
        plots a graph of the scores over time, using uniplot
        first get years and scores as lists, converted to ints/floats
        then plot the graph, years on x-axis, score on y-axis
        """
        years = [int(k) for k in list(self.di.keys())]
        scores = [float(v) for v in list(self.di.values())]
        print(years)
        print(scores)
        plot(
            xs=years, ys=scores, lines=True, legend_labels=["years"],
            title="Happiness scores over time")


def make_country(country, countries_dict):
    # get scores from dictionary, to be passed when creating Class instance
    country_scores = countries_dict.get(country)
    print(country_scores)
    # create instance of Country for the selected country
    c = Country(country, country_scores)
    # test print
    print(f"Name: {c.name}, scores: {c.scores}")
    return c


def get_years():
    # gets the list of available years from method of Country class
    available_years = c.show_years()
    print(f"The years available for {c.name} are: {available_years}")
    requested_years = input(
        "Enter the year you want from this list, or type in A for all years\n")
    # test print the choice to terminal, choice All for A, or year if not A
    if requested_years == "A":
        choice = "all years"
    else:
        choice = requested_years
    print(f"thanks, you asked for {choice}")
    return choice


def graph_option():
    """
    presents option to view graph and handles repsonse
    run show_graph method if Yes
    Otherwise show the next options
    """
    graph = input("Do you want to view graph of this data? Y/N\n")
    if graph == "Y":
        c.show_graph()
        proceed = input(
            "\nPress any key to continue when you have finished with the graph\
                \n")
        if proceed:
            option = show_options(MORE_DATA, DIFF_COUNTRY, EXIT_APP)
            return option
    else:
        option = show_options(MORE_DATA, DIFF_COUNTRY, EXIT_APP)
        return option


def show_options(option1, option2, option3):
    """
    shows options for user to choose next
    returns the option to be handled by different function
    """
    print("\nChoose the option you want next:")
    print(f"1: {option1}")
    print(f"2: {option2}")
    print(f"3: {option3}")
    option = input("Enter 1, 2, or 3 here:\n")
    return option


def handle_all_years(option):
    """
    Handle the option chosen from show_options
    where the user chose all years in the get_years
    """
    if option == "1":
        print("option one all years path")
    elif option == "2":
        print("option two all years path")
    else:
        print("exiting application, all years path")
        exit()


def handle_single_year(option):
    """
    Handle the option chosen from show_options
    where the user chose single year in the get_years
    """
    if option == "1":
        print("option one single path")
    elif option == "2":
        print("option two single year path")
    else:
        print("exiting application, single year path")
        exit()


welcome_msg()
country = get_country()
countries_dict = create_countries_dict("data/world-happiness-report.csv")
c = make_country(country, countries_dict)
choice = get_years()
c.get_scores(choice)
# variables for the show_options function
MORE_DATA = f"Get more data (max, min, median, average scores) for {c.name}"
DIFF_COUNTRY = "Choose a different country"
EXIT_APP = "Exit the application"
ALL_YEARS = f"Get all years for {c.name}"
# if choice of years is all, show graph option
if choice == "all years":
    option = graph_option()
    handle_all_years(option)
else:
    # if chose single year, show next options
    option = show_options(ALL_YEARS, DIFF_COUNTRY, EXIT_APP)
    handle_single_year(option)

# if option == "1":
#     print("option 1")
#     show_max_min_options()
# elif option == "2":
#     get_country()
# else:
#     exit()
