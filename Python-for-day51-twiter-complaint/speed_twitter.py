# get speed and post complaint

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import math


class TwitterBot:
    def __init__(self, account, password):
        self.down = 0
        self.up = 0
        self.account = account
        self.password = password
        self.edge_options = webdriver.EdgeOptions()
        self.edge_options.add_experimental_option("detach", True)
        self.driver = webdriver.Edge(options=self.edge_options)

    def get_internet_speed(self):
        speed_test_url = "https://www.speedtest.net/"
        self.driver.get(speed_test_url)

        # go button
        self.driver.find_element(By.CSS_SELECTOR, value='span.start-text').click()

        time.sleep(40)

        down_speed = self.driver.find_element(By.XPATH,
                                              value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                    '3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        up_speed = self.driver.find_element(By.XPATH,
                                            value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                  '3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text

        pop_up = self.driver.find_element(By.XPATH,
                                          value='//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div['
                                                '3]/div/div[8]/div/div/p[2]/button')
        if pop_up:
            pop_up.click()

        self.down = math.floor(float(down_speed))
        self.up = math.floor(float(up_speed))

    def twitter_provider(self, tweet):
        speed_test_url = "https://www.twitter.com/"
        self.driver.get(speed_test_url)

        time.sleep(2)

        sign_in = self.driver.find_element(By.XPATH,
                                           value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div['
                                                 '1]/div/div[3]/div[5]/a')
        sign_in.click()

        time.sleep(5)

        self.driver.find_element(By.XPATH,
                                 value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                       '2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(
            self.account, Keys.ENTER)

        time.sleep(2)

        self.driver.find_element(By.XPATH,
                                 value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div['
                                       '2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(
            self.password, Keys.ENTER)

        time.sleep(2)

        for i in range(10):
            time.sleep(3)
            self.driver.find_element(By.XPATH,
                                     value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div['
                                           '3]/div/div[2]/div[1]/div/div/div/div[2]/div['
                                           '1]/div/div/div/div/div/div/div/div/div/div/label/div['
                                           '1]/div/div/div/div/div/div[2]/div/div/div/div').send_keys(
                f"{tweet}({i + 1})")
            time.sleep(4)
            post = self.driver.find_element(By.CSS_SELECTOR, value='div[data-testid="tweetButtonInline"]')
            post.click()
