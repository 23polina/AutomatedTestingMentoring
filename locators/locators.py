from selenium.webdriver.common.by import By

#Test case 1:
CARRIERS_LINK = (By.XPATH, "//a[@class='top-navigation__item-link js-op' and text()='Careers']")
START_YOUR_SEARCH_HERE_BUTTON = (By.XPATH, "//div[@class='pinned-button-ui-23']/child::a[contains(@href,'utm_term=start-your-search-here')]")
CLEAR_SEARCH_ICON = (By.CLASS_NAME, "Dropdown_clearIcon__5dPBR")
REMOTE_CHECKBOX = (By.XPATH, "//*[@class='Checkbox_labelElement___nzU3 Checkbox_optional__Y3Wfr' and text() = 'Remote']")
SEARCH_FIELD = (By.CSS_SELECTOR, "[aria-label='search']")
COUNTRIES_DROPDOWN = (By.XPATH, "//div[@class='Dropdown_defaultOption__pvL_3 ym-disable-keys dropdown__indicator Dropdown_defaultOption__pvL_3 ym-disable-keys dropdown__dropdown-indicator css-1xc3v61-indicatorContainer']")
ALL_COUNTRIES_FILTER = (By.XPATH, "//div[@class='Dropdown_defaultOption__pvL_3 ym-disable-keys dropdown__single-value css-1dimb5e-singleValue' and text()='All available countries']")
SEARCH_BUTTON = (By.NAME, "submit_search_box_button")
JOB_TITLE = (By.LINK_TEXT, "Presales Solution Consultant – Data and AI")

#Test case 2:
MAGNIFIER_ICON = (By.XPATH, "//*[@class='header-search__button header__icon']")
INPUT_FIELD = (By.ID, "new_form_search")
FIND_BUTTON = (By.XPATH, "//*[@class='custom-button button-text font-900 gradient-border-button large-gradient-button uppercase-text custom-search-button']")
LINK = (By.PARTIAL_LINK_TEXT, "Smarter Tokenomics Cut Costs 20%")
TEST_VERIFY_LINK = (By.XPATH, "//*[text() ='Smarter Tokenomics Cut Costs 20%, Saved £750K']")