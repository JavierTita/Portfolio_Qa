import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.fixture
def page():
    with sync_playwright() as p:
        browser=p.chromium.launch(headless=False)
        page=browser.new_page()
        yield page
        browser.close()
        
def test_sucesslogin(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name","standard_user")
    page.fill("#password","secret_sauce")
    page.click("#login-button")
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")

def test_emptyfields(page):
    page.goto("https://www.saucedemo.com/")
    page.click("#login-button")
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Username is required")


def test_emptyusername(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#password","secret_sauce")
    page.click("#login-button")
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Username is required")

def test_emptypassword(page):
    page.goto("https://www.saucedemo.com/")
    page.fill("#user-name","standard_user")
    page.click("#login-button")
    expect(page.locator("[data-test=\"error\"]")).to_be_visible()
    expect(page.locator("[data-test=\"error\"]")).to_contain_text("Epic sadface: Password is required")

