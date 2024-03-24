# Selenium Web Scraper

This project is a web scraper specifically designed to collect data from a website. It scrapes information about companies listed on the website, such as their names, addresses, and contact details.

## Overview

The web scraper is implemented in Python and utilizes the Selenium library for web automation. It navigates through the website, collects relevant data, and saves it to CSV files for further analysis.

## Installation

1. Clone the repository to your local machine:

`git clone selenium-webscraper`

2. Install the required dependencies:

`pip install -r requirements.txt`

3. Make sure you have the Chrome browser installed.

## Usage

1. Run the `main.py` script to start scraping data from the website.

`python main.py`

2. The scraper will start collecting data and save it to CSV files located in the `data/` directory.

## Project Structure

-   `config.py`: Contains configuration settings for the scraper.
-   `utils/`: Directory containing utility functions used in the project.
-   `folder_cleaner.py`: Utility to clear contents of a folder.
-   `csv_manager.py`: Utility to read from and write to CSV files.
-   `scraper/`: Directory containing the main scraping functionalities.
-   `base_scraper.py`: Base class for web scraping.
-   `data_scraper.py`: Class for scraping data from web pages.
-   `element_locators.py`: Locators for various elements on the website.
-   `logs/`: Directory to store log files generated during scraping.

## Configuration

-   `BASE_URL`: Base URL of the website to scrape.
-   `DATA_FOLDER_PATH`: Path to the directory where scraped data will be stored.
-   `COMPANIES_DATA_FILEPATH`: Path to the CSV file where company details will be saved.
-   `COMPANIES_LIST_FILEPATH`: Path to the CSV file where list of companies will be saved.
-   `COMPANIES_LIST_HEADER`: Header for the companies list CSV file.
-   `COMPANIES_DATA_HEADER`: Header for the company details CSV file.
-   `CATEGORIES`: Dictionary mapping category URLs to their respective names.

## Contributing

Contributions are welcome! If you encounter any issues or have suggestions for improvement, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
