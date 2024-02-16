from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

INSTAGRAM_URL = "https://www.instagram.com/"
THEME = "python"

# the pathways and tags change all the time, thus sometimes the code can't work


class InstaFollow:

    def __init__(self, account, password):
        self.account = account
        self.password = password
        self.edge_options = webdriver.EdgeOptions()
        self.edge_options.add_experimental_option("detach", True)
        self.driver = webdriver.Edge(options=self.edge_options)

    def login(self):
        self.driver.get(INSTAGRAM_URL)

        # for me, use FB account to log in
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="loginForm"]/div/div[5]/button'))).click()

        self.driver.find_element(By.ID, "email").send_keys(self.account)
        self.driver.find_element(By.ID, "pass").send_keys(self.password, Keys.ENTER)

        # notification open, set it later
        sleep(3)
        pop_up = self.driver.find_element(By.XPATH, "//button[contains(text(), '以后再说')]")
        if pop_up:
            pop_up.click()

    def find_followers(self):
        mian_page = f"{INSTAGRAM_URL}#reactivated/"
        self.driver.get(mian_page)

        # find search link
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="mount_0_0_et"]/div/div/div[2]/div/div/div[1]'
                       '/div[1]/div[1]/div/div/div/div/div[2]/div[2]/span/div/a'))).click()

        # enter the theme we want
        self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_et"]/div/div/div[2]/div/div/div[1]/'
                                           'div[1]/div[1]/div/div/div[2]/div/div/div[2]'
                                           '/div/div/div[1]/div/div/input').send_keys(THEME)
        # fine the first one and click
        WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="mount_0_0_et"]/div/div/div[2]/div/div/div[1]/div[1]'
                       '/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[2]/div/a[1]'))).click()

        # get follower list
        follower_window = WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable(
            (By.XPATH, '//*[@id="mount_0_0_BE"]/div/div/div[2]/div/div/div[1]'
                       '/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a')))

        follower_window.click()

        while True:
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                follower_window)

    def follow(self):
        all_buttons = self.driver.find_elements(By.CLASS_NAME, " _acan _acap _acas _aj1- _ap30")
        for button in all_buttons:
            try:
                button.click()
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()

        self.driver.quit()
