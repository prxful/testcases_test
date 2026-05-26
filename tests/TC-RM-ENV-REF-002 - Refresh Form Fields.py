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
    page.get_by_role("button", name="Refresh").click()
    page.get_by_text("C2M_Demo_2.9x", exact=True).click()
    page.get_by_role("button", name="View Details").nth(5).click()
    page.locator("#radix-_r_20_").click()
    page.get_by_role("menuitem", name="Refresh Instance").click()
    page.get_by_role("heading", name="Data Refresh Options").click()
    page.get_by_role("combobox").filter(
        has_text="Select source environment").click()
    page.get_by_label("C2M2.9_129_ENV_DEF (C2M2.").get_by_text(
        "C2M2.9_129_ENV_DEF (C2M2.").click()
    page.get_by_text("Reset Only?").click()
    page.get_by_text("Reset On Refresh?").click()
    page.get_by_role("combobox").filter(has_text="Config Data").click()
    page.get_by_role("combobox").filter(has_text="Config Data").click()
    page.get_by_role("combobox").filter(has_text="Config Data").click()
    page.locator(".fixed.inset-0").click()
    page.get_by_role("spinbutton").click()
    page.get_by_text("Warning: Data refresh will").click()
    page.get_by_text("Reset On Refresh?").click()
    page.get_by_role("button", name="Cancel").click()
