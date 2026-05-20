from config import BASE_URL, BASE_UNAME, PASSWORD, PKG_CONFIG

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
    page.get_by_role("link", name=PKG_CONFIG, exact=True).click()
    page.get_by_role("button", name="Data Model C2M2.9_129").click()
    page.get_by_role("menuitem", name="C2M_Demo_2.9x", exact=True).click()
    page.get_by_role("button", name="Take Snapshot").click()
    page.get_by_role("combobox").filter(has_text="DEMO-env- pipeline").click()
    page.get_by_text("C2M-DEMO-29X-").click()
    page.get_by_role("textbox", name="Search dataset...").click()
    page.get_by_role("textbox", name="Search dataset...").fill("algo")
    page.get_by_role("option", name="Algorithm", exact=True).click()
    page.get_by_role("button", name="Continue").click()
    page.get_by_label(
        "Key-Based").get_by_role("button").filter(has_text=re.compile(r"^$")).click()
    page.get_by_role("columnheader", name="Name").get_by_placeholder(
        "Search...").click()
    page.get_by_role("columnheader", name="Name").get_by_placeholder(
        "Search...").fill("INFO")
    page.get_by_role(
        "row", name="Select row C1-ACCT-INFO").get_by_label("Select row").click()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Take Snapshot").click()
    page.get_by_text("Snapshot creation started").click()
