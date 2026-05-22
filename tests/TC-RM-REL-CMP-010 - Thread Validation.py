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
    page.get_by_role("link", name="Release Manager").click()
    page.get_by_role("heading", name="TEST78").click()
    page.locator("#radix-_r_2au_").click()
    page.get_by_role("menuitem", name="Compare release").click()
    page.get_by_role("spinbutton").click()
    page.get_by_role("spinbutton").press("ArrowLeft")
    page.get_by_role("spinbutton").fill("10")
    page.get_by_role("spinbutton").press("ArrowLeft")
    page.get_by_role("spinbutton").fill("0")
    expect(page.get_by_role("spinbutton")).to_have_value("1")
