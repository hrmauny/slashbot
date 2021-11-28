# :money_with_wings: SlashBot
<hr>
<p align="center">
<a><img width=500 
  src="/docs/workflows/banner.jpg" alt="Expense tracking made easy!"></a>
</p>
<hr>

![MIT license](https://img.shields.io/badge/License-MIT-green.svg)
![GitHub](https://img.shields.io/github/languages/top/secheaper/slashbot?color=red&label=Python&logo=Python&logoColor=yellow)
![GitHub contributors](https://img.shields.io/github/contributors/secheaper/slashbot)
[![DOI](https://zenodo.org/badge/431190543.svg)](https://zenodo.org/badge/latestdoi/431190543)
[![Platform](https://img.shields.io/badge/Platform-Telegram-blue)](https://desktop.telegram.org/)
[![codecov](https://codecov.io/gh/secheaper/slashbot/branch/main/graph/badge.svg?token=YCKWZTHO7O)](https://codecov.io/gh/secheaper/slashbot)
[![Actions Status](https://github.com/mtkumar123/MyDollarBot/workflows/CI/badge.svg)](https://github.com/mtkumar123/MyDollarBot/actions)
![github workflow](https://github.com/mtkumar123/MyDollarBot/actions/workflows/black.yml/badge.svg)
![Discord](https://img.shields.io/discord/879343473940107264?color=blueviolet&label=Discord%20Discussion%20Chat)
![Lines of code](https://img.shields.io/tokei/lines/github/secheaper/slashbot?color=9cf)
![Version](https://img.shields.io/github/v/release/secheaper/slashbot?color=ff69b4&label=Version)
![GitHub issues](https://img.shields.io/github/issues-raw/secheaper/slashbot)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/secheaper/slashbot)

<hr>

## About SlashBot

SlashBot is an easy-to-use Telegram Bot that assists you in recording your daily expenses on a local system without any hassle.  
With simple commands, this bot allows you to:
- Add/Record a new spending
- Show the sum of your expenditure for the current day/month
- Display your spending history
- Clear/Erase all your records
- Edit/Change any spending details if you wish to

Check out the bot here: https://t.me/mydollarbotprod_bot

---

A demo is shown below. It is run on a local machine.

<p align="center"><img width="1000" src="./mydollar_tutorial.gif"></p>

---

# :star: Whats New

### Version 1.0.2

#### New Features:

- A calendar functionality was added so the user can specify what day a transaction was added.
- The user can now add custom categories instead of using the default categories.
- The bot server is now hosted on heroku, so users do not have to run the python file locally. Check out production bot here: https://t.me/mydollarbotprod_bot
- Visualizations can be seen using the chart command, which generates a pie chart based on user spending.
- More thorough documentation can be found on the GitHub pages.

### Version 1.0.1

#### New Features:

- Users are now able to upload a csv file containing transactions with columns “Date”, “Description”,  “Debit”, and “Date. The bot will go through each transaction in the csv file, and for transactions it has already seen before, the bot will automatically classify that transaction into the right category. For transactions, that the bot has not seen before, the bot will request the user to choose the appropriate category for that transaction.
- Consistent input and output format for all date values, and numeric values of transactions

#### For Contributors:

- Test cases have been completely written. Test cases in the bot folder are tests for functions in the bot.py, while test cases in the unit folder are for the user.py.
- Updated the documentation for all functions.
- Updated Readme.md to reflect current team working on this project.

### Version 1.0.0

#### New Features:

- Users are now able to set a budget expenditure for each category. If users exceed the budget for that category, a message it displayed reminding the user of the budget they had initially set. 
- Users are now able to delete their entire transaction history, or choose to delete just one transaction

#### For Contributors:

- Code has been refactored, and split into two main python files. Bot.py handles all the bot processing functions, and interacts with the bot handler directly. User.py handles all the backend User processing logic, and creates an object User for each individual user interacting with the bot, to maintain that user’s state. 
- Data is stored within the user object, and state is saved using a pickle object. 
- Created CI pipeline using Travis CI, and pylint to check for formatting errors, and code coverage to test for code coverage. 


<!-- [comment]: <> (## Demo) -->

<!-- [comment]: <> (https://user-images.githubusercontent.com/15325746/135395315-e234dc5e-d891-470a-b3f4-04aa1d11ed45.mp4) -->



# :rocket: Installation Guide

## 💻For developers 
1. Install Python, atleast Python3

2. Clone this repository to your local system at a suitable directory/location of your choice

3. Start a terminal session, and navigate to the directory where the repo has been cloned

4. Run the following command to install the required dependencies:
```
  pip install -r requirements.txt
```
5. Download and install the Telegram desktop application for your system from the following site: https://desktop.telegram.org/

6. Once you login to your Telegram account, search for "BotFather" in Telegram. Click on "Start" --> enter the following command:
```
  /newbot
```
7. Follow the instructions on screen and choose a name for your bot. Post this, select a username for your bot that ends with "bot" (as per the instructions on your Telegram screen)

8. BotFather will now confirm the creation of your bot and provide a TOKEN to access the HTTP API - copy this token for future use.

9. Search for "Edit the system environment variables" on your local computer. Click on Environment Variables and create a new System Variable called "API_TOKEN" and paste the token copied in step 8.

10. In the Telegram app, search for your newly created bot by entering the username and open the same. Once this is done, go back to the terminal session. Navigate to the directory containing the "bot.py" file and run the following command:
```
  python code/bot.py
```
If you get the error `ModuleNotFoundError: No module named 'code.user'; 'code' is not a package`, add the absolute path to the main project folder to python path `export PYTHONPATH="${PYTHONPATH}:/path/to/your/project/"` and try again. (You'll have to re-add if you close the terminal or add to the environment variables.)

You can also change the code `from code.user import User` to `from user import User` on line 16 of bot.py. The former is for pylint compatablity.

11. A successful run will generate a message on your terminal that says "TeleBot: Started polling." 
12. Post this, navigate to your bot on Telegram, enter the "/start" or "/menu" command, and you are all set to track your expenses!

For more info on deployment(Heroku), check out the doc [here](https://github.com/mtkumar123/MyDollarBot/blob/main/CONTRIBUTING.md#more-tips-for-developers)



# :information_desk_person: Samples

### Budget

I want to increase/decrease my monthly budget.

<p align="center"><img width="700" src="./docs/workflows/budget.gif"></p>

1. Enter the `/budget` command
2. Enter the new budget amount (must be greater than 0)


### Add

I just spent money and want to mark it as a transaction! 

<p align="center"><img width="700" src="./docs/workflows/add.gif"></p>

1. Enter the `/add` command
2. Click on the date of the transaction
3. Click on the category to add
4. Type in the amount spent

### Delete

Oh no! I entered a transaction but want to delete it! 

<p align="center"><img width="700" src="./docs/workflows/delete.gif"></p>

1. Enter the `/delete` command
2. Based on how many records you want to delete..
   1. Per day: enter the day to delete
   2. Per month: enter the month to delete
   3. All: enter All
3. The records will be display. Enter YES to confirm, or NO to cancel

### Edit

Oh no! I entered a transaction but entered the wrong category! 

<p align="center"><img width="700" src="./docs/workflows/edit.gif"></p>

1. Enter the `/edit` command
2. Specify the date, category, and value of the transaction
3. Specify what part of the transaction to edit (either date, category, or value)
4. Enter in a new value

### Adding transactions from CSV and displaying chart

I want to add transactions from a CSV my bank gave me, and visalize my spendings

<p align="center"><img width="700" src="./docs/workflows/csv_vis.gif"></p>


1. Drag the .csv file into the telegram chat, and press send
2. For each transaction, classify the category
   1. The application will remember these mappings
3. Enter the `/chart` command

### Download History

I want a CSV file of all my transactions.

<p align="center"><img width="700" src="./docs/workflows/download.gif"></p>

1. Make sure you have a transaction history.
2. Enter the `/download` command.
3. A CSV file will be sent with your history.

# :grey_question: Documentation

Thorough documentation of all methods and classes can be found at [Github Pages](https://mtkumar123.github.io/MyDollarBot/)

# :construction: Road Map

Our ideas for new features that can be implemented to make this project better can be seen in our RoadMap project board.
[Road Map](https://github.com/mtkumar123/MyDollarBot/projects/4)



:heart: Acknowledgements
---
We would like to thank Dr. Timothy Menzies for helping us understand the process of building a good Software Engineering project. We would also like to thank the teaching assistants Xiao Ling, Andre Lustosa, Kewen Peng, Weichen Shi for their support throughout the project.


:page_facing_up: License
---
This project is licensed under the terms of the MIT license. Please check [License](https://github.com/secheaper/slashbot/blob/main/LICENSE) for more details.


:sparkles: Contributors
---

<table>
  <tr>
    <td align="center"><a href="http://www.shubhammankar.com/"><img src="https://avatars.githubusercontent.com/u/29366125?v=4" width="75px;" alt=""/><br /><sub><b>Shubham Mankar</b></sub></a></td>
    <td align="center"><a href="https://github.com/pratikdevnani"><img src="https://avatars.githubusercontent.com/u/43350493?v=4" width="75px;" alt=""/><br /><sub><b>Pratik Devnani</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/moksh98"><img src="https://avatars.githubusercontent.com/u/29693765?v=4" width="75px;" alt=""/><br /><sub><b>Moksh Jain</b></sub></a><br /></td>
    <td align="center"><a href="https://rahilsarvaiya.tech/"><img src="https://avatars0.githubusercontent.com/u/32304956?v=4" width="75px;" alt=""/><br /><sub><b>Rahil Sarvaiya</b></sub></a><br /></td>
    <td align="center"><a href="https://github.com/annie0467"><img src="https://avatars.githubusercontent.com/u/17164255?v=4" width="75px;" alt=""/><br /><sub><b>Anushi Keswani</b></sub></a><br /></td>
  </tr>
</table>



# :calling: Support

For any support, email us at mydollarbot@gmail.com/ secheaper@gmail.com
