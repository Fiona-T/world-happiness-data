# World Happiness Data
---
*Note: this project was created for educational purposes as a student of Code Institute.*

World Happiness Data is a tool to provide requested happiness scores from the historical World Happiness datasets. It is a command line application and runs in a mock terminal provided by Code Institute.

[View the live application here.](https://world-happiness-data.herokuapp.com/) 

## Table of Contents

## Purpose
---
The [World Happiness Reports](https://worldhappiness.report/) are annual publications which interpret and draw conclusions from data collected from people in over 150 countries. 

The World Happiness Data tool is a command-line application allowing users to look up a dataset containing the happiness scores from the World Happiness Reports over the years 2005 to 2020 inclusive. For example, to look at data for a particular country so that they can see how the happiness score changed over time. 

The application provides the requested data to the user by printing it to the terminal. The application will also display a graph representing the requested data, also printed in the terminal. 

The target market is relatively broad. In general, it would be people with a passing interest in the Happiness Reports, perhaps piqued when the results are announced each year in the general news. It is not aimed at people with in depth knowledge of the Happiness Reports nor those who want to do in depth data visualisations. The usefulness of the tool lies in the ability to quickly extract information from the large dataset. 

### User’s goals:
- the users of the tool want to access the happiness scores for a country or countries, within the years 2005 - 2020 
- the user may want to view the score from a particular year, or for all years available for the chosen country
- the user may also want to view a graph representing the happiness scores over time for a country, or get more information on that country such as maximium, minimum, average scores for that country.

### Site owner’s goal:
- the goal of this tool is to provide an easy way for users to get different information from the World Happiness historical scores dataset.

## User Experience (UX)
---
### User stories
*Note:* there is no login or registered users for this application, so each user story is from the point of view of a visiting user using the application.
1. As a visiting user, I want to understand what data I can access from the application so that I know what information I can get from it
2. As a visiting user, I want to be able to choose a country so that I can view the data related to that country
3. As a visiting user, I want to see the happiness score for a particular year (from those available) for my selected country
4. As a visiting user, I want to be able to see the happiness score over time for a particular country, so that I can see the scores and trends over time for that country
5. As a visiting user, I want to be able to see a graph of the happiness score over time for a particular country so that I can visualise the data more easily
6. As a visiting user, I want to be able to see the maximum, minimum, average and median happiness score for my selected country. 
7. As a visting user, I want to be able to select one option at a time from: maximum, minimum, average and median happiness score for my selected country

### Design
*Note:* Since the application runs in the terminal, there is no design of the user interface. 

The deployed application runs in a mock terminal on Heroku in order to demonstrate the project, the design of the mock terminal is built into the template provided by Code Institute. 

### Flow Chart
[View the flowchart here](docs/flowchart.pdf), showing the steps that run in the application, how the user can move through the application and the user options at each stage. 

## Features
---
### Existing Features
- Welcome message with short note on the purpose of the application
- Option for user to view the data by the selected country
- Exception handling for the country choice 
- When a valid country is entered, show the years for which the happiness score is available for that country, since the dataset does not have a score recorded for every year for some countries. User can then choose from these years.
- Option for user to choose the year they want to view for that country, or all years
- Exception handling for the user input to the years choice input
- Option for user, if they have chosen to view all years, to choose if they want to view a graph of the data. This will be the happiness score for that country over time
- Exception handling for the user input to the Y/N choice input
- Option for user, if they originally chose a single year, to then view all years for the selected country
- Option for user to view min, max, median, average, or all of these values, for the selected country, if they chose to view all years for that country
- Option for user to go back and select another option from min, max, median, average, or all options (e.g. they chose max first time, can go back and chose min or all, etc.)
- Option for user to choose a different country, or to exit programme when they have viewed their data 
- There are five countries in the dataset that only have a score recorded for one year. If the user chooses these countries, show the score and year along with a note confirming this is the only year available, and the option to choose a different country/exit
- Exception handling for the user input to the numbered options choice inputs
- Exit message confirming to user that they are exiting the application, and how to re-run the application 

### Future Features

## Content Requirements
---
Th content required to create the project was the dataset with which the user will interact. It contains the happiness score for each country over the years 2005 - 2020 inclusive. Not every country has a score in every year, due to the way the data is collected. The [dataset was sourced from Kaggle](https://www.kaggle.com/ajaypalsinghlo/world-happiness-report-2021?select=world-happiness-report.csv).

Explanation of Happiness score:
>It is referred to as "Life Ladder" in the dataset. This is the metric used to rate happiness and is based on a "Cantril life ladder" or subjective life evaluation. Survey respondents are asked to think of a ladder, with the best possible life for them being a 10, and the worst possible life being a 0. They are then asked to state which step of the ladder they feel they are at currently. The score for each country is the national average of each respondent's answer. The other metrics such as GDP, Social Support etc. are used by the Happiness Reports to explain the Life Ladder or Happiness score.

## Technology
---
### Languages
### Frameworks, Libraries, Programmes and Tools

## Data Model
---

## Testing
---
### Code Validation
### Test Cases - user stories
### Fixed Bugs
### Manual Testing
### Supported Screens and Browsers

## Deployment
---
### Gitpod - during development
The application was developed on Gitpod, using GitHub for version control and hosting the repository. The repository for this project, and the associated workspace, was created from the [Code Institute Python Project tempate](https://github.com/Code-Institute-Org/python-essentials-template), which enables the final application to be displayed in a mock terminal once deployed to Heroku. 
-   During development, code was written in the Gitpod workspace and the application was previewed in the Terminal in Gitpod, using the command `python3 -run.py` (with `run.py` being the name of the python file containing the application code). 
- Libraries used in the application (which are then imported in the .py file) were installed by typing the relevant install command (as per library documentation) in the terminal, e.g. `pip3 install termcolor`, where termcolor is the name of the library being installed
-   Files and code were added to the staging area in Gitpod using the command `git add .` and commited using `git commit -m "commit message"`. 
-   Commited changes were then pushed to GitHub using the `git push` command.
### Deployment to Heroku
The following steps show how to deploy the application to [Heroku](https://www.heroku.com/) so that the application can be ran in the mock terminal:
>Do the following in the Gitpod workspace:
1. Go through the .py file(s) and check that every `input` has `\n`, for new line, at the end of the text inside the input. If not there, add now. This needs to be added due to a quirk in the software that creates the mock terminal, if the new line isn't added then the `input` will not appear in the mock terminal.
2. In the terminal type in the command: `pip3 freeze > requirements.txt`. This updates the requirements.txt file with the dependencies that were installed during development. Heroku will use this file to install the requirements when creating the application on Heroku.
3. Then add, commit and push these changes to GitHub using `git add <filename>` then `git commit -m "message"` then `git push`
>Do the following in Heroku:
4. In [Heroku](https://www.heroku.com/):
    - if you don't have an account, then set one up: Click the Sign up button in the header, fill out the form and Click Create Free Account when done. You will receive an email, click the link to confirm. Then you will be brought to page called SET YOUR PASSWORD. Enter password, click SET PASSWORD AND LOG IN. Will then show welcome page, click on CLICK HERE TO PROCEED, then click Accept to accept the terms of service. Then click on "Create new app"
    - if you do have an account then Sign In to your account and go to the Dashboard. Click on "New" on the top right of the screen and then "Create new app"
5. Under App name, enter the name of the application. Note: the name must be unique, so you would not be able to name it the same as the already deployed version
6. Then choose the Region and click "Create app"
7. In the list of tabs at the top of the page underneath Personal, click on the Settings tab
8. If there was a creds.json file in the application then you would update the details under the Config Vars. This is not explained here, since there is no creds.json file in the World Happiness Data application
9. Scroll down to the section called Buildpacks. This is where you indicate the dependencies needed, outside of thos in the requirements.txt file.
    - Click "Add buildpack" button
    - Select Python from the list and press "Save changes"
    - Click "Add buildpack" again, select nodejs and save. This is needed for the mock terminal code
    - Make sure they are in that order with Python on top. If not, drag to change the order
10. Now go to the Deploy section. Scroll to top of page with tabs. Click Deploy
    - Go to Deployment method and click GitHub
    - If have not connected to GitHub previously:
        - Underneath, it will show a section called Connect to GitHub, with a button at the bottom called “Connect to GitHub”. Press this button.
        - A pop up will ask you to Authorize Heroku’s access to your GitHub – click to Authorize, then enter your password and Confirm Password
        - The pop up will close and in the Connect to GitHub section it will show your GitHub username and a box to search for the repository to connect to. 
    - If have already connected to GitHub you do not need to do the above and it should show your GitHub username and a box to search for the repo name as above
    - Enter the repo-name in the box and press Search
    - Underneath, it will display the repo: `yourGitHubUsername/your-github-repo-name`, then press "Connect"
    - Once connected it will then show: Connected to `yourGitHubUsername/your-github-repo-name` by `yourGitHubUsername`
11. Underneath the Connect section, there are two options "Automatic deploys" or "Manual deploy"
    - Automatic – future pushes to GitHub will mean Heroku automatically builds a new version of the app with the pushed changes
    - Manual – the app is not automatically updated with future pushes to GitHub but these can be manually made if needed.
    - click Deploy Branch. I deployed using Manual. The logs will show the buildpacks, dependencies and requirements being installed. When done, the page will refresh and say “Your app was successfully deployed” with a View button.
12.	Click the View button to view the app – it opens in a new window
13.	The Python program automatically runs, you no longer need to type `python3 run.py` in the terminal once the application is deployed
14.	To re-start the programme from the beginning, press the RUN PROGRAM orange button at top of page

### Forking the GitHub Repository
The repository can be forked on GitHub, this creates a copy of the repository that can be viewed or amended without affecting the original repository. This can be done using the following steps:
1. Login to [GitHub](https://github.com/) 
2. Locate the relevant repository on GitHub. [This is the repository for World Happiness Data tool](https://github.com/Fiona-T/world-happiness-data).
3. At the top right of the repository (under your avatar) locate the Fork button and click this button
4. You should now have a copy of the repository in your own GitHub account, to which you can make changes
### Cloning the GitHub Repository
You can make a clone of the repository which will create a local copy on your own computer. Again you can make changes to this local copy that will not affect the original repository. Follow these steps to clone the World Happiness Data tool repository. 
1. Login to [GitHub](https://github.com/) and locate the repository as before
2. Click the button called Code, located to the left of the green Gitpod button
3. Under HTTPS copy the link provided (in this case https://github.com/Fiona-T/world-happiness-data.git) 
4. Go to Gitpod or whichever IDE you are using and open the Terminal
5. Change the current working directory to the location where you want the cloned directory to be made
6. Type `git clone` followed by the url you copied in step 3:
`git clone https://github.com/Fiona-T/world-happiness-data.git`
7. Press Enter to create the local clone

You can refer to the [GitHub documentation](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository) for more detailed information on the above process.
## Credits
---
### Code
### Content
### Media

## Acknowledgements
---
