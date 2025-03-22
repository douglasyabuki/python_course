# type: ignore
# Selenium - Automating browser tasks
from pathlib import Path
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# Chrome command-line options:
# https://peter.sh/experiments/chromium-command-line-switches/
# Selenium documentation:
# https://selenium-python.readthedocs.io/locating-elements.html

# Path to the project root directory
ROOT_FOLDER = Path(__file__).parent
# Path to the chromedriver executable
CHROME_DRIVER_PATH = ROOT_FOLDER / 'drivers' / 'chromedriver.exe' #.exe for windowss


def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 10

    # Example options:
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    # Navigating to Google
    browser.get('https://www.google.com')

    # Wait until the input element is available
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )
    search_input.send_keys('Hello World!')
    search_input.send_keys(Keys.ENTER)

    # # Find search results by ID and then all 'a' tags within
    # results = browser.find_element(By.ID, 'search')
    # links = results.find_elements(By.TAG_NAME, 'a')

    # # Click the first link in the results
    # links[0].click()

    # Wait 10 seconds before closing
    sleep(TIME_TO_WAIT)
