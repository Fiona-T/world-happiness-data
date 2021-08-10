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
            "Please enter the name of the country you want to look up:\n")
        if validate_country(country):
            break
    country_std = convert_country_alias(country.lower())
    country_cap = country_std.title()
    print(
        f"You entered '{country}'. Showing results for '{country_cap}'.")
    return country_cap


def validate_country(user_input):
    countries = [k for k in list(country_dict.keys())]
    countries_lowercase = [c.lower() for c in countries]
    try:
        if user_input.isnumeric():
            raise Exception("Numbers are not valid inputs")
        else:
            # get country name from alias list
            country = convert_country_alias(user_input.lower())
            print(f"country alias is {country}")
            # then check if country is in list
            if country not in countries_lowercase:
                raise Exception(f"{user_input} is not in the list of countries")
    except Exception as e:
        print(colored(
            f"Invalid choice: {e}. You entered '{user_input}'. Try again.\n",
            "red", attrs=["bold"]))
        return False
    return True


def convert_country_alias(input_name):
    """
    Converts 'alias' country, names that user may enter, to name held in csv
    Returns 'std_name' which is the standardised name
    Checks if the input name is in the list of alias names for each country
    If it is, sets the input name to the standardised name
    If not, the standardised name is the input name
    """
    country_alias_list = {
        "afghanistan": ["islamic republic of afghanistan"],
        "albania": ["republic of albania", "arbanon"],
        "algeria": ["people's democratic republic of algeria"],
        "angola": ["republic of angola"],
        "argentian": ["argentine republic"],
        "armenia": ["republic of armenia", "hayastan"],
        "australia": ["commonwealth of australia"],
        "austria": ["republic of austria"],
        "azerbaijan": ["republic of azerbaijan"],
        "bahrain": ["kingdom of bahrain"],
        "belarus": ["republic of belarus", "gudija"],
        "belgium": ["kingdom of belgium"],
        "benin": ["republic of benin", "dahomey"],
        "bhutan": ["kingdom of bhutan"],
        "bolivia": ["plurinational state of bolivia"],
        "bosnia and herzegovina": ["republic of bosnia and herzegovina"],
        "botswana": ["republic of botswana", "bechuanaland"],
        "brazil": ["federative republic of brazil"],
        "bulgaria": ["republic of bulgaria"],
        "burkina faso": ["upper volta"],
        "burundi": ["republic of burundi"],
        "cambodia": ["kingdom of cambodia", "kampuchea", "khmer republic"],
        "cameroon": ["republic of cameroon", "united republic of cameroon"],
        "central african republic": ["central african empire"],
        "chad": ["republic of chad"],
        "chile": ["republic of chile", "chilli", "chili"],
        "china": ["people's republic of china"],
        "colombia": ["republic of colombia"],
        "comoros": ["union of the comoros", "united republic of the commoros"],
        "costa rica": ["republic of costa cica"],
        "croatia": ["republic of croatia", "hrvatska"],
        "cuba": ["republic of cuba"],
        "cyprus": ["republic of cyprus"],
        "czech republic": ["czechia", "cr", "czechland", "the czechlands"],
        "denmark": ["kingdom of denmark", "danmark"],
        "djibouti": ["republic of djibouti"],
        "ecuador": ["republic of ecuador"],
        "egypt": ["arab republic of egypt"],
        "el salvador": ["republic of el salvador"],
        "estonia": ["republic of estonia", "esthonia"],
        "ethiopia": ["federal democratic republic of ethiopia", "abyssinia"],
        "finland": ["republic of finland", "suomi"],
        "france": ["french republic"],
        "gabon": ["gabonese republic"],
        "gambia": ["republic of the gambia", "the gambia"],
        "georgia": ["sakartvelo"],
        "germany": ["federal republic of germany", "brd", "frg"],
        "ghana": ["republic of ghana", "gold coast"],
        "greece": ["hellenic republic", "hellas"],
        "guatemala": ["republic of guatemala"],
        "guinea": ["republic of guinea", "french guinea"],
        "guyana": [
            "co‑operative republic of guyana", "british guiana",
            "cooperative republic of guyana"
            ],
        "haiti": ["republic of haiti", "hayti"],
        "honduras": ["republic of honduras"],
        "iceland": ["republic of iceland"],
        "india": ["republic of india", "union of india"],
        "indonesia": ["republic of indonesia"],
        "iran": ["islamic republic of iran", "iri"],
        "iraq": ["republic of iraq"],
        "ireland": ["republic of ireland"],
        "israel": ["state of israel"],
        "italy": ["italian republic"],
        "ivory coast": [
            "the ivory coast", "côte d'ivoire", "cote d'ivoire",
            "republic of côte d'ivoire", "republic of cote d'ivoire"
            ],
        "japan": ["nippon"],
        "jordan": ["hashemite kingdom of jordan", "hjk"],
        "kazakhstan": ["republic of kazakhstan"],
        "kenya": ["republic of kenya"],
        "kosovo": ["republic of kosovo"],
        "kuwait": ["state of kuwait"],
        "kyrgyzstan": ["kyrgyz republic"],
        "laos": ["lao people's democratic republic"],
        "latvia": ["republic of latvia"],
        "lebanon": ["the lebanese republic", "the lebanon"],
        "lesotho": ["kingdom of lesotho"],
        "liberia": ["republic of liberia"],
        "libya": ["state of libya"],
        "lithuania": ["republic of lithuania"],
        "luxembourg": ["grand duchy of luxembourg"],
        "madagascar": ["republic of madagascar"],
        "malawi": ["republic of malawi"],
        "malaysia": ["persekutuan malaysia", "federation of malaysia"],
        "maldives": [
            "republic of the maldives", "the maldive islands", "the maldives"
            ],
        "mali": ["republic of mali"],
        "malta": ["republic of malta"],
        "mauritania": ["islamic republic of mauritania"],
        "mauritius": ["republic of mauritius"],
        "mexico": ["united mexican states", "mex", "mx"],
        "moldova": ["republic of moldova", "moldavia"],
        "morocco": ["kingdom of morocco"],
        "mozambique": ["republic of mozambique"],
        "myanmar": ["republic of the union of myanmar", "burma"],
        "namibia": ["republic of namibia"],
        "nepal": ["federal democratic republic of nepal", "kingdom of nepal"],
        "netherlands": [
            "kingdom of the netherlands", "holland", "the netherlands"
            ],
        "new zealand": ["aotearoa"],
        "nicaragua": ["republic of nicaragua"],
        "niger": ["republic of the niger", "the niger"],
        "nigeria": ["federal republic of nigeria"],
        "north cyprus": [
            "northern cyprus", "turkish republic of northern cyprus", "trnc"
            ],
        "north macedonia": ["republic of north macedonia", "macedonia"],
        "norway": ["kingdom of norway"],
        "oman": ["sultanate of oman"],
        "pakistan": ["islamic republic of pakistan", "federation of pakistan"],
        "palestinian territories": [
            "palestine", "state of palestine", "palestinian national authority"
            ],
        "panama": ["republic of panama"],
        "paraguay": ["republic of paraguay"],
        "peru": ["republic of peru"],
        "philippines": ["republic of the philippines", "the philippines"],
        "poland": ["republic of poland"],
        "portugal": ["portuguese republic"],
        "qatar": ["state of qatar"],
        "russia": ["russian federation"],
        "rwanda": ["rwandese republic", "republic of rwanda"],
        "saudi arabia": ["kingdom of saudi arabia", "ksa"],
        "senegal": ["republic of senegal"],
        "serbia": ["republic of serbia"],
        "sierra leone": ["republic of sierra leone", "salone"],
        "singapore": ["republic of singapore"],
        "slovakia": ["slovak republic", "sr"],
        "slovenia": ["republic of slovenia", "rs"],
        "somalia": ["federal republic of somalia"],
        "somaliland region": ["republic of somaliland"],
        "south africa": ["republic of south africa"],
        "south korea": ["republic of korea", "rok"],
        "south sudan": ["republic of south sudan"],
        "spain": ["kingdom of spain"],
        "sri lanka": ["democratic socialist republic of sri lanka"],
        "sudan": ["republic of sudan", "the sudan"],
        "suriname": ["republic of suriname", "surinam"],
        "swaziland": ["eswatini", "kingdom of eswatini"],
        "sweden": ["kingdom of sweden"],
        "switzerland": ["swiss confederation"],
        "syria": ["syrian arab republic"],
        "taiwan province of china": [
            "republic of china", "roc", "taiwan", "chinese taipei",
            "taiwan, province of china"
            ],
        "tajikistan": ["republic of tajikistan"],
        "tanzania": ["united republic of tanzania"],
        "thailand": ["kingdom of thailand"],
        "togo": ["togolese republic"],
        "trinidad and tobago": ["republic of trinidad and tobago", "trinbago"],
        "tunisia": ["republic of tunisia"],
        "turkey": ["republic of turkey"],
        "turkmenistan": ["turkmenia"],
        "uganda": ["republic of uganda"],
        "united arab emirates": ["uae", "the emirates"],
        "united kingdom": [
            "uk", "great britain", "britain",
            "united kingdom of great britain and northern ireland"],
        "united states": [
            "usa", "us", "united states of america", "america",
            "north america", "the states"
            ],
        "uruguay": ["oriental republic of uruguay"],
        "uzbekistan": ["republic of uzbekistan"],
        "venezuela": ["bolivarian republic of venezuela"],
        "vietnam": ["socialist republic of vietnam"],
        "yemen": ["republic of yemen", "yemini republic"],
        "zambia": ["republic of zambia"],
        "zimbabwe": ["republic of zimbabwe"],
        }
    std_name = None
    for k, v in country_alias_list.items():
        if input_name in v:
            std_name = k
            print("in the list")
            print(f"k is {k}")
            print(f"new country variable is {std_name}")
    if std_name is None:
        std_name = input_name
    return std_name


