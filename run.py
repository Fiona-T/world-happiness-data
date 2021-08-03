# import Pyfiglet library for text to fonts functionality
from pyfiglet import Figlet
# import Termcolor library for text colours
from termcolor import colored
# import csv module to read the csv file
import csv
# import uniplot for graph display in terminal
from uniplot import plot


# variables for the show_options function
MORE_DATA = "Get more data (max, min, median, average scores) for this country"
DIFF_COUNTRY = "Choose a different country"
EXIT_APP = "Exit the application"
ALL_YEARS = "Get all years for this country"


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
    scores_list is a list of the scores for each year, as a float,
    so that it can be used in graph and for min, max etc.
    years is list of years (keys from the di), converted to integer,
    so that they can be used in graph
    """
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        self.di = dict(self.scores)
        self.scores_list = [float(v) for v in list(self.di.values())]
        self.years = [int(k) for k in list(self.di.keys())]

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
        years and scores were previously converted to ints/floats
        then plot the graph, years on x-axis, score on y-axis
        """
        print(self.years)
        print(self.scores_list)
        plot(
            xs=self.years, ys=self.scores_list, lines=True,
            legend_labels=["years"],
            title="Happiness scores over time")

    def show_min_score(self):
        min_score = min(self.scores_list)
        print(f"The minimum happiness score for {self.name} is: {min_score}")
        # print(min(self.scores_list))
        # create a list of the years corresponding to the min score
        min_years = [k for (k, v) in self.di.items() if float(v) == min_score]
        # check if just 1 year in list, change the print msg accordingly
        if len(min_years) == 1:
            print(f"This score was from the year {min_years[0]}")
        else:
            # otherwise print each year separated with the comma
            print(f"This score was from the years {min_years.split(', ')}")

    def show_max_score(self):
        print(f"The maximum happiness score for {self.name} is:")
        print(max(self.scores_list))


def make_country(country, countries_dict):
    # get scores from dictionary, to be passed when creating Class instance
    country_scores = countries_dict.get(country)
    print(country_scores)
    # create instance of Country for the selected country
    c = Country(country, country_scores)
    # test print
    print(f"Name: {c.name}, scores: {c.scores}")
    return c


def get_years(c):
    # show the list of available years from Country class instance variable
    print(f"The years available for {c.name} are: {c.years}")
    requested_years = input(
        "Enter the year you want from this list, or type in A for all years\n")
    # test print the choice to terminal, choice All for A, or year if not A
    if requested_years == "A":
        choice = "all years"
    else:
        choice = requested_years
    print(f"thanks, you asked for {choice}")
    return choice


def graph_option(c):
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


def handle_all_years(option, c):
    """
    Handle the option chosen from show_options
    where the user chose all years in the get_years
    """
    if option == "1":
        print("option one all years path, min/max etc.")
        more_data_path(c)
    elif option == "2":
        # option 2 is choose different country
        # goes back to main() to choose country from there
        print("option two all years path, choose different country")
        main()
    else:
        # option 3 is to exit the application
        print("Thank you, exiting application, all years path...")
        # print the banner text then exit
        print_banner_msg("Goodbye")
        exit()


def handle_single_year(option, c):
    """
    Handle the option chosen from show_options
    where the user chose single year in the get_years
    """
    if option == "1":
        print("option one single path, all years for same country")
        # option1 = view all years for same country
        # join the all years path - call get_scores method,
        # then call graph_option function and handle_all_years
        c.get_scores("all years")
        option = graph_option(c)
        handle_all_years(option, c)
    elif option == "2":
        # option 2 is choose different country
        # goes back to main() to choose country from there
        print("option two single year path, different country")
        main()
    else:
        # option 3 is to exit the application
        print("Thank you, exiting application, single year path")
        # print the banner text then exit
        print_banner_msg("Goodbye")
        exit()


def more_data_options(c):
    """
    Show the options to user for Min, Max, Median, Average or All
    """
    print(f"Choose from the options below for {c.name}:")
    print("1: Minimum happiness score")
    print("2: Maximum happiness score")
    print("3: Median happiness score")
    print("4: Average happiness score")
    print("5: All of these (min, max, median, average)")
    more_data_choice = input(
        "Enter 1/2/3/4/5 for the option you want from this list\n")
    print(f"You chose {more_data_choice}")
    return more_data_choice


def more_data_path(c):
    """
    Path to run when Option3 chosen from handle_all_years
    """
    more_data_choice = more_data_options(c)
    # handle choice from more_data_options
    if more_data_choice == "1":
        # option1 - min score - show_min_score method
        c.show_min_score()
    elif more_data_choice == "2":
        c.show_max_score()


def main():
    country = get_country()
    countries_dict = create_countries_dict("data/world-happiness-report.csv")
    c = make_country(country, countries_dict)
    choice = get_years(c)
    c.get_scores(choice)
    # if choice of years is all, show graph option
    if choice == "all years":
        option = graph_option(c)
        handle_all_years(option, c)
    else:
        # if chose single year, show next options
        option = show_options(ALL_YEARS, DIFF_COUNTRY, EXIT_APP)
        handle_single_year(option, c)


welcome_msg()
main()
