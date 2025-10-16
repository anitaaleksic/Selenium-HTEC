from selenium.webdriver.common.by import By

validUsername = "tomsmith"
validPassword = "SuperSecretPassword!"

invalidCredentials = "invalidCredentials"

def test_valid_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys(validUsername)
    driver.find_element(By.ID, "password").send_keys(validPassword)

    #the only button on the page
    loginBtn = driver.find_element(By.TAG_NAME, 'button')
    loginBtn.click()

    successEl = driver.find_element(By.ID, "flash")
    assert "You logged into a secure area!" in successEl.text

def test_invalid_login(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys(invalidCredentials)
    driver.find_element(By.ID, "password").send_keys(invalidCredentials)

    loginBtn = driver.find_element(By.TAG_NAME, 'button')
    loginBtn.click()

    errorEl = driver.find_element(By.ID, "flash")
    assert errorEl.is_displayed(), "There should be an error message"

def test_invalid_username(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys(invalidCredentials)
    driver.find_element(By.ID, "password").send_keys(validPassword)

    loginBtn = driver.find_element(By.TAG_NAME, 'button')
    loginBtn.click()

    errorEl = driver.find_element(By.ID, "flash")
    assert errorEl.is_displayed(), "There should be an error message"
    assert "Your username is invalid!" in errorEl.text, "Error message not valid"


def test_invalid_password(driver):
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys(validUsername)
    driver.find_element(By.ID, "password").send_keys(invalidCredentials)

    loginBtn = driver.find_element(By.TAG_NAME, 'button')
    loginBtn.click()

    errorEl = driver.find_element(By.ID, "flash")
    assert errorEl.is_displayed(), "There should be an error message"
    assert "Your password is invalid!" in errorEl.text, "Error message not valid"



