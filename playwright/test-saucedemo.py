import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()

def test_login(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    assert page.url == "https://www.saucedemo.com/inventory.html"

def test_checkout(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.click("//div[@data-test='inventory-item-name' and text()='Sauce Labs Backpack']")
    page.click("#add-to-cart")
    page.click(".shopping_cart_link")
    page.click("#checkout")
    page.fill("#first-name", "Javier")
    page.fill("#last-name", "Tita")
    page.fill("#postal-code", "5006")
    page.click("#continue")
    page.click("#finish")
    assert page.inner_text("h2.complete-header") == "Thank you for your order!"