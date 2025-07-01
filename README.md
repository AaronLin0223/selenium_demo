# Selenium Test Automation Project

This project contains automated tests for a web application using Selenium WebDriver and Python.

## Project Structure

```
selenium_demo/
├── pages/                          # Page Object Models
│   ├── base_page.py               # Base page class
│   ├── login_page.py              # Login page
│   ├── dashboard_page.py          # Dashboard page
│   ├── sidebar.py                 # Sidebar navigation
│   ├── service_catalog_page.py    # Service catalog page
│   ├── my_services_page.py        # My services page
│   ├── dhcp/                      # DHCP-related pages
│   │   ├── dhcp_page.py
│   │   ├── dhcp_list_page.py
│   │   ├── dhcp_detail_page.py
│   │   ├── add_dhcp_for_wifi_page.py
│   │   └── add_dhcp_pool_drawer.py
│   └── directory/                 # Directory server pages
│       └── add_directory_server_page.py
├── tests/                         # Test files
│   ├── conftest.py               # Pytest configuration
│   ├── test_login.py             # Login tests
│   ├── test_google.py            # Google tests
│   ├── test_dhcp_cases.py        # DHCP test cases
│   ├── check_Warning_wording_for_host_number.py
│   └── verify_num_of_host.py
├── utils/                         # Utilities and helpers
│   ├── log.py                    # Logging utilities
│   ├── R1_login.py               # Login helper
│   └── R1_UI_login_helper.py     # UI login helper
├── drivers/                       # WebDriver files
│   └── chromedriver.exe
├── assets/                        # Static assets
│   ├── style.css
│   ├── service_catalog.png
│   ├── R1_UI_login.png
│   ├── login_success.png
│   └── result.png
├── screenshots/                   # Test screenshots
├── logs/                         # Test logs
├── html_of_pages/                # HTML reference files
├── reports/                      # Test reports
│   └── report.html
├── requirements.txt              # Dependencies
└── README.md                     # This file
```

## Setup

1. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up WebDriver:**
   - ChromeDriver is included in the `drivers/` directory
   - Ensure the WebDriver path is correctly configured in your tests

## Running Tests

### Run all tests:
```bash
pytest tests/
```

### Run specific test file:
```bash
pytest tests/test_login.py
```

### Run with HTML report:
```bash
pytest tests/ --html=reports/report.html
```

### Run with verbose output:
```bash
pytest tests/ -v
```

## Test Structure

- **Page Object Model (POM):** Each page has its own class with methods for interactions
- **Base Page:** Common functionality shared across all pages
- **Test Files:** Organized by functionality (login, DHCP, etc.)
- **Utilities:** Helper functions and logging utilities

## Key Features

- **Screenshot Capture:** Automatic screenshots on test actions
- **Logging:** Comprehensive logging for debugging
- **Wait Strategies:** Explicit waits for better reliability
- **Modular Design:** Easy to maintain and extend

## Contributing

1. Follow the existing code structure
2. Add appropriate logging and screenshots
3. Update this README when adding new features
4. Ensure all tests pass before submitting changes

## Notes

- Screenshots are automatically saved to the `screenshots/` directory
- Logs are saved to the `logs/` directory
- Test reports are generated in the `reports/` directory 