# Selenium Test Automation Project

This project contains automated tests for a web application using Selenium WebDriver and Python.

## Project Structure

```
selenium_demo/
│   ├── R1_UI_login.png
│   ├── login_success.png
│   ├── result.png
│   ├── service_catalog.png
│   ├── style.css
│   ├── chromedriver.exe
│   ├── Sidebar.html
│   ├── add_directory_server_page.html
│   ├── test_20250527.log
│   ├── test_20250528.log
│   ├── test_20250529.log
│   ├── test_20250602.log
│   ├── test_20250611.log
│   ├── test_20250612.log
│   ├── test_20250626.log
│   ├── test_20250701.log
│   │   ├── __init__.py
│   │   ├── add_dhcp_for_wifi_page.py
│   │   ├── add_dhcp_pool_drawer.py
│   │   ├── dhcp_detail_page.py
│   │   ├── dhcp_list_page.py
│   │   ├── dhcp_page.py
│   │   ├── __init__.py
│   │   ├── add_directory_server_page.py
│   ├── __init__.py
│   ├── base_page.py
│   ├── dashboard_page.py
│   ├── dhcp/
│   ├── directory/
│   ├── login_page.py
│   ├── my_services_page.py
│   ├── new_feature_page.py
│   ├── service_catalog_page.py
│   ├── sidebar.py
│   ├── report.html
│   ├── add_DHCP for Wi-Fi_clicked_20250612_110020.png
│   ├── add_DHCP for Wi-Fi_clicked_20250612_110104.png
│   ├── add_DHCP for Wi-Fi_clicked_20250612_110231.png
│   ├── add_DHCP for Wi-Fi_clicked_20250612_110304.png
│   ├── add_DHCP for Wi-Fi_clicked_20250612_110821.png
│   ├── add_DHCP for Wi-Fi_clicked_20250612_110854.png
│   ├── add_DHCP for Wi-Fi_clicked_20250626_110829.png
│   ├── add_DHCP for Wi-Fi_clicked_20250626_110902.png
│   ├── add_DHCP for Wi-Fi_page_loaded_20250612_110021.png
│   ├── add_DHCP for Wi-Fi_page_loaded_20250612_110105.png
│   ├── add_DHCP for Wi-Fi_page_loaded_20250612_110231.png
│   ├── add_DHCP for Wi-Fi_page_loaded_20250612_110304.png
│   ├── add_DHCP for Wi-Fi_page_loaded_20250612_110821.png
│   ├── add_DHCP for Wi-Fi_page_loaded_20250612_110854.png
│   ├── add_DHCP for Wi-Fi_page_loaded_20250626_110830.png
│   ├── add_DHCP for Wi-Fi_page_loaded_20250626_110902.png
│   ├── add_dhcp_for_wifi_loaded_20250612_110021.png
│   ├── add_dhcp_for_wifi_loaded_20250612_110105.png
│   ├── add_dhcp_for_wifi_loaded_20250612_110232.png
│   ├── add_dhcp_for_wifi_loaded_20250612_110305.png
│   ├── add_dhcp_for_wifi_loaded_20250612_110822.png
│   ├── add_dhcp_for_wifi_loaded_20250612_110854.png
│   ├── add_dhcp_for_wifi_loaded_20250626_110830.png
│   ├── add_dhcp_for_wifi_loaded_20250626_110903.png
│   ├── add_dhcp_pool_drawer_loaded_20250612_110024.png
│   ├── add_dhcp_pool_drawer_loaded_20250612_110108.png
│   ├── add_dhcp_pool_drawer_loaded_20250612_110234.png
│   ├── add_dhcp_pool_drawer_loaded_20250612_110307.png
│   ├── add_dhcp_pool_drawer_loaded_20250612_110824.png
│   ├── add_dhcp_pool_drawer_loaded_20250612_110857.png
│   ├── add_dhcp_pool_drawer_loaded_20250626_110832.png
│   ├── add_dhcp_pool_drawer_loaded_20250626_110905.png
│   ├── after_click_drawer_add_20250612_110115.png
│   ├── after_click_drawer_add_20250612_110313.png
│   ├── after_click_drawer_add_20250612_110902.png
│   ├── after_click_drawer_add_20250626_110911.png
│   ├── before_click_AutoTest-DHCP_in_list_20250612_110125.png
│   ├── before_click_AutoTest-DHCP_in_list_20250612_110321.png
│   ├── before_click_AutoTest-DHCP_in_list_20250612_110911.png
│   ├── before_click_AutoTest-DHCP_in_list_20250626_110919.png
│   ├── before_click_drawer_add_20250612_110115.png
│   ├── before_click_drawer_add_20250612_110312.png
│   ├── before_click_drawer_add_20250612_110901.png
│   ├── before_click_drawer_add_20250626_110910.png
│   ├── click_DHCP for Wi-Fi_card_20250612_110120.png
│   ├── click_DHCP for Wi-Fi_card_20250612_110316.png
│   ├── click_DHCP for Wi-Fi_card_20250612_110905.png
│   ├── click_DHCP for Wi-Fi_card_20250626_110914.png
│   ├── click_add_confirm_20250612_110117.png
│   ├── click_add_confirm_20250612_110313.png
│   ├── click_add_confirm_20250612_110903.png
│   ├── click_add_confirm_20250626_110912.png
│   ├── click_add_dhcp_pool_20250612_110023.png
│   ├── click_add_dhcp_pool_20250612_110108.png
│   ├── click_add_dhcp_pool_20250612_110234.png
│   ├── click_add_dhcp_pool_20250612_110307.png
│   ├── click_add_dhcp_pool_20250612_110824.png
│   ├── click_add_dhcp_pool_20250612_110856.png
│   ├── click_add_dhcp_pool_20250626_110832.png
│   ├── click_add_dhcp_pool_20250626_110904.png
│   ├── clicked_login_20250612_110000.png
│   ├── clicked_login_20250612_110043.png
│   ├── clicked_login_20250612_110217.png
│   ├── clicked_login_20250612_110249.png
│   ├── clicked_login_20250612_110335.png
│   ├── clicked_login_20250612_110808.png
│   ├── clicked_login_20250612_110838.png
│   ├── clicked_login_20250612_110924.png
│   ├── clicked_login_20250626_110818.png
│   ├── clicked_login_20250626_110849.png
│   ├── dashboard_loaded_20250612_110013.png
│   ├── dashboard_loaded_20250612_110057.png
│   ├── dashboard_loaded_20250612_110226.png
│   ├── dashboard_loaded_20250612_110258.png
│   ├── dashboard_loaded_20250612_110345.png
│   ├── dashboard_loaded_20250612_110816.png
│   ├── dashboard_loaded_20250612_110848.png
│   ├── dashboard_loaded_20250612_110933.png
│   ├── dashboard_loaded_20250626_110826.png
│   ├── dashboard_loaded_20250626_110857.png
│   ├── dhcp_detail_page_loaded_20250612_110126.png
│   ├── dhcp_detail_page_loaded_20250612_110322.png
│   ├── dhcp_detail_page_loaded_20250612_110912.png
│   ├── dhcp_detail_page_loaded_20250626_110921.png
│   ├── dhcp_list_loaded_20250612_110120.png
│   ├── dhcp_list_loaded_20250612_110316.png
│   ├── dhcp_list_loaded_20250612_110905.png
│   ├── dhcp_list_loaded_20250626_110914.png
│   ├── entered_password_20250612_105959.png
│   ├── entered_password_20250612_110042.png
│   ├── entered_password_20250612_110217.png
│   ├── entered_password_20250612_110248.png
│   ├── entered_password_20250612_110334.png
│   ├── entered_password_20250612_110807.png
│   ├── entered_password_20250612_110838.png
│   ├── entered_password_20250612_110923.png
│   ├── entered_password_20250626_110817.png
│   ├── entered_password_20250626_110848.png
│   ├── entered_username_20250612_105958.png
│   ├── entered_username_20250612_110042.png
│   ├── entered_username_20250612_110216.png
│   ├── entered_username_20250612_110248.png
│   ├── entered_username_20250612_110334.png
│   ├── entered_username_20250612_110807.png
│   ├── entered_username_20250612_110837.png
│   ├── entered_username_20250612_110923.png
│   ├── entered_username_20250626_110817.png
│   ├── entered_username_20250626_110848.png
│   ├── fill_description_20250612_110025.png
│   ├── fill_description_20250612_110109.png
│   ├── fill_description_20250612_110235.png
│   ├── fill_description_20250612_110308.png
│   ├── fill_description_20250612_110825.png
│   ├── fill_description_20250612_110857.png
│   ├── fill_description_20250626_110833.png
│   ├── fill_description_20250626_110906.png
│   ├── fill_end_ip_20250612_110027.png
│   ├── fill_end_ip_20250612_110112.png
│   ├── fill_end_ip_20250612_110237.png
│   ├── fill_end_ip_20250612_110310.png
│   ├── fill_end_ip_20250612_110826.png
│   ├── fill_end_ip_20250612_110859.png
│   ├── fill_end_ip_20250626_110836.png
│   ├── fill_end_ip_20250626_110908.png
│   ├── fill_lease_time_20250612_110029.png
│   ├── fill_lease_time_20250612_110113.png
│   ├── fill_lease_time_20250612_110238.png
│   ├── fill_lease_time_20250612_110311.png
│   ├── fill_lease_time_20250612_110828.png
│   ├── fill_lease_time_20250612_110900.png
│   ├── fill_lease_time_20250626_110838.png
│   ├── fill_lease_time_20250626_110909.png
│   ├── fill_pool_name_20250612_110024.png
│   ├── fill_pool_name_20250612_110109.png
│   ├── fill_pool_name_20250612_110235.png
│   ├── fill_pool_name_20250612_110308.png
│   ├── fill_pool_name_20250612_110824.png
│   ├── fill_pool_name_20250612_110857.png
│   ├── fill_pool_name_20250626_110833.png
│   ├── fill_pool_name_20250626_110905.png
│   ├── fill_primary_dns_20250612_110028.png
│   ├── fill_primary_dns_20250612_110112.png
│   ├── fill_primary_dns_20250612_110237.png
│   ├── fill_primary_dns_20250612_110310.png
│   ├── fill_primary_dns_20250612_110827.png
│   ├── fill_primary_dns_20250612_110859.png
│   ├── fill_primary_dns_20250626_110837.png
│   ├── fill_primary_dns_20250626_110908.png
│   ├── fill_secondary_dns_20250612_110028.png
│   ├── fill_secondary_dns_20250612_110113.png
│   ├── fill_secondary_dns_20250612_110237.png
│   ├── fill_secondary_dns_20250612_110310.png
│   ├── fill_secondary_dns_20250612_110827.png
│   ├── fill_secondary_dns_20250612_110900.png
│   ├── fill_secondary_dns_20250626_110837.png
│   ├── fill_secondary_dns_20250626_110908.png
│   ├── fill_start_ip_20250612_110026.png
│   ├── fill_start_ip_20250612_110111.png
│   ├── fill_start_ip_20250612_110236.png
│   ├── fill_start_ip_20250612_110309.png
│   ├── fill_start_ip_20250612_110826.png
│   ├── fill_start_ip_20250612_110859.png
│   ├── fill_start_ip_20250626_110835.png
│   ├── fill_start_ip_20250626_110907.png
│   ├── fill_subnet_address_20250612_110025.png
│   ├── fill_subnet_address_20250612_110110.png
│   ├── fill_subnet_address_20250612_110235.png
│   ├── fill_subnet_address_20250612_110308.png
│   ├── fill_subnet_address_20250612_110825.png
│   ├── fill_subnet_address_20250612_110858.png
│   ├── fill_subnet_address_20250626_110834.png
│   ├── fill_subnet_address_20250626_110906.png
│   ├── fill_subnet_mask_20250612_110026.png
│   ├── fill_subnet_mask_20250612_110111.png
│   ├── fill_subnet_mask_20250612_110236.png
│   ├── fill_subnet_mask_20250612_110309.png
│   ├── fill_subnet_mask_20250612_110826.png
│   ├── fill_subnet_mask_20250612_110858.png
│   ├── fill_subnet_mask_20250626_110834.png
│   ├── fill_subnet_mask_20250626_110907.png
│   ├── fill_vlan_20250612_110030.png
│   ├── fill_vlan_20250612_110115.png
│   ├── fill_vlan_20250612_110239.png
│   ├── fill_vlan_20250612_110312.png
│   ├── fill_vlan_20250612_110828.png
│   ├── fill_vlan_20250612_110901.png
│   ├── fill_vlan_20250626_110838.png
│   ├── fill_vlan_20250626_110910.png
│   ├── my_services_loaded_20250612_110118.png
│   ├── my_services_loaded_20250612_110315.png
│   ├── my_services_loaded_20250612_110904.png
│   ├── my_services_loaded_20250626_110913.png
│   ├── my_services_page_loaded_20250612_110118.png
│   ├── my_services_page_loaded_20250612_110314.png
│   ├── my_services_page_loaded_20250612_110904.png
│   ├── my_services_page_loaded_20250626_110913.png
│   ├── open_login_page_20250612_105958.png
│   ├── open_login_page_20250612_110041.png
│   ├── open_login_page_20250612_110216.png
│   ├── open_login_page_20250612_110248.png
│   ├── open_login_page_20250612_110333.png
│   ├── open_login_page_20250612_110806.png
│   ├── open_login_page_20250612_110837.png
│   ├── open_login_page_20250612_110923.png
│   ├── open_login_page_20250626_110817.png
│   ├── open_login_page_20250626_110847.png
│   ├── select_dhcp_mode_20250612_110022.png
│   ├── select_dhcp_mode_20250612_110107.png
│   ├── select_dhcp_mode_20250612_110233.png
│   ├── select_dhcp_mode_20250612_110306.png
│   ├── select_dhcp_mode_20250612_110823.png
│   ├── select_dhcp_mode_20250612_110855.png
│   ├── select_dhcp_mode_20250626_110831.png
│   ├── select_dhcp_mode_20250626_110904.png
│   ├── service_catalog_loaded_20250612_110019.png
│   ├── service_catalog_loaded_20250612_110103.png
│   ├── service_catalog_loaded_20250612_110231.png
│   ├── service_catalog_loaded_20250612_110303.png
│   ├── service_catalog_loaded_20250612_110821.png
│   ├── service_catalog_loaded_20250612_110853.png
│   ├── service_catalog_loaded_20250626_110829.png
│   ├── service_catalog_loaded_20250626_110901.png
│   ├── service_catalog_page_loaded_20250612_110019.png
│   ├── service_catalog_page_loaded_20250612_110103.png
│   ├── service_catalog_page_loaded_20250612_110231.png
│   ├── service_catalog_page_loaded_20250612_110303.png
│   ├── service_catalog_page_loaded_20250612_110820.png
│   ├── service_catalog_page_loaded_20250612_110853.png
│   ├── service_catalog_page_loaded_20250626_110828.png
│   ├── service_catalog_page_loaded_20250626_110901.png
│   ├── set_service_name_20250612_110021.png
│   ├── set_service_name_20250612_110106.png
│   ├── set_service_name_20250612_110232.png
│   ├── set_service_name_20250612_110305.png
│   ├── set_service_name_20250612_110822.png
│   ├── set_service_name_20250612_110855.png
│   ├── set_service_name_20250626_110830.png
│   ├── set_service_name_20250626_110903.png
│   ├── switch_tab_DHCP Pool_20250612_110126.png
│   ├── switch_tab_DHCP Pool_20250612_110322.png
│   ├── switch_tab_DHCP Pool_20250612_110913.png
│   ├── switch_tab_DHCP Pool_20250626_110922.png
│   ├── __init__.py
│   ├── check_Warning_wording_for_host_number.py
│   ├── conftest.py
│   ├── test_dhcp_cases.py
│   ├── test_google.py
│   ├── test_login.py
│   ├── verify_num_of_host.py
│   ├── R1_UI_login_helper.py
│   ├── R1_login.py
│   ├── __init__.py
│   ├── log.py
│   ├── update_readme.py
├── README.md
├── assets/
├── drivers/
├── html_of_pages/
├── logs/
├── pages/
├── pytest.ini
├── reports/
├── requirements.txt
├── screenshots/
├── tests/
├── utils/
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