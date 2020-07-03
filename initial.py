from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

import time

PATH = "D:\Downloads\chromedriver.exe"
# driver = webdriver.Chrome(PATH)
# mobile_emulation = {"deviceName": "Nexus 5"}

# chrome_options = webdriver.ChromeOptions()

# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

# driver = webdriver.Remote(command_executor="http://127.0.0.1:4444/wd/hub",

#                           desired_capabilities=chrome_options.to_capabilities())
driver = webdriver.Remote(
    command_executor='http://127.0.0.1:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.CHROME)

driver.get("https://www.youtube.com/")
print(driver.title)

# searchBar = driver.find_element_by_xpath("//input[@id='search']")
# searchBar.send_keys("nct 127")
# searchBar.send_keys(Keys.RETURN)

# try:
#     contents = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, "//div[@id='contents']"))
#     )
#     videoTitles = contents.find_elements_by_xpath(
#         "//a[@id='video-title']//yt-formatted-string")

#     titles = map(lambda x: x.text, videoTitles)
#     print('\n'.join(titles))
# finally:
#     driver.quit()
driver.quit()
