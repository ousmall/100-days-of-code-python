import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

Z_SEARCH_URL = "https://appbrewery.github.io/Zillow-Clone/"

FORM_URL = ("https://docs.google.com/forms/d/e/1FAIpQLScta5kYJZom9f7Dgp6dFsUJQbJYnGrjIEH0gOax3H0BrpNc5Q/viewform?usp"
            "=sf_link")

result = []


def get_list():
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/121.0.0.0 Safari/537.36",
        "accept-language": "en-US,en;q=0.5"
    }

    response = requests.get(Z_SEARCH_URL, headers)
    response.raise_for_status()

    page_content = BeautifulSoup(response.text, "html.parser")

    whole_list = page_content.select(".StyledPropertyCardDataWrapper")

    all_link = [each_list.find(attrs={"data-test": "property-card-link"}).get("href") for each_list in whole_list]
    all_address = [each_list.find(attrs={"data-test": "property-card-addr"}).get_text().replace("|", "").strip()
                   for each_list in whole_list]
    all_price = [each_list.find(attrs={"data-test": "property-card-price"}).get_text().replace("/mo", "").split("+")[0]
                 for each_list in whole_list]

    for address, price, link in zip(all_address, all_price, all_link):
        result.append(
            {
                "address": address,
                "price": price,
                "link": link
            }
        )
    return result


def write_form(entry):
    edge_option = webdriver.EdgeOptions()
    edge_option.add_experimental_option("detach", True)
    edge_driver = webdriver.Edge(options=edge_option)

    edge_driver.get(FORM_URL)

    for n in range(len(entry)):
        sleep(2)

        address_box = edge_driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

        price_box = edge_driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

        link_box = edge_driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

        submit = edge_driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

        sleep(1)
        address_box.send_keys(entry[n]["address"])
        price_box.send_keys(entry[n]["price"])
        link_box.send_keys(entry[n]["link"])

        sleep(1)
        submit.click()
        sleep(3)
        refresh = edge_driver.find_element(
            By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
        refresh.click()

    edge_driver.quit()


get_list()
write_form(result)
