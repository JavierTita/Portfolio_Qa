# Playwright - SauceDemo Test Suite

Automated test suite for [SauceDemo](https://www.saucedemo.com) built with Playwright and Python.

## Tests

| Test | Description |
|------|-------------|
| `test_login` | Navigates to SauceDemo, logs in with valid credentials and verifies redirect to inventory page |
| `test_checkout` | Full purchase flow — logs in, selects Sauce Labs Backpack, adds to cart, completes checkout and validates order confirmation |

## Tech stack

- Python 3.11
- Playwright
- pytest

## Setup

1. Clone the repository
```bash
git clone https://github.com/JavierTita/Portfolio_Qa.git
cd Portfolio_Qa/playwright
```

2. Create and activate virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate  # Windows
```

3. Install dependencies
```bash
pip install playwright pytest-playwright
playwright install
```

4. Run tests
```bash
pytest test_saucedemo.py
```

## Test credentials

Uses the standard SauceDemo test account:
- **Username:** `standard_user`
- **Password:** `secret_sauce`

## Selenium vs Playwright

This project replicates the same test suite available in the `selenium/` folder, allowing a direct comparison between both frameworks.

| | Selenium | Playwright |
|---|---|---|
| Driver setup | Manual via webdriver-manager | Automatic |
| Waits | Explicit WebDriverWait required | Built-in auto-waiting |
| Lines of code | ~50 | ~30 |
| Browser launch | ChromeOptions + Service | `p.chromium.launch()` |
