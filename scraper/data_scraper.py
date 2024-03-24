import logging
import time

from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from utils.csv_manager import CsvManager

from .base_scraper import BaseScraper
from ..logs.element_locators import ElementLocators as el_loc


class DataScraper(BaseScraper):
    '''Class for scraping data from web pages.'''

    def __init__(self):
        '''Initialize the DataScraper.'''
        super().__init__()

    def save_details_data_to_csv_file(self, scraped_data):
        '''Save details data to CSV file.'''
        header = self.config.COMPANIES_DATA_HEADER
        output_path = self.config.COMPANIES_DATA_FILEPATH
        CsvManager.write_to_csv(header, scraped_data, output_path)

    def save_data_to_csv_file(self, scraped_data):
        '''Save data to CSV file.'''
        header = self.config.COMPANIES_LIST_HEADER
        output_path = self.config.COMPANIES_LIST_FILEPATH
        CsvManager.write_to_csv(header, scraped_data, output_path)

    def get_categories_list(self):
        '''Get categories list.'''
        try:
            self.open_web_page(self.config.BASE_URL)
            elems = self.driver.find_elements(*el_loc.CATEGORIES_CSS)
            categories = [elem.get_attribute('value') for elem in elems]
            return categories

        except Exception as e:
            logging.error(f'Categories cannot be found, error occurred: {e}')
            return []

    def get_page_counts_by_category(self, categories):
        '''Get page counts by category.'''
        page_counts_by_category = {}

        if not categories:
            logging.warning(
                'Cannot proceed with a page count, because no categories provided.')
            return page_counts_by_category

        for category in categories:
            url = f'{self.config.BASE_URL}{category}'
            self.open_web_page(url)

            try:
                WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located(el_loc.NO_RESULT_MSG_CSS))
                page_counts_by_category[category] = None
                logging.info(
                    f'Category \'{category}\': there are no results.')

            except:
                try:
                    last_page_href = self.driver.find_element(
                        *el_loc.GO_TO_LAST_PAGE_CSS).get_attribute('href')
                    total_pages_amount = int(last_page_href.split('=')[-1])
                    page_counts_by_category[category] = total_pages_amount

                    logging.info(
                        f'Category \'{category}\': {page_counts_by_category[category]} pages.')

                except NoSuchElementException:
                    page_counts_by_category[category] = None
                    logging.error(
                        f'Category \'{category}\': failed to find last page element.')

        return page_counts_by_category

    def scrape_page(self, url, category, page_num, page_count):
        '''Scrape a page.'''
        self.open_web_page(url)
        companies = self.driver.find_elements(*el_loc.COMPANIES_LIST_CSS)
        for company in companies:
            company_link = company.get_attribute('href')
            company_title = company.find_element(
                *el_loc.COMPANY_TITLE_CSS).text
            company_address = company.find_element(
                *el_loc.COMPANY_ADDRESS_CSS).text.strip()
            company_postcode = company.find_element(
                *el_loc.COMPANY_POSTCODE_CSS).text
            company_city = company.find_element(
                *el_loc.COMPANY_CITY_CSS).text.strip()
            self.save_data_to_csv_file(
                [category, company_title, company_address, company_postcode, company_city, company_link])

        logging.info(
            f'Page {page_num}/{page_count} for {category} category is done.')

    def scrape_companies_data(self):
        '''Scrape companies data.'''
        categories = self.get_categories_list()
        if not categories:
            logging.warning(
                'Cannot proceed with a companies list scraping. No categories found.')
            return

        time.sleep(2)

        page_counts_by_category = self.get_page_counts_by_category(categories)

        try:
            for category in categories:
                logging.info(
                    f'Starting companies list scraping for {category} category...')

                page_count = page_counts_by_category.get(category)

                if page_count is not None:
                    for page_num in range(1, page_count + 1):
                        url = f'{self.config.BASE_URL}{category}page={page_num}'
                        self.scrape_page(url, category, page_num, page_count)

                logging.info(
                    f'Companies list scraping for {category} category is completed.')
                logging.info(
                    '---------------------------------------------------------------')

            return True

        except Exception as e:
            logging.error(f'Error occured: {e}')

    def scrape_company_details(self):
        '''Scrape company details.'''
        retries = 3
        for _ in range(retries):
            try:
                time.sleep(2)

                phone_number = self.find_element_text(el_loc.PHONE_NUMBER_CSS)
                website = self.find_element_text(el_loc.WEBSITE_CSS)

                return [phone_number, website]

            except TimeoutException:
                print('Timeout occurred. Retrying...')
                continue

            except Exception as e:
                print(f'An error occurred: {e}')
                break

    def process_company_data(self, company_data):
        '''Process company data.'''
        category = company_data[0]
        category_title = self.config.CATEGORIES[category]
        company_link = company_data[5]
        self.open_web_page(company_link)
        company_details = self.scrape_company_details()
        self.update_company_data(company_data, category_title, company_details)
        self.save_details_data_to_csv_file(company_data)

    def update_company_data(self, company_data, category_title, company_details):
        '''Update company data.'''
        company_data[0] = category_title
        company_data[5:7] = company_details

    def scrape_companies_details_data(self):
        '''Scrape companies details data.'''
        companies_data = CsvManager.read_csv(
            self.config.COMPANIES_LIST_FILEPATH)

        for company_data in companies_data:
            try:
                time.sleep(1)
                self.process_company_data(company_data)

            except Exception as e:
                company_title = company_data[2]
                logging.error(
                    f'Error occurred while processing: {company_title}. Error: {e}')

    def scrape_data(self):
        '''Scrape data.'''
        try:
            prep_list = self.scrape_companies_data()

            if prep_list:
                self.scrape_companies_details_data()

        finally:
            self.cleanup()
