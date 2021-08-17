# import Pyfiglet library for text to fonts functionality
from pyfiglet import Figlet
# import Termcolor library for text colours
from termcolor import colored
# import csv module to read the csv file
import csv
# import uniplot for graph display in terminal
from uniplot import plot
# import python statistics module for median calculation
import statistics
# import the constant variables from constants.py
from constants import (
    COUNTRIES_ALT_NAMES, MORE_DATA, DIFF_COUNTRY, EXIT_APP, ALL_YEARS, DIFF_YR)


def print_banner_msg(text):
    """
    Print the text passed in, as a banner msg using Figlet font
    """
    font = Figlet(font="ogre")
    print("-" * 48)
    print(colored(font.renderText(text), "yellow"))
    print("-" * 48)


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
    print("This is the World Happiness Data Tool.")
    print(
        "You can look up the Happiness Score per country, "
        "for the years 2005 - 2020.\n")
    # print_smiley()


def get_country():
    """
    Get country name from user
    Calls validate_country to validate, loops until True returned
    Calls convert_country_alias to convert the input name to the
    standardised name (the name as per the csv file)
    Then capitalises the name (as validation done with lowercase)
    The capitalised name is returned, to be used to create country instance
    """
    while True:
        print("\nChoose the country you want to look up.")
        print("Use the common English name for the country, with no dots.")
        print("You will then be shown the years from which you can choose")
        country = input(
            "Please enter the name of the country you want to look up: \n")
        if validate_country(country):
            break
    country_std = convert_country_alias(country.lower())
    country_cap = convert_to_titlecase(country_std)
    print_output(
        f"\nYou entered '{country}'. Showing results for '{country_cap}'.")
    return country_cap


def convert_to_titlecase(string):
    """
    Converts the lower case country name back to title case
    Does not capitalise the exceptions
    Returns the country name in title case
    """
    # 'region' included below because it is not capitalised in csv file
    exceptions = ["and", "of", "region"]
    words = string.split(" ")
    title_case_words = [words[0].capitalize()]
    title_case_words += [
        word if word in exceptions else word.capitalize()
        for word in words[1:]
        ]
    title_case_string = " ".join(title_case_words)
    return title_case_string


def print_output(text):
    """
    Prints the text in yellow. Used for outputs to user.
    """
    print(colored(text, "yellow"))


def print_error_msg(e, user_input):
    """
    prints error message from the validate functions
    prints in red bold text
    """
    print(colored(
            f"Invalid choice: {e}. You entered '{user_input}'. Try again.\n",
            "red", attrs=["bold"]))


def validate_country(user_input):
    """
    Validate the user input from get_country
    1st check if numeric, if so raise error msg
    Then check if in the countries list, raise error msg
    (Convert input name to standard name in order to check if country in list)
    Using lowercase for validation. Return false if any errors, true if none
    """
    countries = [k for k in list(country_dict.keys())]
    countries_lowercase = [c.lower() for c in countries]
    try:
        if user_input.isnumeric():
            raise Exception("Numbers are not valid inputs")
        else:
            country = convert_country_alias(user_input.lower())
            if country not in countries_lowercase:
                raise Exception(
                            f"{user_input} is not in the list of countries")
    except Exception as e:
        print_error_msg(e, user_input)
        return False
    return True


def convert_country_alias(input_name):
    """
    Converts 'alias' country, names that user may enter, to name held in csv
    Returns 'std_name' which is the standardised name
    Checks if the input name is in the list of alt names for each country
    If it is, sets the input name to the standardised name
    If not, the standardised name is the input name
    """
    std_name = None
    for k, v in COUNTRIES_ALT_NAMES.items():
        if input_name in v:
            std_name = k
    if std_name is None:
        std_name = input_name
    return std_name


