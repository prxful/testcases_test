import pytest
import re
from playwright.sync_api import Page, expect


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
    page.get_by_role("link", name="Search Packages").click()
    page.get_by_role("cell", name="TEST_ACCT_V111").click()
    page.get_by_role("textbox", name="Enter package name").click()
    page.get_by_role("textbox", name="Enter package name").fill(
        "TEST_ACCT_V111")
    page.get_by_role("combobox").filter(has_text="All Statuses").click()
    page.get_by_role("option", name="Pending").click()
    page.get_by_role("button", name="FIND PACKAGES").click()
    page.get_by_text("No Results Found").click()
    page.get_by_role("combobox").filter(has_text="Pending").click()
    page.get_by_role("option", name="All Statuses").click()
    page.get_by_role("button", name="FIND PACKAGES").click()
    page.get_by_text("sealed").click()
