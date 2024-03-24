import json
import os

from dotenv import load_dotenv

load_dotenv()


class Config:

    BASE_URL = os.getenv('BASE_URL')
    DATA_FOLDER_PATH = os.getenv('DATA_FOLDER_PATH')
    COMPANIES_DATA_FILEPATH = os.getenv('COMPANIES_DATA_FILEPATH')
    COMPANIES_LIST_FILEPATH = os.getenv('COMPANIES_LIST_FILEPATH')

    COMPANIES_LIST_HEADER = os.getenv('COMPANIES_LIST_HEADER', '').split(',')
    COMPANIES_DATA_HEADER = os.getenv('COMPANIES_DATA_HEADER', '').split(',')

    CATEGORIES_FILEPATH = os.getenv('CATEGORIES_FILEPATH')
    with open(CATEGORIES_FILEPATH) as f:
        CATEGORIES = json.load(f)
