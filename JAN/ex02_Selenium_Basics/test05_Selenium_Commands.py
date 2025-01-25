from selenium import webdriver
import pytest
import allure

@allure.title("Verify that the title of vwo.com is expected.")
def test_vmo_sample():
    driver = webdriver.Edge()
    driver.get("https://app.vwo.com")
    print(driver.title)
    print(driver.current_url)
    print(driver.page_source)

