from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def test_login_success():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5500/labs/lab04/login.html")  # đường dẫn form login của bạn
    driver.find_element(By.ID, "username").send_keys("admin")
    driver.find_element(By.ID, "password").send_keys("1234")
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(1)
    assert "Welcome" in driver.page_source
    driver.quit()

def test_login_fail():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5500/labs/lab04/login.html")
    driver.find_element(By.ID, "username").send_keys("wrong")
    driver.find_element(By.ID, "password").send_keys("9999")
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(1)
    assert "Invalid" in driver.page_source
    driver.quit()

def test_login_empty():
    driver = webdriver.Chrome()
    driver.get("http://127.0.0.1:5500/labs/lab04/login.html")
    driver.find_element(By.ID, "loginBtn").click()
    time.sleep(1)
    assert "Please enter" in driver.page_source
    driver.quit()
