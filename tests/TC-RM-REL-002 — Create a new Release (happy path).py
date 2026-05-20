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
    page.get_by_role("button", name="TEST").click()
    page.get_by_role("menuitem", name="test", exact=True).click()
    page.get_by_role("button").filter(
        has_text=re.compile(r"^$")).nth(3).click()
    page.get_by_role("textbox", name="Release Name *").click()
    page.get_by_role("textbox", name="Release Name *").fill("REL_TEST_ACCT_V1")
    page.get_by_role("combobox", name="Pipeline Environment *").click()
    page.get_by_role("option", name="GUEST-P1").click()
    page.get_by_role("textbox", name="Description *").click()
    page.get_by_role("textbox", name="Description *").fill("Release  By P")
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Release saved successfully").click()
