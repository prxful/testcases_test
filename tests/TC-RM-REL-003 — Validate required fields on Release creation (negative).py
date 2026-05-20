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
    page.get_by_role("link", name="Release Manager").click()
    page.get_by_role("button", name="New Release").click()
    page.get_by_role("textbox", name="Release Name *").click()
    page.get_by_role("textbox", name="Release Name *").fill("ACCT_VER_TEST_V1")
    page.get_by_role("combobox", name="Pipeline Environment *").click()
    page.get_by_text("GUEST-P1").click()
    page.get_by_role("textbox", name="Description *").click()
    page.get_by_role("textbox", name="Description *").fill("Test by P")
    page.get_by_role("textbox", name="Description *").press("ControlOrMeta+a")
    page.get_by_role("textbox", name="Description *").fill("")
    page.get_by_text("Description is required").click()
    page.get_by_role("textbox", name="Release Name *").click()
    page.get_by_role("textbox", name="Release Name *").press("ControlOrMeta+a")
    page.get_by_role("textbox", name="Release Name *").fill("")
    page.get_by_text("Release Name is required").click()
    page.get_by_role("button", name="Save").click()
