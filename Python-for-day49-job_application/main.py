from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

JOB_URL = "https://www.linkedin.com/"
MY_EMAIL = "smallouforme@gmail.com"
MY_PASSWORD = "078376266SMALLou"
MY_PHONE = "9024833326"
MY_JOB = "python developer"


def apply_job(driver):
    try:
        top_show_job = driver.find_element(By.CLASS_NAME, "jobs-apply-button--top-card")
        job_type = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card span")

        if job_type.text == "Easy Apply":
            top_show_job.click()
            time.sleep(5)

            tel_box = driver.find_element(By.CSS_SELECTOR, ".artdeco-text-input--container input")
            if tel_box.get_attribute("class") != "artdeco-text-input--input":
                tel_box.send_keys(MY_PHONE)
            else:
                next_button = driver.find_element(By.CSS_SELECTOR, ".display-flex button")
                time.sleep(5)
                next_button.click()

                time.sleep(5)
                next_button.click()

                # the third step should answer plenty of non-formatting questions. we should answer them manually
                time.sleep(5)
                close_discard(driver)
        else:
            pass
    except Exception as e:
        print(f"Error applying job: {str(e)}")


def close_discard(driver):
    try:
        close_button = driver.find_element(By.ID, "ember1542")
        close_button.click()

        discard_button = driver.find_element(By.ID, "ember1571")
        discard_button.click()
    except Exception as e:
        print(f"Error closing or discarding: {str(e)}")


edge_option = webdriver.EdgeOptions()
edge_option.add_experimental_option("detach", True)

edge_driver = webdriver.Edge(edge_option)

edge_driver.get(JOB_URL)

# wait a sec and login
time.sleep(5)
login = edge_driver.find_element(By.CSS_SELECTOR, ".nav__button-secondary")
login.click()

time.sleep(5)
user_box = edge_driver.find_element(By.ID, "username")
user_box.send_keys(MY_EMAIL)

password_box = edge_driver.find_element(By.ID, "password")
password_box.send_keys(MY_PASSWORD, Keys.ENTER)

# search job position
time.sleep(5)
search = edge_driver.find_element(By.CSS_SELECTOR, "#global-nav-typeahead input")
search.send_keys(MY_JOB, Keys.ENTER)

# see first page result
time.sleep(5)
job_result = edge_driver.find_element(By.CSS_SELECTOR, ".search-results__cluster-bottom-banner a")
job_result.click()

# get the whole list of the first page and click
time.sleep(5)
whole_page_job_lists = edge_driver.find_elements(By.CSS_SELECTOR, ".scaffold-layout__list-container li a")
for job_list in whole_page_job_lists:
    job_list.click()
    apply_job(edge_driver)
    edge_driver.back()  # Go back to the job list page

edge_driver.quit()


