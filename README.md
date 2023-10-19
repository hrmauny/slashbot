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
[![CI](https://github.com/hrmauny/slashbot/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/hrmauny/slashbot/actions/workflows/main.yml)
[![Lint](https://github.com/hrmauny/slashbot/actions/workflows/black.yml/badge.svg?branch=main)](https://github.com/hrmauny/slashbot/actions/workflows/black.yml)
![Discord](https://img.shields.io/discord/1163591668637896807?color=blueviolet&label=Discord%20Discussion%20Chat)
![Lines of code](https://img.shields.io/tokei/lines/github/hrmauny/slashbot)
![Version](https://img.shields.io/github/v/release/hrmauny/slashbot?color=ff69b4&label=Version)
![GitHub issues](https://img.shields.io/github/issues-raw/hrmauny/slashbot)
![GitHub closed issues](https://img.shields.io/github/issues-closed-raw/hrmauny/slashbot)

<hr>

## Demo Video

https://www.youtube.com/watch?v=YLBqP0q3jUM

## About SlashBot

SlashBot is an easy-to-use Telegram Bot that assists you in recording your daily expenses on a local system without any hassle.  
With simple commands, this bot allows you to:
- Add/Record a new spending
- Show the sum of your expenditure for the current day/month
- Display your spending history
- Clear/Erase all your records
- Edit/Change any spending details if you wish to
- Download your expenditure history in the CSV format
- Visualize your spendings in the form of graphs/pie chart using the /chart option
- Email the history CSV file to yourself
- See the total daily/monthly expenditure in different currencies
- Get summary of your expenses and tips from AI
- Upload Image and CSV to add your expsenses in bulk

Check out the bot here: https://t.me/ncsuBot

---
Sample demos are shown below. They are run on a local machine.

- [:information_desk_person: Sample Demos](#information_desk_person-Sample-Demos)


---

# :star: Whats New

### Relase Version 1.2.2
- New AI Chat feature added
- New Feature to upload Image and CSV added
- New Feature to visualise montly expenditure
- New Feature to visualise weekly expenditure
- Fixed issue of CSV format in Email
- Fixed cosmetic detail issue


### Release Version 1.2.1

- See your total daily/monthly expenditure in differet currencies using the /displayDifferentCurrency command
- Download your spendings history CSV file using the /download command
- Email the monthly spendings history to yourself using the /sendEmail command
- User can now get a message when the monthly budget is exhausted.
- Details for testing requirements added in README.md


### Release Version 1.2.0

- Visualize your spendings in the form of graphs
- The User can now see his expenses across various categories in the form of graphs along with pie charts.
- Just go on adding multiple spendings using /add and type /chart to see the spendings in the form of graphs.
- More Badges added in Repository




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

10. In the Telegram app, search for your newly created bot by entering the username and open the same. Once this is done, go back to the terminal session. 
Make sure you export the PYTHONPATH variable to the main project folder
 ```
 python src/bot.py
```
11. A successful run will generate a message on your terminal that says "TeleBot: Started polling." 
12. Post this, navigate to your bot on Telegram, enter the "/start" or "/menu" command, and you are all set to track your expenses!

Notes:
If you get the error ModuleNotFoundError: No module named 'src.user'; 'src' is not a package, add the absolute path to the main project folder to python path export PYTHONPATH="${PYTHONPATH}:/path/to/your/project/" and try again. (You'll have to re-add if you close the terminal or add to the environment variables.)
You will have to install tessarect to work with Pytessarect. Also add path to tessarect in PATH variable.


## 💻For testing with Pytest
1. Some modules in testing require CHAT_ID environment variable to be set.
2. This is the specific ID that is maintained for your chat with the Bot.
3. While running the bot.py , get this id from line 72 and set it in your system environment variables.
4. This should ensure effective running of all tests.


# :information_desk_person: Sample Demos

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

### See total Expenditure in different currencies

I want to convert my total daily or monthly expenditure in a different currency.

<p align="center"><img width="700" src="./docs/workflows/currencyWorking.gif"></p>

1. Enter the /displayDifferentCurrency command
2. Choose from the category of day or month
3. Next, Choose your currency from the options
4. You will get the converted price in that currency


### Visualization in the form of graphs

I want to see my spendings in the form of graphs

<p align="center"><img width="700" src="./docs/workflows/multipleVisualizations.gif"></p>

1. Make sure you have a transaction history.
2. Enter the `/chart` command.
3. You will see multiple visualizations for your spending 

### SendEmail 

I want to send myself an email for the monthly expenditure


<p align="center"><img width="700" src="./docs/workflows/email.gif"></p>

1. Make sure you have a transaction history.
2. Enter the `/sendEmail` command.
3. Type the intended email address
4. You will get an email with the history file as attachment

### Summary 

I want to see summary and need tips on how to manage my finance based on my expense.


<p align="center"><img width="700" src="./docs/workflows/summary.gif"></p>

1. Enter the `/summary` command.
3. You will receive AI Generated response about your spendings and how you can manage budget for rest of the month.

### Adding transactions from Image

I want to add transactions from a Image my seller gave me.

<p align="center"><img width="700" src="./docs/workflows/ocr.gif"></p>


1. Enter '/Image' command
2. Upload your Image in uncompressed format.

### Weekly Analysis of Expenditure

I want to visualize my weekly expenditure.

<p align="center"><img width="700" src="./docs/workflows/weekly.gif"></p>


1. Check first if there are historical transaction using `/history`
2. Enter `/weekly` to get two line charts depicting weekly expenditure with and without categories.

### Monthly Analysis of Expenditure

I want to visualize my monthly expenditure.

<p align="center"><img width="700" src="./docs/workflows/monthly.gif"></p>


1. Check first if there are historical transaction using `/history`
2. Enter `/monthly` to get two line charts depicting monthly expenditure with and without categories.
# :grey_question: Documentation

Thorough documentation of all methods and classes can be found at [Github Pages](https://mtkumar123.github.io/MyDollarBot/)

# :construction: Road Map

Our ideas for new features that can be implemented to make this project better can be seen in our RoadMap project board.
[Road Map](https://github.com/secheaper/slashbot/projects/1)



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
