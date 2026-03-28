import pytest
from playwright.sync_api import sync_playwright, expect

        
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

def test_logout(logged_page):
    logged_page.click("#react-burger-menu-btn")
    logged_page.click("#logout_sidebar_link")
    expect(logged_page).to_have_url("https://www.saucedemo.com/")
    expect(logged_page.locator("#login-button")).to_be_visible()