def create_countries_dict(filepath):
    """
    Open the specified csv file, create a list of countries from 1st column
    """
    with open(filepath, "r") as f:
        data = list(csv.reader(f))
        # open the file and read it, convert to list of lists
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
        # if country only has one year, scores will be a tuple not list
        # in that case, don't need dictionary, scores_list or years list
        # so these are only created when country has multiple years
        if isinstance(self.scores, list):
            self.di = dict(self.scores)
            self.scores_list = [float(v) for v in list(self.di.values())]
            self.years = [int(k) for k in list(self.di.keys())]

    def get_scores(self, choice, single):
        """
        creates dictionary of the year and score from self.scores
        prints the score for the selected year
        or prints year + score for all years if all selected
        """
        if single == "y":
            print(f"There is only one year available for {self.name}")
            print(f"The score is {self.scores[1]} for {choice}")
        else:
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
        # create a list of the years corresponding to the min score
        min_years = [k for (k, v) in self.di.items() if float(v) == min_score]
        # check if just 1 year in list, change the print msg accordingly
        if len(min_years) == 1:
            print(f"This score was from the year {min_years[0]}")
        else:
            # otherwise print each year separated with the comma
            print(f"This score was from the years {min_years.split(', ')}")

    def show_max_score(self):
        max_score = max(self.scores_list)
        print(f"The maximum happiness score for {self.name} is: {max_score}")
        # create a list of the years corresponding to the max score
        max_years = [k for (k, v) in self.di.items() if float(v) == max_score]
        # check if just 1 year in list, change the print msg accordingly
        if len(max_years) == 1:
            print(f"This score was from the year {max_years[0]}")
        else:
            # otherwise print each year separated with the comma
            print(f"This score was from the years {max_years.split(', ')}")

    def show_median_score(self):
        """
        Get the median score from the scores_list, print to terminal
        """
        median_score = statistics.median(self.scores_list)
        print(f"The median happiness score for {self.name} is: {median_score}")

    def show_average_score(self):
        total_score = sum(self.scores_list)
        # total divided by length is average, rounded to 2 decimal places
        average_score = round(total_score/len(self.scores_list), 2)
        print(
            f"The average happiness score for {self.name} is: {average_score}")


