# Playwright Automation Tests

## Test Suite - Saucedemo

### conftest.py — Fixtures
Shared fixtures available for all test files:

- **page** — launches Chromium browser and creates a new page
- **logged_page** — launches browser and performs login automatically

---

### test_login.py — Login Test Suite
5 test cases covering all login scenarios:

- **test_sucesslogin** — Successful login, verifies redirect to inventory page
- **test_emptyfields** — Both fields empty, verifies error message
- **test_emptyusername** — Password filled, username empty, verifies error message
- **test_emptypassword** — Username filled, password empty, verifies error message
- **test_logout** — Successful login and logout, verifies return to login page and login button visibility

---

### test_checkout.py — Complete Purchase Flow
End-to-end test covering the full purchase process:

- Select product (Sauce Labs Backpack)
- Add to cart
- Proceed to checkout
- Fill personal information form
- Complete purchase
- Verify success message "Thank you for your order!"

---

### test_products.py — Product Sorting
Test covering product sorting functionality:

- **test_sort** — Sort products Z to A, verifies first product is correct

---

## Tools used
- Playwright
- Pytest
- Python
- CSS Selectors (#id, .class, [data-test])
- Fixtures (conftest.py)
