from selenium.webdriver.support.ui import WebDriverWait


class InputElement(object):
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 10).until(
            lambda x: x.find_element_by_xpath(self.locator)
        )
        driver.find_element_by_xpath(self.locator).clear()
        driver.find_element_by_xpath(self.locator).send_keys(value)

    def __get__(self, obj, owner):
        driver = obj.driver
        WebDriverWait(driver, 10).until(
            lambda x: x.find_element_by_xpath(self.locator)
        )
        element = driver.find_element_by_xpath(self.locator)
        return element.get_attribute("value")
