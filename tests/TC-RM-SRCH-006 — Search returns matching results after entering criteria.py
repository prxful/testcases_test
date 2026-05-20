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
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name="Search Packages").click()
    page.get_by_role("textbox", name="Enter package name").click()
    page.get_by_role("textbox", name="Enter package name").fill("ACCT_P")
    page.get_by_role("button", name="FIND PACKAGES").click()
    page.get_by_text("No Results Found").click()
