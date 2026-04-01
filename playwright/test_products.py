
from playwright.sync_api import expect

def test_sort(logged_page):
 logged_page.locator("[data-test='product-sort-container']").select_option("za")
 expect(logged_page.locator("[data-test='inventory-item-name']").first).to_have_text("Test.allTheThings() T-Shirt (Red)")
def test_multi_cart(logged_page):
 logged_page.locator("#add-to-cart-sauce-labs-backpack").click()
 logged_page.locator("#add-to-cart-sauce-labs-bike-light").click()
 logged_page.locator("#add-to-cart-sauce-labs-bolt-t-shirt").click()
 logged_page.locator("#add-to-cart-sauce-labs-fleece-jacket").click()
 logged_page.locator("#add-to-cart-sauce-labs-onesie").click() 
 logged_page.locator("[data-test='add-to-cart-test.allthethings()-t-shirt-(red)']").click()
 expect(logged_page.locator("[data-test='shopping-cart-badge']")).to_have_text('6')

def test_price(logged_page):
    productos = [
        ("Sauce Labs Backpack", "$29.99"),
        ("Sauce Labs Bike Light", "$9.99"),
        ("Sauce Labs Bolt T-Shirt", "$15.99"),
        ("Sauce Labs Fleece Jacket", "$49.99"),
        ("Sauce Labs Onesie", "$7.99"),
        ("Test.allTheThings() T-Shirt (Red)", "$15.99"),
    ]
    for nombre, precio in productos:
        item = logged_page.locator(".inventory_item").filter(has_text=nombre)
        expect(item.locator("[data-test='inventory-item-name']")).to_have_text(nombre)
        expect(item.locator("[data-test='inventory-item-price']")).to_have_text(precio)
      
 