def make_country(country, countries_dict):
    # get scores from dictionary, to be passed when creating Class instance
    country_scores = countries_dict.get(country)
    # create instance of Country for the selected country
    c = Country(country, country_scores)
    return c


def get_years(c):
    # show the list of available years from Country class instance variable
    years = c.years
    while True:
        print(f"The years available for {c.name} are: {c.years}")
        requested_years = input(
            "Enter the year you want from this list, "
            "or type in A for all years\n")
        if requested_years == "A" or requested_years == "a":
            choice = "all years"
            break
        elif validate_years(requested_years, years):
            print("valid choice")
            choice = requested_years
            break
    print(f"thanks, you asked for {choice}")
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
        print(colored(
            f"Invalid choice: {e}. You entered '{user_input}'. Try again.\n",
            "red", attrs=["bold"]))
        return False
    try:
        int(user_input)
    except ValueError:
        print(colored(
            f"Please enter a number, you entered '{user_input}'",
            "red", attrs=["bold"]))
        return False
    try:
        if len(user_input) != 4 and len(user_input) != 1:
            raise Exception(
                f"Enter 4 numbers for a year, not {len(user_input)}. "
                f"Or enter A for all years.")
        elif len(user_input) == 4 and int(user_input) not in available_years:
            raise Exception(f"{user_input} is not in the list")
    except Exception as e:
        print(colored(
            f"Invalid choice: {e}. You entered '{user_input}'. Try again.\n",
            "red", attrs=["bold"]))
        return False
    return True


def graph_option(c):
    """
    presents option to view graph and handles repsonse
    Run show_graph method if Y, Otherwise show the next options
    Calls validate_y_n to validate the user input (converted to lowercase)
    The while loop continues until validate_y_n returns True
    """
    while True:
        graph_q = input("Do you want to view graph of this data? Y/N\n")
        graph = graph_q.lower()
        print(graph)
        if validate_y_n(graph):
            print("valid choice")
            break
    if graph == "y":
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
            raise Exception("Number is not a valid choice.")
        elif user_input != "y" and user_input != "n":
            raise Exception("You didn't enter Y or N.")
    except Exception as e:
        print(colored(
            f"Invalid choice: {e}. You entered '{user_input}'. Try again.\n",
            "red", attrs=["bold"]))
        return False
    return True


