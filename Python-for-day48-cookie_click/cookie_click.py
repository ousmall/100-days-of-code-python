from selenium import webdriver
from selenium.webdriver.common.by import By
import time

TIMEOUT = 300
CHECK_TIME = 5


def run_game():
    cookie = edge_driver.find_element(By.ID, "cookie")

    start_time = time.time()
    end_time = start_time + TIMEOUT
    check_time = start_time + CHECK_TIME
    while True:
        cookie.click()
        if time.time() > end_time:
            break
        if time.time() > check_time:
            buy_buff()
            check_time += CHECK_TIME  # check after next 5 sec


def buy_buff():
    # get cookie money(variable value, put inside)
    money = int(edge_driver.find_element(By.ID, "money").text.replace(",", ""))

    # get items' name and prices(variable value, put inside)
    buff_prices = edge_driver.find_elements(By.CSS_SELECTOR, "#store b")
    item_prices = [price.text.split("-")[1].strip().replace(",", "") for price in buff_prices if price.text != ""]

    # format items dict with price-key and id-value
    upgrades = {}
    for price, item_id in zip(item_prices, item_ids):
        upgrades[price] = {'id': item_id}

    # loop through the dict and find affordable items
    affordable_upgrades = {}
    for upgrade_cost, upgrade_id in upgrades.items():
        if money > int(upgrade_cost):
            affordable_upgrades[upgrade_cost] = upgrade_id

    # find the max one and get its key as a css-selector then click it
    affordable_id = affordable_upgrades[max(affordable_upgrades)]["id"]
    edge_driver.find_element(By.ID, f"{affordable_id}").click()


edge_driver = webdriver.Edge()

edge_driver.get("https://orteil.dashnet.org/experiments/cookie/")

"""get the whole list of upgrade items and get item ids(constant value), 
if I put them inside the buy_buff function the list will renew every time 
the function works and the code will crush because driver find an invalid id="", 
so it will stop running. Put them outside it just search once"""

item_list = edge_driver.find_elements(By.CSS_SELECTOR, "#store div")
item_ids = [item.get_attribute("id") for item in item_list]

run_game()

cps = edge_driver.find_element(By.ID, "cps").text
print(cps)

edge_driver.quit()