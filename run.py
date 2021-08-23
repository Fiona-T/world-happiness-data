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
    Print banner msg using Figlet font.

    Args:
        text (str): text to be printed
    """
    font = Figlet(font="ogre")
    print("-" * 78)
    print(colored(font.renderText(text), "yellow"))
    print("-" * 78)


def print_smiley():
    """
    Print smiley face using ASCII characters
    """
    print("-" * 78)
    print(" " * 32 + "_" * 8)
    print(" " * 29 + "_'" + " " * 10 + "'_")
    print(" " * 27 + "." + " " * 16 + ".")
    print(" " * 26 + "/" + " " * 5 + "." + " " * 7 + "." + " " * 5 + "\\")
    print(" " * 25 + ":" + " " * 21 + ":")
    print(" " * 25 + "|" + " " * 21 + "|")
    print(" " * 25 + ":" + " " * 3 + "\\" + " " * 13 + "/" + " " * 3 + ":")
    print(" " * 26 + "\\" + " " * 3 + "`. _______ .'" + " " * 3 + "/")
    print(" " * 27 + "`." + " " * 15 + ".'")
    print(" " * 29 + "`_" + " " * 11 + "_'")
    print(" " * 32 + "' " + "-" * 6 + " '")
    print("-" * 78)


def welcome_msg():
    """
    Print banner msg and intro text
    """
    print_banner_msg(" "*14 + "Welcome")
    print("This is the World Happiness Data Tool.")
    print(
        "You can look up the Happiness Score per country, "
        "for the years 2005 - 2020.\n")
    print(colored(
            "For all inputs, remember to press Enter after typing your input"
            "\n", attrs=["bold"]))
    print("-" * 78)


def create_countries_dict(filepath):
    """
    Create dictionary of countries from the csv file specified.

    Args:
        filepath (str): the path to the file

    Returns:
        country_dict (dict): global variable dictionary where key = country
        name, value = list of tuples each containing year and score pairs
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
    return country_dict


def get_country():
    """
    Get country name from user.
    Calls validate_country to validate, loops until True returned.
    Calls convert_country_alias to convert the input name to the
    standardised name (the name as per the csv file).
    Then capitalises the name (as validation done with lowercase).

    Returns:
        capitalised country name, to be used to create country instance
    """
    while True:
        print("\nChoose the country you want to look up.")
        print("Use the common English name for the country, with no dots.")
        print("You will then be shown the years from which you can choose")
        country = input(
            "\nType in the name of the country you want to look up: \n")
        if validate_country(country):
            break
    country_std = convert_country_alias(country.lower())
    country_cap = convert_to_titlecase(country_std)
    print_output(
        f"\nYou entered '{country}'. Showing results for '{country_cap}'.")
    return country_cap


class ApplicationError(Exception):
    """
    Base class for exceptions in this application.
    """
    pass


class InvalidInputError(ApplicationError):
    """
    Raised for incorrect inputs.
    """
    pass


def validate_country(user_input):
    """
    Validate the user input from get_country.
    1st check if numeric, if so raise error msg.
    Then check if in the countries list, raise error msg if not.
    (Convert input name to standard name in order to check if country in list)

    Args:
        user_input (str): the input of country name from the user to check

    Returns:
        bool: True if no errors raised, False otherwise

    Raises:
        InvalidInputError if a number is entered, or the input entered is not
        in the list of countries.
    """
    countries = [k for k in list(country_dict.keys())]
    countries_lowercase = [c.lower() for c in countries]
    try:
        if user_input.isnumeric():
            raise InvalidInputError("Numbers are not valid inputs")
        else:
            country = convert_country_alias(user_input.lower())
            if country not in countries_lowercase:
                raise InvalidInputError(
                            f"{user_input} is not in the list of countries"
                            "\nHere are the countries you can choose from,"
                            f" please choose from this list: \n{countries}\n")
    except InvalidInputError as e:
        print_error_msg(e, user_input)
        return False
    return True


def convert_country_alias(input_name):
    """
    Converts 'alias' country, names that user may enter, to name held in csv.
    Checks if the input name is in the list of alt names for each country.

    Args:
        input_name (str): the country name input by the user

    Returns:
        std_name (str): the standardised country name, which will be the name
        from the csv file if user input an alternative country name, otherwise
        it is the same as the user input
    """
    std_name = None
    for k, v in COUNTRIES_ALT_NAMES.items():
        if input_name in v:
            std_name = k
    if std_name is None:
        std_name = input_name
    return std_name


