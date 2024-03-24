from selenium.webdriver.common.by import By

class ElementLocators:

    #################### For companies list scraping ####################
    ACCEPT_COOKIE_CSS = (
        By.CSS_SELECTOR, 'ACCEPT_COOKIE_CSS')

    NO_RESULT_MSG_CSS = (
        By.CSS_SELECTOR, 'NO_RESULT_MSG_CSS')

    CATEGORIES_CSS = (
        By.CSS_SELECTOR, 'CATEGORIES_CSS')

    SEARCH_BTN_CSS = (
        By.CSS_SELECTOR, 'SEARCH_BTN_CSS')

    COMPANIES_LIST_CSS = (
        By.CSS_SELECTOR, 'COMPANIES_LIST_CSS')

    COMPANY_TITLE_CSS = (
        By.CSS_SELECTOR, 'COMPANY_TITLE_CSS')

    COMPANY_ADDRESS_CSS = (
        By.CSS_SELECTOR, 'COMPANY_ADDRESS_CSS')

    COMPANY_POSTCODE_CSS = (
        By.CSS_SELECTOR, 'COMPANY_POSTCODE_CSS')

    COMPANY_CITY_CSS = (
        By.CSS_SELECTOR, 'COMPANY_CITY_CSS')

    PAGES_NAVIGATION_CSS = (
        By.CSS_SELECTOR, 'PAGES_NAVIGATION_CSS')

    GO_TO_LAST_PAGE_CSS = (
        By.CSS_SELECTOR, 'GO_TO_LAST_PAGE_CSS')

    #################### For companies data scraping ####################
    PHONE_NUMBER_CSS = (
        By.CSS_SELECTOR, 'PHONE_NUMBER_CSS')

    ADDRESS_CSS = (
        By.CSS_SELECTOR, 'ADDRESS_CSS')

    POSTCODE_CITY_CSS = (
        By.CSS_SELECTOR, 'POSTCODE_CITY_CSS')

    WEBSITE_CSS = (
        By.CSS_SELECTOR, 'WEBSITE_CSS')