def create_countries_dict(filepath):
    """
    Returns global variable dictionary from the specified file path
    Key = country name
    Value = list of tuples each containing year and score pairs
    """
    with open(filepath, "r") as f:
        data = list(csv.reader(f))
    global country_dict
    country_dict = {}
    # for each list in the list of lists, excluding first one
    for sublist in data[1:]:
        # key is the first column (country), value is tuple of year and score
        key, value = sublist[0], tuple(sublist[1:3])
        # if the country is not already there, then add the corresponding value
        if key not in country_dict:
            country_dict[key] = value
        else:
            # if country exists, check if values are NOT a list
            # if not then convert to list so new values added in same list
            if not isinstance(country_dict[key], list):
                country_dict[key] = [country_dict[key]]
            # append the new value to the exising list of values
            country_dict[key].append(value)
    print(f"Creating countries dictionary from {filepath}...")
    return country_dict


class Country:
    """
    Creates an instance of Country class, for the chosen country.
    name = the country name
    scores = a list of tuples containing year, score
    for countries with more than one year, score pair:
    di = dictionary with year as k, score as v
    scores_list = a list of the scores for each year, as a float,
    so that it can be used in graph and for min, max etc.
    years = list of years (keys from the di), converted to integer,
    so that they can be used in graph
    """
    def __init__(self, name, scores):
        self.name = name
        self.scores = scores
        # if country only has one year, scores will be a tuple not list
        # in that case, don't need dictionary, scores_list or years list
        # so these are only created when country has multiple years
        if isinstance(self.scores, list):
            self.di = dict(self.scores)
            self.scores_list = [float(v) for v in list(self.di.values())]
            self.years = [int(k) for k in list(self.di.keys())]

    def get_scores(self, years_choice, single_score_c):
        """
        If country has single score, prints the year + score
        Else prints year + score for all years / selected year
        """
        if single_score_c:
            print_output(f"There is only one year available for {self.name}")
            print_output(f"The score is {self.scores[1]} for {years_choice}")
        else:
            print_output(f"The score for {self.name} for {years_choice} is:")
            if years_choice == "all years":
                [print_output(f"{k} : {v}") for k, v in self.di.items()]
            else:
                print_output(self.di.get(years_choice))

    def show_graph(self):
        """
        Plots a graph of the scores over time, using uniplot
        years and scores were previously converted to ints/floats
        years on x-axis, score on y-axis
        """
        print(self.years)
        print(self.scores_list)
        plot(
            xs=self.years, ys=self.scores_list, lines=True,
            legend_labels=["years"],
            title="Happiness scores over time")

    def show_min_score(self):
        """
        Gets the minimum score from the scores_list
        Creates a list of the years corresponding to the min score
        Prints the year OR list of years corresponding to the min score
        """
        min_score = min(self.scores_list)
        print_output(
            f"The minimum happiness score for {self.name} is: {min_score}")
        min_years = [k for (k, v) in self.di.items() if float(v) == min_score]
        if len(min_years) == 1:
            print_output(f"This score was from the year {min_years[0]}")
        else:
            print_output(
                f"This score was from the years {min_years.split(', ')}")

    def show_max_score(self):
        """
        Gets the maximum score from the scores_list
        Creates a list of the years corresponding to the max score
        Prints the year OR list of years corresponding to the max score
        """
        max_score = max(self.scores_list)
        print_output(
            f"The maximum happiness score for {self.name} is: {max_score}")
        max_years = [k for (k, v) in self.di.items() if float(v) == max_score]
        if len(max_years) == 1:
            print_output(f"This score was from the year {max_years[0]}")
        else:
            print_output(
                f"This score was from the years {max_years.split(', ')}")

    def show_median_score(self):
        """
        Get the median score from the scores_list, print to terminal
        """
        median_score = statistics.median(self.scores_list)
        print_output(
            f"The median happiness score for {self.name} is: {median_score}")

    def show_average_score(self):
        """
        Get the average score from the scores_list: total/length, rounded
        Print to terminal
        """
        total_score = sum(self.scores_list)
        average_score = round(total_score/len(self.scores_list), 2)
        print_output(
            f"The average happiness score for {self.name} is: {average_score}")


def make_country(country, countries_dict):
    """
    Create instance of Country class for the selected country using:
    country = validated country input from user, and
    country_scores = scores from the country dictionary
    """
    country_scores = countries_dict.get(country)
    c = Country(country, country_scores)
    return c


def handle_country_choice(c):
    if isinstance(c.scores, tuple):
        one_score_path(c)
    else:
        years_choice(c)


