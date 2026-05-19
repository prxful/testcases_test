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
    page.get_by_role("link", name=f"{PKG_TRANS} PENDING").click()
    page.get_by_role("link", name="Release Manager").click()
    page.get_by_role("button", name="New Release").click()
    page.get_by_role("textbox", name="Release Name *").click()
    page.get_by_role("textbox", name="Release Name *").fill("AUTO_TEST_V1")
    page.get_by_text("Pipeline Environment *Select").click()
    page.get_by_text("Pipeline Environment *Select").click()
    page.get_by_text("C2M_Demo_2.9x TEST").click()
    page.get_by_role("textbox", name="Description *").click()
    page.get_by_role(
        "textbox", name="Description *").fill("Test by Automation")
    page.get_by_role("button", name="Save").click()
    page.get_by_role("textbox", name="i.e., CM.MYC.0801.V01").click()
    page.get_by_role("textbox", name="i.e., CM.MYC.0801.V01").fill(
        "AUTO_TEST_V")
    page.get_by_text("No packages found.").click()
