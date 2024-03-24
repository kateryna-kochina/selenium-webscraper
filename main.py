import logging
import os

from config import Config
from scraper.data_scraper import DataScraper
from utils.folder_cleaner import clear_folder


def run_web_scraper():
    # Set up paths and URL
    data_folder_path = Config.DATA_FOLDER_PATH
    output_filepath = Config.COMPANIES_DATA_FILEPATH
    url = Config.BASE_URL

    # Create logs directory if it doesn't exist
    if not os.path.exists('logs'):
        os.makedirs('logs')
    logging.basicConfig(filename='logs/scraping_log.txt', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    logging.info(f'Starting scraping for {url}...')

    # Clear data folder before scraping
    clear_folder(data_folder_path)

    # Initialize scraper
    scraper = DataScraper()

    # Start scraping
    scraper.scrape_data()

    logging.info(
        f'Scraping completed. Results could be found by {output_filepath} path.')


if __name__ == '__main__':
    run_web_scraper()