def get_years(c):
    """
    Get the requested year from the user:
    Show the list of available years from Country class instance variable
    Calls validate_years to validate, loops until True returned
    Returns choice - A for all years or specific year for one year
    """
    years = c.years
    while True:
        print_output(f"\nThe years available for {c.name} are: \n{c.years}")
        requested_years = input(
            "Enter the year you want from this list, "
            "or type in A for all years: \n")
        if requested_years == "A" or requested_years == "a":
            choice = "all years"
            break
        elif validate_years(requested_years, years):
            choice = requested_years
            break
    return choice


def validate_years(user_input, available_years):
    """
    Validate input from get_years, if it is not A or a:
    If length of input is 1, user may be trying to input A
    for all years - error to prompt user for A.
    Then, try to convert to integer, as any other inputs
    must be a number (year), so must be able to convert to int
    Then, if length is not 4 or 1, prompt user for correct length
    Then, if length is 4 (correct) but year is not in the list of
    years for that country, prompt user for correct year.
    Return False with any errors, or True if no error.
    """
    try:
        if len(user_input) == 1:
            raise Exception("Enter A for all years")
    except Exception as e:
        print_error_msg(e, user_input)
        return False
    try:
        int(user_input)
    except ValueError:
        print_error_msg("Please enter a number", user_input)
        return False
    try:
        if len(user_input) != 4 and len(user_input) != 1:
            raise Exception(
                f"Enter 4 numbers for a year, not {len(user_input)}. "
                f"Or enter A for all years")
        elif len(user_input) == 4 and int(user_input) not in available_years:
            raise Exception(f"{user_input} is not in the list")
    except Exception as e:
        print_error_msg(e, user_input)
        return False
    return True


def handle_years_choice(choice, c):
    if choice == "all years":
        all_years_path(c)
    else:
        single_yr_path(choice, c)


def get_graph_choice():
    """
    Presents option to view graph,
    Calls validate_y_n to validate the user input (converted to lowercase)
    The while loop continues until validate_y_n returns True
    And returns repsonse
    """
    while True:
        graph_q = input("Do you want to view graph of this data? Y/N: \n")
        graph = graph_q.lower()
        if validate_y_n(graph):
            break
    return graph


def validate_y_n(user_input):
    """
    Validate the input to the Y/N question
    If it is a number, raise error
    If it isn't equal to y or n, raise error
    Print the error and return false
    If no error return True back to the input function
    """
    try:
        if user_input.isdigit():
            raise Exception("Number is not a valid choice")
        elif user_input != "y" and user_input != "n":
            raise Exception("You didn't enter Y or N")
    except Exception as e:
        print_error_msg(e, user_input)
        return False
    return True


def handle_graph_choice(choice, c):
    """
    Run show_graph method if choice is Y
    The while loop continues until user enters a key to proceed
    """
    if choice == "y":
        while True:
            c.show_graph()
            proceed = input(
                "\nEnter any key(s) to continue when you are finished with the graph:"
                " \n")
            if proceed:
                break


def show_num_options(*options):
    """
    Shows options for user to choose next - iterates through
    options tuple, show number and option text.
    Calls validate_options function to check the input,
    passing length of options tuple as the max number for validation
    Continues looping until validate_options returns True
    Then returns the choice to be handled by handle_option function
    """
    while True:
        print("\nChoose the option you want next:")
        for option in options:
            print(f"{options.index(option)+1}: {option}")
        choice = input(
            "Enter the number corresponding to your choice here: \n")
        # convert the number chosen back to the option variable name
        opt_chosen = options[int(choice)-1]
        if validate_options(choice, len(options)):
            break
    return opt_chosen


def validate_options(option, num_choices):
    """
    validate the option entered by the user in show_options.
    First check if input can be converted to an integer, Print error if not
    Next try block checks if more than one number entered, raises error
    Then check if number entered is above num of options or = 0, raise error
    Except clause returns the errors raised in the try block
    Returns True when validated or False if error, to the
    while loop in the show_options() function
    """
    try:
        int(option)
    except ValueError:
        print_error_msg("Please enter a number", option)
        return False
    try:
        if len(option) > 1:
            raise ValueError(
                "Please enter only one number and no space or "
                f"characters. '{option}' is {len(option)} characters long")
        elif int(option) > num_choices or int(option) == 0:
            raise Exception(
                f"Number must be between 1 and {num_choices}")
    except (ValueError, Exception) as e:
        print_error_msg(e, option)
        return False
    return True


