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
    page.get_by_role("tab", name="Search").click()
    page.get_by_role("combobox").filter(has_text="+ Add Filter").click()
    page.get_by_text("Description").click()
    page.get_by_role("combobox").filter(has_text=re.compile(r"^$")).click()
    page.get_by_text("Creation Date").click()
    page.get_by_role("combobox").filter(has_text=re.compile(r"^$")).click()
    page.get_by_text("Config Packages").click()
    page.get_by_role("combobox").filter(has_text=re.compile(r"^$")).click()
    page.get_by_text("Release Name").click()
    page.get_by_role("combobox").filter(has_text=re.compile(r"^$")).click()
    page.get_by_text("Release Id").click()
    page.get_by_role("combobox").filter(has_text=re.compile(r"^$")).click()
    page.get_by_text("Pipeline Environment").click()
