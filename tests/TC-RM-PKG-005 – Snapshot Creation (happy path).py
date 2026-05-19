import pytest
import re
from playwright.sync_api import Page, expect
from config import BASE_URL, BASE_UNAME, PASSWORD, PKG_TRANS


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    return {"ignore_https_errors": True}


def test_example(page: Page) -> None:
    page.goto(BASE_URL)
    page.get_by_role("textbox", name="Username").click()
    page.get_by_role("textbox", name="Username").fill(BASE_UNAME)
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill(PASSWORD)
    page.get_by_role("textbox", name="Password").press("Enter")
    page.get_by_role("button", name="Login").click()
    page.get_by_role("link", name=PKG_TRANS).click()
    page.get_by_role("button", name="Take Snapshot").click()
    page.get_by_role("button", name="Data Model C2M2.9_129").click()
    page.get_by_role("menuitem", name="GUEST_C2M_DEMO_2.9x").click()
    page.get_by_role("button", name="Cancel").click()
    page.get_by_role("button", name="Data Model GUEST_C2M_DEMO_2.9x").click()
    page.get_by_role("menuitem", name="C2M_Demo_2.9x", exact=True).click()
    page.get_by_role("button", name="Take Snapshot").click()
    page.get_by_role("combobox").filter(has_text="DEMO-env- pipeline").click()
    page.get_by_role("option", name="C2M-DEMO-29X-").click()
    page.get_by_role("textbox", name="Search dataset...").click()
    page.get_by_role("textbox", name="Search dataset...").fill("acc")
    page.get_by_role("option", name="Account").click()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("textbox", name="Enter value...").click(
        modifiers=["ControlOrMeta"])
    page.get_by_role("textbox", name="Enter value...").fill("0065787048")
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Take Snapshot").click()
    page.goto("https://98.95.255.82:7503/mmmWeb/workflow/package/1397562458")
    page.get_by_role("cell", name="0065787048").click()
