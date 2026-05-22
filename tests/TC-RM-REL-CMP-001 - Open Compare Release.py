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
    page.get_by_role("heading", name="TEST_ACCTV1").click()
    page.locator("#radix-_r_1o_").click()
    page.get_by_role("menuitem", name="Compare release").click()
    expect(page.get_by_role("heading", name="Compare Release")
           ).to_have_text("Compare Release")
