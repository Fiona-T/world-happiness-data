# variables for the show_options functions in run.py
MORE_DATA = "Get more data (max, min, median, average scores) for this country"
DIFF_COUNTRY = "Choose a different country"
EXIT_APP = "Exit the application"
ALL_YEARS = "Get the score for all years for this country"
DIFF_YR = "Get the score for a different year for this country"

# dictionary of alternative names for countries that user might input
# used by convert_country_alias function in run.py
COUNTRIES_ALT_NAMES = {
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
        "bosnia and herzegovina": [
            "republic of bosnia and herzegovina", "bih", "bosnia-herzegovina",
            "bosnia"
            ],
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
        "china": ["people's republic of china", "peoples republic of china"],
        "colombia": ["republic of colombia"],
        "comoros": ["union of the comoros", "united republic of the commoros"],
        "congo (brazzaville)": [
            "republic of the congo", "congo-brazzaville", "congo brazzaville",
            "congo republic", "congo", "the congo"
            ],
        "congo (kinshasa)": [
            "democratic republic of the congo", "democratic republic of congo",
            "zaire", "congo kinshasa", "congo-kinshasa", "drc", "dr congo",
            "the drc", "the droc"
            ],
        "costa rica": ["republic of costa rica"],
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
        "hong kong s a r of china": [
            "hong kong", "hsar", "hong kong china",
            "hong kong special administrative region of china",
            "hong kong special administrative region of the people's "
            "republic of china",
            "hong kong special administrative region of the peoples "
            "republic of china",
            "hong kong sar of china", "hong kong, china"
            ],
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
        "laos": [
            "lao people's democratic republic",
            "lao peoples democratic republic"
            ],
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
