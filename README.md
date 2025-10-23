# Selenium-HTEC
For exercise 7 changed validUsername to be invalid so the tests would fail

Selenium UI Test Automation Feedback
====================================================

✅ What Was Done Well:
- Implemented all required tasks using Pytest.
- Used fixtures for WebDriver setup and teardown.
- Covered login scenarios, form validation, and dynamic waits.
- Screenshot capture on failure via Pytest hook.

⚠️ What Could Be Improved:
- Some assertions are tightly coupled to exact strings; consider more flexible checks.
- Minimal logging; adding logs would improve traceability.

 Suggestions for Enhancement:
- Use Page Object Model (POM) for better structure.
- Add negative test cases and edge validations.
- Implement reporting and parallel execution.
- test_home_checked method - Make sure you don't rely on multiple identifiers in one element search. 
If you concatenate multiple elements from dom tree, if something changes there are bigger chances for your code to fail. Use minimally needed, unique selectors to identify element. If needed use relative elements finding (find unique element that identify one area and the one specific selector in it)
