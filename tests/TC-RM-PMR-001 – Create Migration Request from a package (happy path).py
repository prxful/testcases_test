import pytest
import re
from playwright.sync_api import Page, expect
from config import BASE_URL, BASE_UNAME, PASSWORD, PKG_CONFIG


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
    page.get_by_role("link", name=PKG_CONFIG).click()
    page.get_by_role("tab", name="Migration Requests").click()
    page.get_by_role("button", name="Migration Requests").click()
    page.get_by_role("combobox", name="Target Definition").click()
    page.get_by_text("C2M_Demo_2.9x TEST").click()
    page.get_by_role("button", name="Save").click()
