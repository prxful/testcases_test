import pytest
import re
from playwright.sync_api import Page, expect
from config import BASE_URL, BASE_UNAME, PASSWORD, PKG_CONFIG, PKG_TRANS


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
    page.get_by_role("row", name=f"Select row {PKG_CONFIG}").get_by_label(
        "Select row").click()
    page.get_by_role("row", name=f"Select row {PKG_TRANS}").get_by_label(
        "Select row").click()
    page.get_by_role("button", name="Package Bulk Actions").click()
    page.get_by_role("menuitem", name="Archive Package(s)").click()
    page.get_by_role("button", name="Archive").click()
    page.get_by_text("2 package(s) archived").click()
