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
    page.get_by_role("button", name="Data Model C2M2.9_129").click()
    page.get_by_role("menuitem", name="C2M_Demo_2.9x", exact=True).click()
    page.get_by_role("heading", name="TEST9876").click()
    page.get_by_role("button", name="Pull Packages").click()
    page.get_by_role("menuitem", name="Unassigned Only").click()
    page.get_by_text("Packages pulled successfully").click()
    page.get_by_role("cell", name="No results.").click()