def handle_options(option_chosen, c):
    """
    Handle the option chosen from show_num_options
    Sends user to the relevant path based on their choice
    """
    if option_chosen == MORE_DATA:
        more_data_path(c)
    elif option_chosen == DIFF_COUNTRY:
        country_choice(country_dict)
    elif option_chosen == ALL_YEARS:
        all_years_path(c)
    elif option_chosen == DIFF_YR:
        years_choice(c)
    elif option_chosen == EXIT_APP:
        exit_program()
    else:
        print("Unknown choice, exiting programme")
        exit_program()


def more_data_options(c):
    """
    Show the options to user for Min, Max, Median, Average or All
    """
    while True:
        print(f"\nChoose from the options below for {c.name}:")
        print("1: Minimum happiness score")
        print("2: Maximum happiness score")
        print("3: Median happiness score")
        print("4: Average happiness score")
        print("5: All of these (min, max, median, average)")
        more_data_choice = input(
            "Enter 1/2/3/4/5 for the option you want from this list: \n")
        if validate_options(more_data_choice, 5):
            break
    return more_data_choice


def handle_data_options(choice, c):
    """
    handle the choice for the more_data_options function,
    i.e. Min, Max, Median, Average or All
    """
    if choice == "1":
        c.show_min_score()
    elif choice == "2":
        c.show_max_score()
    elif choice == "3":
        c.show_median_score()
    elif choice == "4":
        c.show_average_score()
    elif choice == "5":
        c.show_min_score()
        c.show_max_score()
        c.show_median_score()
        c.show_average_score()


def start():
    """
    starts the application - shows the welcome message,
    creates the country dictionary and then calls country
    choice to get user choice
    """
    welcome_msg()
    country_dict = create_countries_dict("data/world-happiness-report.csv")
    country_choice(country_dict)


def country_choice(dict):
    """
    Gets the user choice of country and creates instance of
    Country class after validating choice.
    Decides the next path available to user:
    If country only has one year (self.scores is a tuple not list)
    Then one_score_path, otherwise gets years choice from user
    """
    country = get_country()
    c = make_country(country, dict)
    handle_country_choice(c)


def one_score_path(c):
    """
    Path where country only has one year/score
    """
    year = c.scores[0]
    c.get_scores(year, True)
    option = show_num_options(DIFF_COUNTRY, EXIT_APP)
    handle_options(option, c)


def years_choice(c):
    """
    Gets the user choice of year(s) they want the score(s) for
    Decides the next path available to user based on their choice
    """
    choice = get_years(c)
    handle_years_choice(choice, c)


def single_yr_path(year, c):
    """
    Path if user chooses a single year
    """
    c.get_scores(year, False)
    option = show_num_options(
        ALL_YEARS, DIFF_YR, MORE_DATA, DIFF_COUNTRY, EXIT_APP)
    handle_options(option, c)


def all_years_path(c):
    """
    Path if user choose to view scores for all years
    """
    c.get_scores("all years", False)
    graph = get_graph_choice()
    handle_graph_choice(graph, c)
    new_choice = show_num_options(MORE_DATA, DIFF_COUNTRY, EXIT_APP)
    handle_options(new_choice, c)


def more_data_path(c):
    """
    Path to run when Option3 chosen from handle_all_years
    Show the choices
    Pass the choice to handle_data_options function
    Show further options after this
    Then handle the option chosen
    """
    more_data_choice = more_data_options(c)
    handle_data_options(more_data_choice, c)
    option = show_num_options(MORE_DATA, DIFF_COUNTRY, EXIT_APP)
    handle_options(option, c)


def exit_program():
    print("Thank you, exiting application...")
    print_banner_msg("Goodbye")
    exit()


# check if file is being ran directly, if it is start the program
if __name__ == "__main__":
    start()
