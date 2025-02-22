from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.base import Base

"""
This module contains all polkadot needed utils.
"""

class PolkaPage:
  
  polka_understand = (By.XPATH ,'//*[@id="root"]/main/div[4]/button')
  polka_allow = (By.XPATH ,'//*[@id="root"]/main/div[1]/div[2]/div/button')
  polka_addAccount_icon = (By.XPATH ,'//*[@id="root"]/main/div[1]/div/div[2]/div[1]')
  polka_add_account = (By.XPATH ,'//*[@id="root"]/main/div[1]/div/div[3]/div[1]/a')
  polka_checkbox = (By.XPATH ,'//*[@id="root"]/main/div[6]/label/span')
  polka_next_step = (By.XPATH ,'//*[@id="root"]/main/div[7]/button')
  polka_user_name = (By.XPATH ,'//*[@id="root"]/main/div[4]/div/input')
  polka_user_pass = (By.XPATH ,'//*[@id="root"]/main/div[5]/div/input')
  polka_user_repass = (By.XPATH ,'//*[@id="root"]/main/div[6]/div/input')
  polka_submit = (By.XPATH ,'//*[@id="root"]/main/div[8]/button[2]')
  polka_auth_pass = (By.XPATH ,'//*[@id="root"]/main/div[3]/div[1]/div/input')
  polka_auth_submit = (By.XPATH ,'//*[@id="root"]/main/div[3]/button/div[1]')

  def __init__(self, browser):
    self.browser = browser
    
  def authenticate(self):
    WebDriverWait(self.browser, 20).until(EC.number_of_windows_to_be(2))
    self.browser.switch_to.window(self.browser.window_handles[1])
    self.browser.find_element(*self.polka_understand).click()
    self.browser.find_element(*self.polka_allow).click()
    self.browser.switch_to.window(self.browser.window_handles[0])
  
  def add_account(self, name, password):
    self.browser.execute_script("window.open('');")
    self.browser.switch_to.window(self.browser.window_handles[1])
    self.browser.get(Base.extension_url)
    self.browser.find_element(*self.polka_addAccount_icon).click()
    self.browser.find_element(*self.polka_add_account).click()
    self.browser.find_element(*self.polka_checkbox).click()
    self.browser.find_element(*self.polka_next_step).click()
    self.browser.find_element(*self.polka_user_name).send_keys(name)
    self.browser.find_element(*self.polka_user_pass).send_keys(password)
    self.browser.find_element(*self.polka_user_repass).send_keys(password)
    self.browser.find_element(*self.polka_submit).click()
    self.browser.close()
    self.browser.switch_to.window(self.browser.window_handles[0])

  def AuthenticateWithPass(self, Pass):
    WebDriverWait(self.browser, 20).until(EC.number_of_windows_to_be(2))
    self.browser.switch_to.window(self.browser.window_handles[1])
    self.browser.find_element(*self.polka_auth_pass).send_keys(Pass)
    self.browser.find_element(*self.polka_auth_submit).click()
    self.browser.switch_to.window(self.browser.window_handles[0])