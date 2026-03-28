import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        yield page
        browser.close()


def test_checkout(page):
    page.goto("https://www.saucedemo.com")
    page.fill("#user-name", "standard_user")
    page.fill("#password", "secret_sauce")
    page.click("#login-button")
    page.get_by_text("Sauce Labs Backpack").click()
    page.click("#add-to-cart")
    page.click("#shopping_cart_container")
    page.click("#checkout")
    page.fill("#first-name", "Javier")
    page.fill("#last-name", "Tita")
    page.fill("#postal-code", "5006")
    page.click("#continue")
    page.click("#finish")
    expect(page.locator("[data-test=\"complete-header\"]")).to_contain_text("Thank you for your order!")