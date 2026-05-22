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
    page.get_by_text("TEST78Deployed1 packages0").click()
    page.get_by_role("heading", name="TEST78").click()
    page.locator("#radix-_r_ll_").click()
    page.get_by_role("menuitem", name="Compare release").click()
    page.get_by_role("combobox").click()
    do_not_use = page.get_by_text("--DO NOT USE-- C2M 2.9.x")

    expect(do_not_use).to_contain_text("DO NOT USE")
    do_not_use.click()
    page.get_by_role("combobox").click()
    page.get_by_role("option", name="C2M-DEMO-29X-").click()
