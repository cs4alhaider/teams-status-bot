#!/usr/bin/python3

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# ======================================================================================== #
# ====================================== SETTINGS ======================================== #
# ======================================================================================== #


# you can get yours updated driver from here: https://sites.google.com/a/chromium.org/chromedriver/downloads
driver = webdriver.Chrome("./chromedriver")

# Email
email = "REPLACE_THIS_WITH_YOUR_TEAMS_EMAIL_ADDRESS"

# Password
password = "REPLACE_THIS_WITH_YOUR_PASSWORD"

# The frequency that you want to update your status in minuts
updateEvery = 1  # => in minuts, means it will update your status ever one minute

# For how long you want to keep this running, default = 1 hour
forHours = 8  # => in hours, means it will keep the program running for 8 hours


# ======================================================================================== #
# ======================================== LOGIC ========================================= #
# ======================================================================================== #


def setupDriver():
    # opens MS teams web page
    driver.get("https://teams.microsoft.com/")

    # Sets a sticky timeout to implicitly wait for an element to be found,
    # or a command to complete.
    # This method only needs to be called one time per session.
    driver.implicitly_wait(45)


def findElement(xPath, _driver=driver):
    """
        Finds an element by it's xPath.

        :Args:
         - xPath: HTML xPath.
         - _driver: WebDriver

        :Usage:

            findElement(xPath="html/...")

    """
    return _driver.find_element_by_xpath(xPath)


def login(email, password):
    # getting email text box
    emailBox = findElement("/html/body/div/form[1]/div/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[2]/div/input[1]")

    # adding email address in the text box
    emailBox.send_keys(email)

    # clicking enter to continue
    emailBox.send_keys(Keys.RETURN)

    # getting the password text box element
    passwordBox = findElement("/html/body/div[2]/div[2]/div[1]/div[2]/div/div/form/div[2]/div[2]/input")

    # adding the password
    passwordBox.send_keys(password)

    # clicking enter to continue
    passwordBox.send_keys(Keys.RETURN)


def stayLoggedIn(value: bool = False):
    if value:
        saveSession = findElement("/html/body/div/form/div[1]/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[2]/input")
        saveSession.send_keys(Keys.RETURN)
    else:
        # don't stay logged in
        saveSession = findElement("/html/body/div/form/div[1]/div/div[1]/div[2]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input")
        saveSession.send_keys(Keys.RETURN)


def useTeamsOnTheWeb():
    # use MS teams on the web
    useOnWeb = findElement("/html/body/promote-desktop/div/div/div/div[1]/div[2]/div/a")
    useOnWeb.click()


def updateStatus(status: str = "/available"):
    """
        Set your profile status to whatever you pass.

        :Args:
         - status: "/available".

        :Usage:

            updateStatus(status="/available")

    """
    # select the search bar
    searchBox = findElement("/html/body/div[2]/div[1]/app-header-bar/div/power-bar/div/div/form/search-box/div/input")
    searchBox.send_keys(status)
    # select `available` from the dropdown menu
    select = findElement("/html/body/div[2]/div[1]/app-header-bar/div/power-bar/div/div/form/slash-command-box/div/slash-command-popover/div/div[2]/ul/li/div")
    select.click()


def keepUpdating(status: str = "/available", every: int = 5, hours: int = 1):
    """
        Automate updating your status with time logic.

        :Args:
         - status: "/available".
         - every: the frequency that you want to update your status
         - hours: for how long you want to keep this running, default = 1 hour 

        :Usage:

            # The below usage example will keep updating the status every 5 minuts 
            # for maxmum 8 hours then it will stop.
            keepUpdating(status="/available", every=5, hours=8)
    """
    selectedRange: int = int((hours * 60) / every)
    for _ in range(selectedRange):
        updateStatus(status)
        time.sleep(every * 60)


def runAutomation(email, password, every, hours):
    setupDriver()
    login(email, password)
    stayLoggedIn(False)
    useTeamsOnTheWeb()
    keepUpdating(every=every, hours=hours)
    # then quit the browser once done
    driver.quit()


# MAIN RUNNING POINT OF THIS APP
runAutomation(
    email=email,
    password=email,
    every=updateEvery,
    hours=forHours
)
