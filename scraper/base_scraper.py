import logging

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from config import Config


class BaseScraper:
    '''Base class for web scraping.'''

    def __init__(self):
        '''Initialize the web driver.'''
        # Set up Chrome options
        chrome_options = Options()
        chrome_options.add_argument('--disable-notifications')
        chrome_options.add_argument('--lang=fr')

        self.driver = None
        try:
            # Initialize webdriver
            self.driver = webdriver.Chrome(
                service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
        except Exception as e:
            # Log if initialization fails
            logging.error(f'Failed to initialize webdriver: {e}.')

        # Load configuration
        self.config = Config()

    def cleanup(self):
        '''Quit the web driver to clean up resources.'''
        if self.driver:
            self.driver.quit()

    def open_web_page(self, url):
        '''Open a web page in the web driver.'''
        if self.driver:
            self.driver.get(url)

    def find_element_text(self, locator):
        '''
        Find element by locator and retrieve its text.

        Args:
            locator (tuple): Locator of the element to be found.

        Returns:
            str or None: Text of the found element, or None if element not found.
        '''
        try:
            element = self.driver.find_element(*locator)
            return element.text
        except NoSuchElementException:
            # Log if element not found
            logging.warning('Element not found.')
            return None
