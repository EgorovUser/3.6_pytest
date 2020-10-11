import pytest
from selenium import webdriver

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/';

def test_guest_should_see_login_link(browser):
    browser.get(link)
    browser.implicitly_wait(5)
    button = browser.find_elements_by_css_selector('.btn-add-to-basket')
    assert len(button) > 0 ,"Элемент не найден"