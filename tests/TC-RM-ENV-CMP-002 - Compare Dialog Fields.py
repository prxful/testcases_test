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
    page.get_by_role("button", name="Pipeline Management").click()
    page.get_by_role("link", name="Environment Definition").click()
    page.locator("div:nth-child(6) > .group > .mr-1 > .lucide").click()
    page.get_by_text("C2M-DEMO-29X-").click()
    page.locator("#radix-_r_20_").click()
    page.get_by_role("menuitem", name="Compare Config").click()
    page.get_by_role("heading", name="Config Compare Options").click()
    page.get_by_role("combobox").click()
    page.get_by_label("C2M2.9_129_ENV_DEF (C2M2.").get_by_text(
        "C2M2.9_129_ENV_DEF (C2M2.").click()
    page.get_by_role("button", name="Run Task").click()
    expect(page.get_by_text("Service task submitted")
           ).to_have_text("Service task submitted")