def show_options(option1, option2, option3):
    """
    shows options for user to choose next
    calls the validate_options function to check the input
    continues looping until validate_options returns True
    Then returns the option to be handled by handle_option function
    """
    while True:
        print("\nChoose the option you want next:")
        print(f"1: {option1}")
        print(f"2: {option2}")
        print(f"3: {option3}")
        option = input("Enter 1, 2, or 3 here:\n")
        if validate_options(option, 3):
            print("choice is OK")
            break
    return option


def validate_options(option, num_choices):
    """
    validate the option entered by the user in show_options. Must be 1,2, or 3.
    First check if input can be converted to an integer, Print error if not
    Next try block checks if more than one number entered, raises error
    Then check if number entered is above 3 or equals 0, raise error
    Except clause returns the errors raised in the try block
    Returns True when validated or False if error, to the
    while loop in the show_options() function
    """
    try:
        int(option)
    except ValueError:
        print(colored(
            f"Please enter a number, you entered '{option}'",
            "red", attrs=["bold"]))
        return False
    try:
        if len(option) > 1:
            raise ValueError(
                "Please enter only one number and no space or "
                f"characters, you input '{option}', which "
                f"is {len(option)} characters long")
        elif int(option) > num_choices or int(option) == 0:
            raise Exception(
                f"Number must be between 1 and {num_choices}. "
                f"You entered '{option}'")
    except (ValueError, Exception) as e:
        print(colored(
            f"Invalid choice: {e}, try again.\n", "red", attrs=["bold"]))
        return False
    return True


def handle_options(option, c, path):
    """
    Handle the option chosen from show_options
    Option 1 - if single year path, joins the 'all years path'
    Option 1 - if not single year, goes to (if coming from all years path),
    or loops back to (if already on more_data_path), start of more_data_path
    Option 2 loops back to start of the main() path, to choose new country
    Option 3 prints exit message and exits the application
    """
    if path == "single year" and option == "1":
        print("option one single path, all years for same country")
        # option1 = view all years for same country
        # join the all years path - call get_scores method,
        # then call graph_option function and handle_all_years
        c.get_scores("all years", "n")
        option = graph_option(c)
        handle_options(option, c, "all years")
    elif path != "single year" and option == "1":
        print("option one, back to min/max etc.")
        more_data_path(c)
    elif option == "2":
        print("option two, choose different country")
        main(country_dict)
    else:
        print("Thank you, exiting application...")
        print_banner_msg("Goodbye")
        exit()


def more_data_options(c):
    """
    Show the options to user for Min, Max, Median, Average or All
    """
    while True:
        print(f"Choose from the options below for {c.name}:")
        print("1: Minimum happiness score")
        print("2: Maximum happiness score")
        print("3: Median happiness score")
        print("4: Average happiness score")
        print("5: All of these (min, max, median, average)")
        more_data_choice = input(
            "Enter 1/2/3/4/5 for the option you want from this list\n")
        print(f"You chose {more_data_choice}")
        if validate_options(more_data_choice, 5):
            print("valid choice")
            break
    return more_data_choice


def handle_data_options(choice, c):
    """
    handle the choice for the more_data_options function,
    i.e. Min, Max, Median, Average or All
    """
    if choice == "1":
        # option1 - min score - show_min_score method
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
    option = show_options(MORE_DATA, DIFF_COUNTRY, EXIT_APP)
    print(option)
    handle_options(option, c, "more data")


def main(dict):
    country = get_country()
    c = make_country(country, dict)
    # if country only has one year (self.scores is a tuple not list),
    # then set choice to that yea and single year to y.
    # Otherwise, choice is chosen year
    if isinstance(c.scores, tuple):
        choice = c.scores[0]
        c.get_scores(choice, "y")
    else:
        choice = get_years(c)
        c.get_scores(choice, "n")
    # if choice of years is all, show graph option
    if choice == "all years":
        option = graph_option(c)
        handle_options(option, c, "all years")
    else:
        # if chose single year, show next options
        option = show_options(ALL_YEARS, DIFF_COUNTRY, EXIT_APP)
        handle_options(option, c, "single year")


def start():
    """
    starts the application - shows the welcome message,
    creates the country dictionary and then runs main,
    passing country dictionary (application can be
    developed further to do dictionary by year, so using
    the type of dictionary as an argument for main function)
    """
    welcome_msg()
    country_dict = create_countries_dict("data/world-happiness-report.csv")
    main(country_dict)


start()
