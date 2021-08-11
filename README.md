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
### Deployment to Heroku
### Forking the GitHub Repository
### Cloning the GitHub Repository

## Credits
---
### Code
### Content
### Media

## Acknowledgements
---
