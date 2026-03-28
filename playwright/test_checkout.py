import pytest
from playwright.sync_api import sync_playwright, expect


def test_checkout(logged_page):
    logged_page.get_by_text("Sauce Labs Backpack").click()
    logged_page.click("#add-to-cart")
    logged_page.click("#shopping_cart_container")
    logged_page.click("#checkout")
    logged_page.fill("#first-name", "Javier")
    logged_page.fill("#last-name", "Tita")
    logged_page.fill("#postal-code", "5006")
    logged_page.click("#continue")
    logged_page.click("#finish")
    expect(logged_page.locator("[data-test=\"complete-header\"]")).to_contain_text("Thank you for your order!")