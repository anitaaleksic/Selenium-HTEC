
# Selenium UI Testing Exercises

This repository contains beginner-friendly exercises to practice UI testing using Selenium. Each exercise is designed to reinforce core concepts such as web element interaction, locators, waits, and validation.

---

## Practice Exercises

### 1. Basic Page Interaction
- **URL:** [https://example.com](https://example.com)
- **Task:** Open the page and assert the title is "Example Domain"
- **Skills Practiced:** WebDriver setup, navigation, basic assertions

---

### 2. Locate and Interact with Elements
- **URL:** [https://demoqa.com/text-box](https://demoqa.com/text-box)
- **Task:** Fill in the form using various locators (`id`, `name`, `className`, `xpath`, `cssSelector`) and submit. Validate the output.
- **Skills Practiced:** Locators, form interaction, assertions

---

### 3. Waits and Synchronization
- **URL:** [https://demoqa.com/dynamic-properties](https://demoqa.com/dynamic-properties)
- **Task:** Wait for a button to become clickable and click it.
- **Skills Practiced:** Explicit waits, `WebDriverWait`, `ExpectedConditions`

---

### 4. Table Data Extraction
- **URL:** [https://www.w3schools.com/html/html_tables.asp](https://www.w3schools.com/html/html_tables.asp)
- **Task:** Extract company names from the table and assert that "Island Trading" is present.
- **Skills Practiced:** DOM traversal, data validation

---

### 5. UI Element States
- **URL:** [https://demoqa.com/checkbox](https://demoqa.com/checkbox)
- **Task:** Verify selection state, visibility, and enablement of checkboxes.
- **Skills Practiced:** `isDisplayed()`, `isEnabled()`, `isSelected()`

---

### 6. Login Form Automation
- **URL:** [https://the-internet.herokuapp.com/login](https://the-internet.herokuapp.com/login)
- **Task:** Automate login with valid/invalid credentials and validate success/error messages.
- **Skills Practiced:** Form handling, error validation, conditional logic

---

### 7. Screenshot on Failure
- **URL:** Use any of the above (e.g., login page)
- **Task:** Intentionally fail a test and capture a screenshot.
- **Skills Practiced:** Exception handling, screenshot capture

---

### 8. Optional Additions to Deepen Learning
- Automate a small workflow across multiple pages
- Create a test suite with setup/teardown and multiple test cases
- Try to run in parallel

## Getting Started
Make sure you have the following installed:
- Python 3.x
- Selenium (`pip install selenium`)
- ChromeDriver or another browser driver

---

Happy Testing!