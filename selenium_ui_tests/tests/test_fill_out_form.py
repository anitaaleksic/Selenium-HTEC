from selenium.webdriver.common.by import By
import time

def test_form(driver):
    driver.get("https://demoqa.com/text-box")
    userName = "Anita Aleksic"
    email = "anita@email.com"
    currAdd = "current address"
    permAdd = "permanent address"
    driver.find_element(By.ID, "userName").send_keys(userName)
    driver.find_element(By.ID, "userEmail").send_keys(email)
    driver.find_element(By.XPATH, '//*[@id="userForm"]//*[@id="currentAddress"]').send_keys(currAdd)
    driver.find_element(By.XPATH, '//*[@id="userForm"]//*[@id="permanentAddress"]').send_keys(permAdd)

    #can't click button because an ad is in the way 
    submit_btn = driver.find_element(By.XPATH, '//*[@id="userForm"]//*[@id="submit"]')
    driver.execute_script("arguments[0].scrollIntoView(true);", submit_btn)
    time.sleep(0.5)  # short wait just to let scroll finish
    submit_btn.click()

    #setup_driver.find_element(By.XPATH, '//*[@id="userForm"]//*[@id="submit"]').click()

    assert driver.find_element(By.ID, "output").is_displayed(), "Output element should be visible on the page!"

    assert "Name:" + userName in driver.find_element(By.ID, "name").text, "Output name doesn't match input"
    assert "Email:" + email in driver.find_element(By.ID, "email").text, "Output email doesn't match input"
    assert "Current Address :" + currAdd in driver.find_element(By.XPATH, '//*[@id="output"]//*[@id="currentAddress"]').text, "Output current address doesn't match input"
    assert "Permananet Address :" + permAdd in driver.find_element(By.XPATH, '//*[@id="output"]//*[@id="permanentAddress"]').text, "Output permanent address doesn't match input"