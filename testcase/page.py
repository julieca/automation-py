from locator import *
from selenium.webdriver.common.keys import Keys
from element import InputElement


class SearchTextElement(InputElement):
    locator = "//input[@id='search']"


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):
    search_text = SearchTextElement()

    def is_title_match(self):
        return "YouTube" in self.driver.title

    def click_search_btn(self):
        btn = self.driver.find_element(*MainPageLocators.GO_BTN)
        btn.click()


class SearchResultsPage(BasePage):
    def is_video_found(self):
        return True
        # contents = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.XPATH, "//div[@id='contents']"))
        # )
        # videoTitles = contents.find_elements_by_xpath(
        #     "//a[@id='video-title']//yt-formatted-string")

        # titles = map(lambda x: x.text, videoTitles)
        # return len(titles) > 0
