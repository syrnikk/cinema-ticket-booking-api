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

class DataEditing():
  def __init__(self):
    self.email = "testresetuhasla1234@gmail.com"
    self.password = "1234"
    self.phone_before = "606606606"
    self.phone_after = "123123123"
    print()

  def setup_method(self):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def test(self):
    # Test name: edit_data
    # Step # | name | target | value | comment
    # 1 | open | / |  | 
    self.driver.get("https://89b4778d.cinema-app.pages.dev/")
    time.sleep(4)

    # 2 | click | css=.MuiButton-outlined |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-outlined").click()
    time.sleep(4)

    # 3 | click | id=:r0: |  | 
    self.driver.find_element(By.ID, ":r0:").click()
    time.sleep(4)

    # 4 | type | id=:r0: | testresetuhasla1234@gmail.com | 
    self.driver.find_element(By.ID, ":r0:").send_keys(self.email)
    time.sleep(4)

    # 5 | click | id=:r1: |  | 
    self.driver.find_element(By.ID, ":r1:").click()
    time.sleep(4)

    # 6 | type | id=:r1: | 1234 | 
    self.driver.find_element(By.ID, ":r1:").send_keys(self.password)
    time.sleep(4)

    # 7 | click | css=.css-no3uto |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-no3uto").click()
    time.sleep(4)

    # 8 | click | css=.css-16xxzug |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-16xxzug").click()
    time.sleep(2)
    print("\nLogin was successful!")
    time.sleep(2)

    # 9 | click | css=.MuiBox-root:nth-child(4) > .MuiTypography-root |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiBox-root:nth-child(4) > .MuiTypography-root").click()
    time.sleep(4)

    # 10 | storeText | css=.MuiBox-root:nth-child(4) > .MuiTypography-root | phone_before | 
    self.vars["phone_before"] = self.driver.find_element(By.CSS_SELECTOR, ".MuiBox-root:nth-child(4) > .MuiTypography-root").text.replace(" ", '').replace("+48", "")
    time.sleep(4)

    # 11 | click | css=.css-ui1dqj > a:nth-child(1) > .MuiButtonBase-root |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-ui1dqj > a:nth-child(1) > .MuiButtonBase-root").click()
    time.sleep(4)

    # 12 | click | id=:r6: |  | 
    self.driver.find_element(By.ID, ":r6:").click()
    time.sleep(4)

    # 13 | assertValue | id=:r6: | 606606606 | 
    value = self.driver.find_element(By.ID, ":r6:").get_attribute("value")
    assert value == self.vars["phone_before"]
    time.sleep(4)

    # 14 | click | id=:r6: |  | 
    self.driver.find_element(By.ID, ":r6:").click()
    time.sleep(4)

    # 15 | type | id=:r6: | 123123123 | 
    self.driver.find_element(By.ID, ":r6:").send_keys(Keys.CONTROL + "a")
    self.driver.find_element(By.ID, ":r6:").send_keys(Keys.DELETE)
    self.driver.find_element(By.ID, ":r6:").send_keys(self.phone_after)
    time.sleep(4)
    
    # 16 | storeValue | id=:r6: | phone_after | 
    self.vars["phone_after"] = self.driver.find_element(By.ID, ":r6:").get_attribute("value")
    time.sleep(4)

    # 17 | mouseOver | css=.css-16769lc |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".css-16769lc")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    time.sleep(4)
    
    # 18 | click | css=.css-16769lc |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-16769lc").click()
    time.sleep(2)
    print("\nChanging the phone number was successful!")
    time.sleep(2)

    # 19 | click | css=.MuiBox-root:nth-child(4) > .MuiTypography-root |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiBox-root:nth-child(4) > .MuiTypography-root").click()
    time.sleep(4)
    
    # 20 | assertText | css=.MuiBox-root:nth-child(4) > .MuiTypography-root | +48 123 123 123 | 
    assert self.driver.find_element(By.CSS_SELECTOR, ".MuiBox-root:nth-child(4) > .MuiTypography-root").text.replace(" ", '').replace("+48", "") == self.vars["phone_after"]
    time.sleep(2)
    print("\nPhone numbers match!")
    time.sleep(2)

    # 21 | click | css=.css-ui1dqj > a:nth-child(1) > .MuiButtonBase-root |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-ui1dqj > a:nth-child(1) > .MuiButtonBase-root").click()
    time.sleep(4)

    # 22 | click | id=:rb: |  | 
    self.driver.find_element(By.ID, ":rb:").click()
    time.sleep(4)

    # 23 | click | id=:rb: |  | 
    self.driver.find_element(By.ID, ":rb:").click()
    time.sleep(4)

    # 24 | assertValue | id=:rb: | 123123123 | 
    value = self.driver.find_element(By.ID, ":rb:").get_attribute("value")
    assert value == self.vars["phone_after"]
    time.sleep(2)
    print("\nPhone numbers match!")
    time.sleep(2)

    # 25 | click | id=:rb: |  | 
    self.driver.find_element(By.ID, ":rb:").click()
    time.sleep(4)

    # 26 | click | id=:rb: |  | 
    self.driver.find_element(By.ID, ":rb:").click()
    time.sleep(4)

    # 27 | type | id=:rb: | 606606606 | 
    self.driver.find_element(By.ID, ":rb:").send_keys(Keys.CONTROL + "a")
    self.driver.find_element(By.ID, ":rb:").send_keys(Keys.DELETE)
    self.driver.find_element(By.ID, ":rb:").send_keys(self.vars["phone_before"])
    time.sleep(4)

    # 28 | click | css=.css-16769lc |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".css-16769lc").click()
    time.sleep(2)
    print("\nChanging the phone number was successful!")
    time.sleep(2)

    # 29 | click | css=.MuiBox-root:nth-child(4) > .MuiTypography-root |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiBox-root:nth-child(4) > .MuiTypography-root").click()
    time.sleep(4)

    # 30 | assertText | css=.MuiBox-root:nth-child(4) > .MuiTypography-root | +48 606 606 606 | 
    assert self.driver.find_element(By.CSS_SELECTOR, ".MuiBox-root:nth-child(4) > .MuiTypography-root").text.replace(" ", '').replace("+48", "") == self.vars["phone_before"]
    time.sleep(2)
    print("\nPhone numbers match!")
    time.sleep(2)

    # 31 | click | css=.MuiButton-outlined |  | 
    self.driver.find_element(By.CSS_SELECTOR, ".MuiButton-outlined").click()
    time.sleep(2)
    print("\nLogout was successful!")
    time.sleep(2)

    # 32 | mouseOver | css=.css-q6al5w |  | 
    element = self.driver.find_element(By.CSS_SELECTOR, ".css-q6al5w")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    time.sleep(4)



# if __name__ == "__main__":
#     sel1 = DataEditing()
#     sel1.setup_method()
#     sel1.test()
#     sel1.teardown_method()
  
