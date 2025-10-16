import pytest 
import time
import os
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options

# Ensure screenshot directory exists
os.makedirs("screenshots", exist_ok=True)

@pytest.fixture
def driver():
    options =  Options()
    options.add_argument("--start-maximized")
    service = Service(r"C:\Drivers\edgedriver_win64\msedgedriver.exe")
    driver = webdriver.Edge(service=service, options=options)
    yield driver
    driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # We only care about actual failing test calls
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver") 
        if driver:
            timestamp = int(time.time())
            file_name = f"screenshots/{item.name}_{timestamp}.png"
            driver.save_screenshot(file_name)
            print(f"\n Screenshot saved to: {file_name}")