def convert_to_titlecase(string):
    """
    Converts the lower case country name back to title case.
    Does not capitalise the words listed in exceptions.

    Args:
        string (str): the string to be converted, i.e. country name

    Returns:
        the country name in title case
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


def print_error_msg(e, user_input):
    """
    Prints error message from the validate functions, in red bold.

    Args:
        e (str): the error message
        user_input (str): the input from the user, that generated the error
    """
    print(colored(
            f"Invalid choice: {e}. You entered '{user_input}'. Try again.\n",
            "red", attrs=["bold"]))


def print_output(text):
    """
    Prints the text in yellow. Used for outputs to user.

    Args:
        text (str): the text to be printed
    """
    print(colored(text, "yellow"))


class Country:
    """
    Country class, to create instance for the chosen country and use methods.

    """
    def __init__(self, name, scores):
        """
        Initializer to create instance of Country.
        The attributes self.di, self.scores_list and self.years are
        only created for countries with more than one score/year recorded.
        If country only has one year, then scores will be a tuple not list
        and these attributes are not created.

        Args:
            name (str): the country name
            scores (list): of tuples containing year, score
        """
        self.name = name
        self.scores = scores
        if isinstance(self.scores, list):
            # dictionary with year as k, score as v
            self.di = dict(self.scores)
            # list of scores for each year, as a float (for graph, max, etc.)
            self.scores_list = [float(v) for v in list(self.di.values())]
            # list of years (keys from the di), converted to int for later use
            self.years = [int(k) for k in list(self.di.keys())]

    def show_scores(self, years_choice, single_score_c):
        """
        If country has single score only, prints the year + score.
        Else prints year + score for all years / selected year.

        Args:
            years_choice (str): "all years" for all, or year for single year
            single_score_c (bool): True if single score country, else False
        """
        if single_score_c:
            print_output(
                "\nThere is only one year with a happiness score recorded for "
                f"{self.name}:")
            print_output(f"The score is {self.scores[1]} for {years_choice}")
        else:
            print_output(
                f"\nThe happiness score for {self.name} for "
                f"{years_choice} is:")
            if years_choice == "all years":
                [print_output(f"{k} : {v}") for k, v in self.di.items()]
            else:
                print_output(self.di.get(years_choice))

    def yrs_span(self):
        """
        Gets the first and last year from the years list, to be used in
        the other class methods.

        Returns:
            f string stating the span of years i.e. first and last years
        """
        return f"the years {self.years[0]} to {self.years[-1]}"

    def show_graph(self):
        """
        Plots a graph of the scores over time, using uniplot.
        years (ints so whole number) on x-axis, scores_list on y-axis.
        """
        print("\n")
        plot(
            xs=self.years, ys=self.scores_list, lines=True, color=True,
            title=f"Happiness scores for {self.yrs_span()} for {self.name}",
            height=16)

    def print_yr_for_min_max(self, score):
        """
        Creates a list of the years corresponding to the min or max score.
        Prints the year OR list of years corresponding to the min or max score.
        Called by other methods that display the min or max score.

        Args:
            score (float): min or max score for which the year will be found

        Returns:
            f string printing the year or years corresponding to min or max
        """
        min_or_max_years = [
            k for (k, v) in self.di.items() if float(v) == score]
        if len(min_or_max_years) == 1:
            score_year = f"year {min_or_max_years[0]}"
        else:
            score_year = f"years {min_or_max_years.split(', ')}"
        return f"This score was from the {score_year}."

    def show_min_or_max_score(self, min_or_max):
        """
        Gets the minimum OR maximum score from the scores_list.
        Calls print_yr_for_min_max method to show year(s) corresponding to
        min/max score.

        Args:
            min_or_max (str): "minimum" or "maximum", set by handle_num_options
        """
        if min_or_max == "minimum":
            score = min(self.scores_list)
        elif min_or_max == "maximum":
            score = max(self.scores_list)
        else:
            print("unknown minimum or maximum request, exiting.")
            exit_program()
        print_output(
            f"The {min_or_max} happiness score for {self.name} over "
            f"{self.yrs_span()} is: {score}.")
        print_output(f"{self.print_yr_for_min_max(score)}")

    def show_median_score(self):
        """
        Gets the median score from the scores_list, prints to terminal.
        """
        median_score = statistics.median(self.scores_list)
        print_output(
            f"The median happiness score for {self.name} over "
            f"{self.yrs_span()} is: {median_score}.")

    def get_average_score(self):
        """
        Gets the average score from the scores_list: total/length, rounded.
        Called by other methods that display the average score.

        Returns:
            average_score (float): average score
        """
        total_score = sum(self.scores_list)
        average_score = round(total_score/len(self.scores_list), 3)
        return average_score

    def show_average_score(self):
        """
        Prints average score to terminal.
        """
        print_output(
            f"The average happiness score for {self.name} over "
            f"{self.yrs_span()} is: {self.get_average_score()}.")

    def show_min_max_ave_med(self):
        """
        Displays the min, max, average and median scores with associated text.
        """
        min_score = min(self.scores_list)
        max_score = max(self.scores_list)
        print_output(f"Scores for {self.name} over {self.yrs_span()}:")
        print_output(
            f"Minimum happiness score: {min_score}. "
            f"{self.print_yr_for_min_max(min_score)}")
        print_output(
            f"Maximum happiness score: {max_score}. "
            f"{self.print_yr_for_min_max(max_score)}")
        print_output(
            f"Median happiness score: {statistics.median(self.scores_list)}.")
        print_output(f"Average happiness score: {self.get_average_score()}.")


def make_country(country, countries_dict):
    """
    Create instance of Country class for the selected country

    Args:
        country (str): the validated country input from user
        countries_dict (dict): dictionary of countries with their scores
    Returns:
        c (obj): instance of Country class for chosen country
    """
    country_scores = countries_dict.get(country)
    c = Country(country, country_scores)
    return c


def handle_country_choice(c):
    """
    Decides next path for user, based on country chosen in country_choice path.
    If c.scores variable is a tuple, then the country only has one score, so
    next path is the one_score_path. Otherwise, years_choice to show list of
    years to user.

    Args:
        c (obj): the instance of Country for chosen country
    """
    if isinstance(c.scores, tuple):
        one_score_path(c)
    else:
        years_choice(c)


def get_years(c):
    """
    Get the requested year from the user:
    Show the list of available years from Country class instance variable.
    Sets choice to "all years" if input is A or a.
    Calls validate_years to validate, loops until True returned

    Args:
        c(obj): the instance of Country for chosen country

    Returns:
        choice (str): user choice for years - either "all years" if
        they chose all, otherwise the selected year
    """
    available_years = c.years
    while True:
        print_output(f"\nThe years available for {c.name} are:")
        print_output(", ".join(map(str, c.years)))
        requested_years = input(
            "\nEnter the year from this list for which you want to see the "
            f"\nhappiness score for {c.name}. \nOr type in A to see the "
            f"happiness scores for all years for {c.name}: \n")
        if requested_years == "A" or requested_years == "a":
            choice = "all years"
            break
        elif validate_years(requested_years, available_years):
            choice = requested_years
            break
    return choice


def validate_years(user_input, available_years):
    """
    Validate input from get_years, if it is not A or a:
    If length of input is 1, user may be trying to input A
    for all years - error to prompt user for A.
    Then, try to convert to integer, as any other inputs
    must be a number (year), so must be able to convert to int.
    Then, if length is not 4 or 1, prompt user for correct length.
    Then, if length is 4 (correct) but year is not in the list of
    years for that country, prompt user for correct year.

    Args:
        user_input (str): the input of years choice from the user to check
        available_years (list): list of years for country

    Returns:
        bool: True if no errors raised, False otherwise.

    Raises:
        InvalidInputError if length is 1.
        ValueError if input cannot be converted to int.
        InvalidInputError if input can be converted to int AND length is not
        equal to 4 or 1, OR length is 4 but the year is not in the list.
    """
    try:
        if len(user_input) == 1:
            raise InvalidInputError("Enter A for all years")
    except InvalidInputError as e:
        print_error_msg(e, user_input)
        return False
    try:
        int(user_input)
    except ValueError:
        print_error_msg("Please enter a number", user_input)
        return False
    try:
        if len(user_input) != 4 and len(user_input) != 1:
            raise InvalidInputError(
                f"Enter 4 numbers for a year, not {len(user_input)}. "
                f"Or enter A for all years")
        elif len(user_input) == 4 and int(user_input) not in available_years:
            raise InvalidInputError(f"{user_input} is not in the list")
    except InvalidInputError as e:
        print_error_msg(e, user_input)
        return False
    return True


def handle_years_choice(choice, c):
    """
    Decides next path for user, based on the yr choice from years_choice path.
    Either show score for all years path, or show score for single year path.

    Args:
        choice (str): "all years" or the selected year, after validating.
        c (obj): the instance of Country for chosen country
    """
    if choice == "all years":
        all_years_path(c)
    else:
        single_yr_path(choice, c)


def get_graph_choice():
    """
    Presents option to view graph, calls validate_y_n to validate user input.
    The while loop continues until validate_y_n returns True

    Returns:
        graph (str): user choice y/n whether they want to view graph or not
    """
    while True:
        graph_q = input("\nDo you want to view graph of this data? Y/N: \n")
        graph = graph_q.lower()
        if validate_y_n(graph):
            break
    return graph


def validate_y_n(user_input):
    """
    Validate the input to Y/N question (to view graph):
    If it is a number, raise error.
    If it isn't equal to y or n, raise error.
    Print the error and return false.
    If no error return True back to the input function.

    Args:
        user_input (str): the input of y/n graph choice from user to check

    Returns:
        bool: True if no errors raised, False otherwise.

    Raises:
        InvalidInputError if input contains numbers, or if (lowercase)input
        does not equal y or n.
    """
    try:
        if user_input.isdigit():
            raise InvalidInputError("Number is not a valid choice")
        elif user_input != "y" and user_input != "n":
            raise InvalidInputError("You didn't enter Y or N")
    except InvalidInputError as e:
        print_error_msg(e, user_input)
        return False
    return True


def handle_graph_choice(choice, c):
    """
    Run show_graph method if choice is Y. s
    The while loop continues until user enters a key to proceed

    Args:
        choice (str): validated user input to graph question - y or n
        c (obj): the instance of Country for chosen country
    """
    if choice == "y":
        while True:
            c.show_graph()
            proceed = input(
                "\nEnter any key(s) to continue when you are finished with the"
                " graph: \n")
            if proceed:
                break


def show_num_options(*options):
    """
    Shows numbered options for user to choose next - iterates through
    options tuple, displays number along with option text.
    Calls validate_options function to check the input,
    passing length of options tuple as the max number for validation
    Continues looping until validate_options returns True

    Args:
        *options: variable length tuple of options to show the user

    Returns:
        opt_chosen: name of option chosen by user
    """
    while True:
        print("\nChoose the option you want next:")
        for option in options:
            print(f"{options.index(option)+1}: {option}")
        choice = input(
            "\nEnter the number corresponding to your choice here: \n")
        if validate_options(choice, len(options)):
            # convert the number chosen back to the option variable name
            opt_chosen = options[int(choice)-1]
            break
    return opt_chosen


def validate_options(user_input, num_choices):
    """
    Validate the option entered by the user in show_options.
    First check if input can be converted to an integer, Print error if not.
    Next try block checks if more than one number entered, raises error.
    Then check if number entered is above num of options or = 0, raise error.

    Args:
        user_input (str): the input option choice from user to check
        num_choices (int): the number of options that were presented

    Returns:
        bool: True if no errors raised, False otherwise.

    Raises:
        ValueError if input cannot be converted to int.
        InvalidInputError if input can be converted to int AND length is longer
        than 1, OR length is 1 but the number input is greater than the
        number of available choices, or the number input is 0.
    """
    try:
        int(user_input)
    except ValueError:
        print_error_msg("Please enter a number", user_input)
        return False
    try:
        if len(user_input) > 1:
            raise InvalidInputError(
                "Please enter only one number and no space or "
                f"characters. '{user_input}' is {len(user_input)} characters"
                " long")
        elif int(user_input) > num_choices or int(user_input) == 0:
            raise InvalidInputError(
                f"Number must be between 1 and {num_choices}")
    except InvalidInputError as e:
        print_error_msg(e, user_input)
        return False
    return True


def handle_options(option_chosen, c):
    """
    Handle the option chosen from show_num_options.
    Sends user to the relevant next path based on their choice

    Args:
        option_chosen: name of option chosen by user
        c (obj): the instance of Country for chosen country
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
    Show the options to user for Min, Max, Median, Average or All.
    Calls validate_options function to check the input.
    Continues looping until validate_options returns True.

    Args:
        c (obj): the instance of Country for chosen country

    Returns:
        more_data_choice (str): number for option chosen by user
    """
    while True:
        print(f"\nChoose from the options below for {c.name}:")
        print("1: Minimum happiness score")
        print("2: Maximum happiness score")
        print("3: Median happiness score")
        print("4: Average happiness score")
        print("5: All of these (min, max, median, average)")
        more_data_choice = input(
            "\nEnter 1/2/3/4/5 for the option you want from this list: \n")
        if validate_options(more_data_choice, 5):
            print("\n")
            break
    return more_data_choice


def handle_data_options(choice, c):
    """
    Handle the choice by user from more_data_options function, sends user to
    relevant next path based on their choice (Min, Max, Median, Average or All.

    Args:
        choice: number for the option chosen by user
        c (obj): the instance of Country for chosen country
    """
    if choice == "1":
        c.show_min_or_max_score("minimum")
    elif choice == "2":
        c.show_min_or_max_score("maximum")
    elif choice == "3":
        c.show_median_score()
    elif choice == "4":
        c.show_average_score()
    elif choice == "5":
        c.show_min_max_ave_med()


def start():
    """
    Starts the application - shows the welcome message, creates the
    country dictionary and then calls next path: country_choice()
    """
    welcome_msg()
    country_dict = create_countries_dict("data/world-happiness-report.csv")
    country_choice(country_dict)


def country_choice(country_dict):
    """
    Gets user choice of country, creates instance of Country class.
    handle_country_choice  function decides the next path available to user:
    one_score_path if country only has one score available,
    otherwise years_choice section.

    Args:
        country_dict(dict): dictionary of countries with years,scores
    """
    country = get_country()
    c = make_country(country, country_dict)
    handle_country_choice(c)


def one_score_path(c):
    """
    Path where country only has one year/score.
    Shows the score for that year and presents next options.
    handle_options function decides the next path available to user
    based on their choice from show_num_options function.

    Args:
        c (obj): the instance of Country for chosen country
    """
    year = c.scores[0]
    c.show_scores(year, True)
    option = show_num_options(DIFF_COUNTRY, EXIT_APP)
    handle_options(option, c)


def years_choice(c):
    """
    Gets user choice of year(s) they want the score(s) for.
    Decides the next path available to user based on their choice:
    single_yr_path or all_years_path

    Args:
        c (obj): the instance of Country for chosen country
    """
    choice = get_years(c)
    handle_years_choice(choice, c)


def single_yr_path(year, c):
    """
    Path if user chooses a single year to view score for.
    Shows the score for that year and presents next options.
    handle_options function decides the next path available to user
    based on their choice from show_num_options function.

    Args:
        c (obj): the instance of Country for chosen country
    """
    c.show_scores(year, False)
    option = show_num_options(
        ALL_YEARS, DIFF_YR, MORE_DATA, DIFF_COUNTRY, EXIT_APP)
    handle_options(option, c)


def all_years_path(c):
    """
    Path if user choose to view scores for all years
    Shows the scores for the years, shows option to view graph. Handles
    graph choice (show graph if choice is "y"), then present next options.
    handle_options function decides the next path available to user
    based on their choice from show_num_options function.

    Args:
        c (obj): the instance of Country for chosen country
    """
    c.show_scores("all years", False)
    graph = get_graph_choice()
    handle_graph_choice(graph, c)
    new_choice = show_num_options(MORE_DATA, DIFF_COUNTRY, DIFF_YR, EXIT_APP)
    handle_options(new_choice, c)


def more_data_path(c):
    """
    Path that runs when user chooses MORE_DATA from show_num_options.
    Show the choices availables - min, max, median, average, all.
    handle_data_options calls the relevant methods to show the requested data.
    Then presents next options, then handle_options function decides the
    next path available to user based on choice from show_num_options function.

    Args:
        c (obj): the instance of Country for chosen country
    """
    more_data_choice = more_data_options(c)
    handle_data_options(more_data_choice, c)
    option = show_num_options(MORE_DATA, DIFF_COUNTRY, EXIT_APP)
    handle_options(option, c)


def exit_program():
    """
    Runs when user chooses EXIT from show_num_options.
    Exits the application with exit message.
    """
    print_smiley()
    print("Thank you, exiting World Happiness Data application...")
    print("Click the RUN PROGRAM button above to run again.")
    print_banner_msg(" "*14 + "Goodbye")
    exit()


# check if file is being ran directly, if it is start the program
if __name__ == "__main__":
    start()
