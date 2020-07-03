import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("D:\Downloads\chromedriver.exe")
        self.driver.get("https://www.youtube.com/")

    def test_video_list(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_match()
        mainPage.search_text = "nct 127"
        mainPage.click_search_btn()
        searchResultPage = page.SearchResultsPage(self.driver)
        assert searchResultPage.is_video_found()

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
