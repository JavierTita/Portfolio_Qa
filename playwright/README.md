# Playwright Automation Tests

## Test Suite - Saucedemo

### test_login.py — Login Test Suite
4 test cases covering all login scenarios:

- **test_sucesslogin** — Successful login, verifies redirect to inventory page
- **test_emptyfields** — Both fields empty, verifies error message
- **test_emptyusername** — Password filled, username empty, verifies error message
- **test_emptypassword** — Username filled, password empty, verifies error message

### test_checkout.py — Complete Purchase Flow
End-to-end test covering the full purchase process:

- Login with valid credentials
- Select product (Sauce Labs Backpack)
- Add to cart
- Proceed to checkout
- Fill personal information form
- Complete purchase
- Verify success message "Thank you for your order!"

### Tools used:
- Playwright
- Pytest
- Python
- CSS Selectors (#id, .class, [data-test])
