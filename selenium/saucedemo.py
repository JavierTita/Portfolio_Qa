from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import pytest

class TestSauce:

  def setup_method(self):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })
    options.add_argument("--disable-features=PasswordLeakDetection")
    def setup_method(self):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    })
    options.add_argument("--disable-features=PasswordLeakDetection")
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    self.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    self.driver.maximize_window()
    self.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    self.driver.maximize_window()
    

  def test_login(self):
      self.driver.get("https://www.saucedemo.com")
      self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
      self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
      self.driver.find_element(By.ID,"login-button").click()
  def test_buttonlogin(self):
       self.test_login()
       assert self.driver.current_url==("https://www.saucedemo.com/inventory.html") 
  def test_checkout(self):
      self.test_login()       
      self.driver.find_element (By.XPATH, "//div[@data-test='inventory-item-name' and text()='Sauce Labs Backpack']").click()
      self.driver.find_element (By.ID, "add-to-cart").click()
      self.driver.find_element (By.XPATH, "//a[@class='shopping_cart_link']").click()
      self.driver.find_element (By.ID, "checkout").click()
      self.driver.find_element (By.ID, "first-name").send_keys("javi")
      self.driver.find_element (By.ID, "last-name").send_keys("tita")
      self.driver.find_element (By.ID, "postal-code").send_keys("5006")
      self.driver.find_element (By.ID, "continue").click()
      self.driver.find_element (By.ID, "finish").click()
      assert self.driver.find_element(By.XPATH, "//h2[@class='complete-header']").text == "Thank you for your order!"
      
   
  def teardown_method(self):
        if self.driver is not None:
            self.driver.quit()
