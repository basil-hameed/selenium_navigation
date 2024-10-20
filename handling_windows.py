from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.service import Service
from time import sleep

class CowinAutomation:
    dashboard_locator = '//*[@id="navbar"]/div[4]/div/div[1]/div/nav/div[3]/div/ul/li[2]/a'

    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()

    def start(self):
        self.driver.maximize_window()
        self.driver.get(self.url)
        sleep(5)

    def click_dashboard(self):
        homepage_window_handle = self.driver.current_window_handle
        print("Cowin Homepage Window ID : ", homepage_window_handle)

        # click the dashboard
        self.driver.find_element(by=By.XPATH, value=self.dashboard_locator).click()

        # fetch all the window handles
        all_window_handle = self.driver.window_handles
        print("All Window Handles : ", all_window_handle)

        # switch to window handle and close it
        for window in all_window_handle:
            if window != homepage_window_handle:
                # switching to dashboard window
                self.driver.switch_to.window(window)
                print("Switched to dashboard window")
                sleep(3)
                self.driver.close()
                print("Closed Dashboard window")
                sleep(5)
                break

    def shutdown(self):
        self.driver.quit()

cowin_url = "https://www.cowin.gov.in/"
cowin_test = CowinAutomation(cowin_url)
cowin_test.start()
cowin_test.click_dashboard()
cowin_test.shutdown()

