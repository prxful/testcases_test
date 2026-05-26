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
    page.get_by_role("button", name="Pipeline Management").click()
    page.get_by_role("link", name="Environment Definition").click()
    page.get_by_text("C2M_Demo_2.9x", exact=True).click()
    page.get_by_role("button", name="View Details").nth(5).click()
    page.locator("#radix-_r_7m_").click()
    page.get_by_role("menuitem", name="Refresh Instance").click()
    page.get_by_role("spinbutton").click()
    page.get_by_role("spinbutton").fill("10")
