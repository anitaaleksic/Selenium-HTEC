from selenium.webdriver.common.by import By

def test_data_extraction(driver):
    driver.get("https://www.w3schools.com/html/html_tables.asp")

    table = driver.find_element(By.TAG_NAME, "table")
    rows = table.find_elements(By.TAG_NAME, "tr")
    companies = []

    for r in rows:
        try: 
            #first td element contains company name
            firstTd = r.find_element(By.TAG_NAME, "td")
            companies.append(firstTd.text)
        #because first tr doesn't have td elements
        except:
            continue
    
    assert "Island Trading" in companies, "Island Trading not found in companies table"

