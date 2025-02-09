import pytest
from selenium.webdriver.common.by import By

def test_valid_login(driver):
    driver.get("https://www.saucedemo.com/")
    
    print(driver.page_source)  # הדפס את קוד ה-HTML של הדף

    # הכנסת שם משתמש וסיסמה
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")

    # לחיצה על כפתור הכניסה
    driver.find_element(By.ID, "login-button").click()

    # בדיקה שהמשתמש נכנס בהצלחה
    assert "inventory.html" in driver.current_url
