import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
 with sync_playwright() as p:
  browser=p.chromium.launch(headless=False)
  page=browser.new_page()
  yield page
  browser.close()
  
@pytest.fixture
def logged_page(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    return page