from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_expicit_waits(driver):
    driver.get("https://demoqa.com/dynamic-properties")

    wait = WebDriverWait(driver, 10)
    button = wait.until(EC.element_to_be_clickable((By.ID, "enableAfter")))
    driver.execute_script("arguments[0].scrollIntoView(true);", button)

    assert button.is_enabled(), "Button 'enableAfter' should be enabled" 
    button.click()

    button2 = wait.until(EC.visibility_of_element_located((By.ID, "visibleAfter")))

    assert button2.is_displayed(), "Button 'visibleAfter' should be visible"