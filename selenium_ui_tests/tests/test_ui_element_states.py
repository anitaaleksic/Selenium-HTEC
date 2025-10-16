from selenium.webdriver.common.by import By

def test_home_checked(driver):
    driver.get("https://demoqa.com/checkbox")

    #find home element 
    assert driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li').is_displayed(), "Home element not visible"
    #check that element 
    homeCb = driver.find_element(By.XPATH, '//*[@id="tree-node"]/ol/li/span/label/span[1]')
    driver.execute_script("arguments[0].scrollIntoView(true);", homeCb)
    homeCb.click()

    #check if result is displayed
    result = driver.find_element(By.ID, "result")
    assert result.is_displayed(), "Result should be displayed"
    #check it displays checked items
    assert "You have selected :\nhome\ndesktop\nnotes\ncommands\ndocuments\nworkspace\nreact\nangular\nveu\noffice\npublic\nprivate\nclassified\ngeneral\ndownloads\nwordFile\nexcelFile" in result.text, "Result should contain all checked items"




