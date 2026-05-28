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
    page.get_by_text("C2M_Demo_2.9x", exact=True).click()
    page.get_by_role("button", name="Data Model C2M2.9_129").click()
    page.get_by_role("menuitem", name="C2M_Demo_2.9x", exact=True).click()
    page.get_by_role("complementary").get_by_text(
        "C2M_Demo_2.9x", exact=True).click()
    page.get_by_role("button", name="View Details").nth(5).click()
    page.get_by_role("button", name="Build/Deploy").click()
    page.get_by_role("checkbox", name="Auto-Compare on Release?").click()
    page.get_by_role("button", name="Save").click()
    page.get_by_role("button", name="Workflow").click()
    page.get_by_role("link", name="Release Manager").click()
    page.get_by_role("heading", name="TEST78").click()
    page.locator("#radix-_r_12a_").click()
    page.get_by_role("menuitem", name="Deploy").click()
    page.get_by_role("button", name="Process Deployment").click()
    page.get_by_role("tab", name="Batch Parameters").click()
    page.get_by_role("link", name="RELEASE_ID", exact=True).click()
    page.locator("#radix-_r_1pk_").click()
    page.get_by_role("menuitem", name="Analyze Comparison").click()
    page.get_by_role("link", name="TEST78").click()
    page.locator("#radix-_r_1rf_").click()
    page.locator("html").click()
    page.get_by_role("tab", name="Reconciliations").click()
    page.locator("#radix-_r_1rf_").click()
    page.get_by_role("menuitem", name="Analyze Comparison").click()
    page.get_by_role("button", name="Refresh").click()
    page.get_by_role("button", name="Refresh").click()
    page.get_by_text("1117447450").click()
    page.get_by_text("Deltas").first.click()
