# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class LoggingInAndDataCheck():
  def __init__(self):
    self.email = "testresetuhasla1234@gmail.com"
    self.password = "1234"
    print()

  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test(self):
    # Test name: log_and_data
    # Step # | name | target | value | comment
    # 1 | open | / |  | 
    self.driver.get("https://89b4778d.cinema-app.pages.dev/")
    time.sleep(4)

    # 2 | mouseOver | css=.MuiButton-outlined |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-outlined")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    time.sleep(4)

    # 3 | click | css=.MuiButton-outlined |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-outlined").click()
    time.sleep(4)

    # 4 | click | id=:r0: |  | 
    self.driver.find_element(By.ID, ":r0:").click()
    time.sleep(4)

    # 5 | type | id=:r0: | self.email | 
    self.driver.find_element(By.ID, ":r0:").send_keys(self.email)
    time.sleep(4)

    # 6 | mouseOver | css=.css-no3uto |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".css-no3uto")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    time.sleep(4)

    # 7 | type | id=:r1: | self.password | 
    self.driver.find_element(By.ID, ":r1:").send_keys(self.password)
    time.sleep(2)
    print("\nLogin was successful!")
    time.sleep(2)

    # 8 | click | css=.css-no3uto |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-no3uto").click()
    time.sleep(4)

    # 9 | mouseOver | css=.css-16xxzug |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".css-16xxzug")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    time.sleep(4)

    # 10 | storeText | css=.css-16xxzug | imie_i_nazwisko | 
    self.vars["imie_i_nazwisko"] = self.driver.find_element(By.CSS_SELECTOR, ".css-16xxzug").text
    time.sleep(4)

    # 11 | mouseOver | css=.css-16xxzug |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".css-16xxzug")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    time.sleep(4)

    # 12 | click | css=.css-16xxzug |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-16xxzug").click()
    time.sleep(4)

    # 13 | click | css=.css-aqki53:nth-child(1) > .MuiTypography-root |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-aqki53:nth-child(1) > .MuiTypography-root").click()
    time.sleep(4)

    # 14 | assertText | css=.css-aqki53:nth-child(1) > .MuiTypography-root | imie_i_nazwisko1 | 
    assert self.driver.find_element(By.CSS_SELECTOR, ".css-aqki53:nth-child(1) > .MuiTypography-root").text.upper() == self.vars["imie_i_nazwisko"]
    time.sleep(2)
    print("\nName and surname match!")
    time.sleep(2)

    # 15 | click | css=.css-x0yk1z |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-x0yk1z").click()
    time.sleep(4)

    # 16 | click | css=.css-x0yk1z |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-x0yk1z").click()
    time.sleep(4)

    # 17 | assertText | css=.css-aqki53:nth-child(2) > .MuiTypography-root | email | 
    assert self.driver.find_element(By.CSS_SELECTOR, ".css-aqki53:nth-child(2) > .MuiTypography-root").text == self.email
    time.sleep(2)
    print("\nEmail match too!")
    time.sleep(2)

    # 18 | click | css=.MuiButton-outlined |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-outlined").click()
    time.sleep(2)
    print("\nLogout was successful!")
    time.sleep(2)

    # 19 | mouseOver | css=.css-q6al5w |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".css-q6al5w")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    time.sleep(4)

