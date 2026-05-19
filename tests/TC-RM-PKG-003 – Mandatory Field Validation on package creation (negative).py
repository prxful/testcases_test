import pytest
import re
from playwright.sync_api import Page, expect
from config import BASE_URL, BASE_UNAME, PASSWORD


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {"ignore_https_errors": True}


def test_example(page: Page) -> None:
    page.goto(BASE_URL)
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill(BASE_UNAME)
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("textbox", name="Password").press("Enter")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="New Package").click()
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Package Name is required").click()
    page.locator("#package-name").click()
    page.locator("#package-name").fill("AUTO_TEST_V3")
    page.get_by_role("textbox", name="Enter package description...").click()
    page.get_by_role("textbox", name="Enter package description...").fill(
        "Test Validation by Automation")
    page.locator("#package-type").click()
    page.get_by_text("Configuration", exact=True).click()
    page.locator("#package-name").click()
    page.locator("#package-name").dblclick()
    page.locator("#package-name").fill("\\")
    page.get_by_text("Package Name is required").click()
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Package Name is required").click()
    page.locator("#package-name").click()
    page.locator("#package-name").fill("AUTO_TEST_V4")
    page.get_by_role("textbox", name="Enter package description...").dblclick()
    page.get_by_role("textbox", name="Enter package description...").fill("")
    page.get_by_text("Description is required").click()
    page.get_by_role("button", name="Save").click()
