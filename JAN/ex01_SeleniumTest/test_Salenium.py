import time

from selenium import webdriver
import allure
import pytest

@allure.title("open the app.vmo.com")
@pytest.mark.regression
def test_vmo_login():
    driver = webdriver.Edge()
    driver.get("https:/app.vwo.com")
    time.sleep(15)
