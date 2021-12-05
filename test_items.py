import pytest
from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_localization_add_cart_button(options, browser):
    browser.get(link)
    time.sleep(30)
    try:
        browser.find_element_by_class_name("btn-add-to-basket")
        total = "true"
    except NoSuchElementException:
        total = "false"
    assert total == "true", "Add to cart button is not found"
