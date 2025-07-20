# SauceDemo UI Test Suite

Automated functional UI tests for the [SauceDemo](https://www.saucedemo.com) web application, built using Python, Selenium WebDriver, and PyTest.

This project follows the Page Object Model (POM) pattern to keep tests organized, maintainable, and scalable. Each test case is also documented in a separate markdown file under the `docs` folder.

## Project Purpose

This project serves as a portfolio and practice project for developing real-world UI automation skills with a professional structure and workflow.

## Tech Stack

- Python 3.10+
- PyTest
- Selenium WebDriver
- ChromeDriver
- Page Object Model (POM) pattern

## How to Run the Tests

### 1. Clone the repository

```bash
git clone https://github.com/rastkojovic/qa-automation-saucedemo.git
cd qa-automation-saucedemo
```

### 2. Set up a virtual environment and install dependencies

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Run the tests

```bash
pytest tests/
```

## Project Structure

```
qa-automation-saucedemo/
│
├── conftest.py                   # PyTest fixture for driver setup
├── requirements.txt              # Dependencies
├── README.md
│
├── drivers/
│   └── chromedriver.exe          # ChromeDriver executable
│
├── pages/                        # Page Object Model classes
│   ├── base_page.py
│   ├── inventory_page.py
│   └── login_page.py
│
├── tests/                        # Test files
│   ├── test_add_multiple_items_to_cart.py
│   ├── test_add_single_item_to_cart.py
│   ├── test_cart_icon_updates.py
│   ├── test_inventory_page_loads.py
│   ├── test_invalid_login.py
│   ├── test_remove_item_from_cart.py
│   └── test_valid_login.py
│
└── docs/                         # Manual test cases
    ├── add_single_item_to_cart_test_case.md
    ├── cart_icon_updates_test_case.md
    ├── invalid_login_test_case.md
    ├── inventory_loads_test_case.md
    ├── login_test_case.md
    └── remove_item_test_case.md
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Author

**Rastko**
Aspiring QA Engineer and test automation developer.
