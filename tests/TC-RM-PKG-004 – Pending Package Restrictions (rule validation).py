import pytest
import re
from playwright.sync_api import Page, expect
from config import BASE_URL, BASE_UNAME, PASSWORD, PENDING_PKG


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {"ignore_https_errors": True}


def test_example(page: Page) -> None:
    page.goto(BASE_URL)
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill(BASE_UNAME)
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("button", name="Login").click()
    page.get_by_role("button", name="New Package").click()
    page.locator("#package-name").click()
    page.locator("#package-name").fill(PENDING_PKG)
    page.locator("#package-type").click()
    page.get_by_text("Configuration", exact=True).click()
    page.get_by_role("textbox", name="Enter package description...").click()
    page.get_by_role("textbox", name="Enter package description...").fill(
        "Test by Automation")
    page.get_by_role("button", name="Save").click()
    page.get_by_role("link", name=f"{PENDING_PKG} PENDING").click()
    page.get_by_role("link", name=f"{PENDING_PKG} PENDING").click()
    page.get_by_role("link", name="Release Manager").click()
    page.get_by_role("button", name="C2M_129").click()
    page.get_by_role("menuitem", name="test", exact=True).click()
    page.get_by_role("heading", name="REL_TEST_ACCT").click()
    page.get_by_role("textbox", name="i.e., CM.MYC.0801.V01").click()
    page.get_by_role("textbox", name="i.e., CM.MYC.0801.V01").fill(
        PENDING_PKG)
    page.get_by_text("No packages found.").click()
