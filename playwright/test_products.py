import pytest
from playwright.sync_api import sync_playwright , expect


def test_sort(logged_page):
 logged_page.locator("[data-test='product-sort-container']").select_option("za")
 expect(logged_page.locator("[data-test='inventory-item-name']").first).to_have_text("Test.allTheThings() T-Shirt (Red)")