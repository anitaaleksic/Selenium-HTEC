def test_title(driver):
    driver.get("https://example.com")
    print("Page title: ", driver.title)
    assert "Example Domain" in driver.title