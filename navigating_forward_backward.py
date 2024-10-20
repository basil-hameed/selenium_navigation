"""
Navigating forward and backward using python selenium
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

class GuviNavigation:

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()

    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        print("URL 1 : ", self.driver.current_url)
        sleep(15)

    def shutdown(self):
        self.driver.quit()

    def click_login(self):
        self.driver.find_element(by=By.ID, value='login-btn').click()
        sleep(3)
        print("URL 2 (ClICKED THE LOGIN BUTTON) : ", self.driver.current_url)

    def move_backward(self):
        sleep(2)
        self.driver.back()
        print("URL 3 (BACK) : ", self.driver.current_url)

    def move_forward(self):
        sleep(2)
        self.driver.forward()
        print("URL 4 (FORWARD) : ", self.driver.current_url)

guvi_url = 'https://www.guvi.in/'
guvi_automation = GuviNavigation(guvi_url)
guvi_automation.start()
guvi_automation.click_login()
guvi_automation.move_backward()
guvi_automation.move_forward()
guvi_automation.shutdown()