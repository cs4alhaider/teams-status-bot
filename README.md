# Microsoft Teams Status Bot

Automate updating your Microsoft Teams status to be available all the time with an easy configurations

- [Microsoft Teams Status Bot](#microsoft-teams-status-bot)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Author](#author)
  - [License](#license)

## Installation

1. Make sure you have `python3` and `pip` on your machine
   1. You can check if you have python3 or not by running `$ python3 --version`
   2. Also, you can check `pip` by running `$ pip3 --version`
2. Install `selenium` if not installed by running `$ pip3 install selenium`
3. Open a Terminal window to clone this repo:

```bash
$ git clone https://github.com/cs4alhaider/teams-status-bot.git
$ cd teams-status-bot
```

## Usage

Open `teams-status-bot.py` file then edit the `SETTINGS` part with your preferences

```python
# ======================================================================================== #
# ====================================== SETTINGS ======================================== #
# ======================================================================================== #


# you can get your updated driver from here: https://sites.google.com/a/chromium.org/chromedriver/downloads
driver = webdriver.Chrome("./chromedriver")

# Email
email = "REPLACE_THIS_WITH_YOUR_TEAMS_EMAIL_ADDRESS"

# Password
password = "REPLACE_THIS_WITH_YOUR_PASSWORD"

# The frequency that you want to update your status in minutes
updateEvery = 1  # => in minutes, means it will update your status ever one minute

# For how long you want to keep this running, default = 1 hour
forHours = 8  # => in hours, means it will keep the program running for 8 hours

```

After configuring the file with your preferences, now it's time to run it:

```python
$ python3 teams-status-bot.py

```

## Author

[Twitter](https://twitter.com/cs4alhaider), cs.alhaider@gmail.com

## License

teams-status-bot is available under the MIT license. See the LICENSE file for more info.
