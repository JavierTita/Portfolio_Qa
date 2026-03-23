# Selenium - SauceDemo Test Suite

Automated test suite for [SauceDemo](https://www.saucedemo.com) built with Selenium WebDriver and Python.

## Tests

| Test | Description |
|------|-------------|
| `test_login` | Navigates to SauceDemo and logs in with valid credentials |
| `test_buttonlogin` | Verifies successful login redirects to inventory page |
| `test_checkout` | Full purchase flow — selects Sauce Labs Backpack, adds to cart, completes checkout and validates order confirmation |

## Tech stack

- Python 3.11
- Selenium WebDriver
- pytest
- WebDriver Manager

## Setup

1. Clone the repository
```bash
git clone https://github.com/JavierTita/Portfolio_Qa.git
cd Portfolio_Qa/selenium
```

2. Create and activate virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

3. Install dependencies
```bash
pip install selenium pytest webdriver-manager
```

4. Run tests
```bash
pytest saucedemo.py
```

## Test credentials

Uses the standard SauceDemo test account:
- **Username:** `standard_user`
- **Password:** `secret_sauce`

## Notes

- Chrome is launched with password manager and leak detection disabled to prevent browser popups from interrupting test execution
- Each test is independent and handles its own login
- `teardown_method` ensures the browser closes after every test regardless of result
