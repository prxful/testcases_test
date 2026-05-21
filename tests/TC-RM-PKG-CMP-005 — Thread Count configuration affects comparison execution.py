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
    page.get_by_role("link", name="TEST_ACCT_V111").click()
    page.get_by_role("button", name="Compare Package").click()
    page.get_by_role("spinbutton").click()
    page.get_by_role("spinbutton").fill("4")
    page.get_by_role("combobox").filter(has_text="Select Environment").click()
    page.get_by_text("C2M-DEMO-29X-").click()
    page.get_by_role("button", name="Perform Comparison").click()
    page.get_by_text("Comparison job started").click()
    page.get_by_text("4").nth(1).click()
