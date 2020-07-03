from selenium.webdriver.common.by import By


class MainPageLocators(object):
    SEARCH_INPUT = (By.XPATH, "//input[@id='search']")
    GO_BTN = (By.ID, "search-icon-legacy")


class SearchResultsPageLocators(object):
    pass
