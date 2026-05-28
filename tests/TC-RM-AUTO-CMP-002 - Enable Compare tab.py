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
    page.get_by_role("button", name="View Details").nth(5).click()
    page.get_by_role("button", name="Build/Deploy").click()
    page.get_by_text("Auto-Compare on Release?").click()
    page.get_by_text("Auto-Compare on Release?").click()
    page.get_by_role("button", name="Source Code Repo").click()
    page.get_by_role("button", name="Build/Deploy").click()
    page.get_by_role("checkbox", name="Auto-Compare on Release?").click()
    page.get_by_role("button", name="Save").click()
    page.get_by_text("Environment saved successfully").click()
    page.get_by_role("link", name="Pipelines").click()
    page.get_by_text("TEST (test)").click()
    page.get_by_text("GUEST-P1 (GUEST-P1)").click()
    page.get_by_label("Environment Definition").get_by_role(
        "combobox").filter(has_text="C2M-DEMO-29X-").click()
    page.get_by_label("Environment Definition").get_by_role(
        "combobox").filter(has_text="C2M-DEMO-29X-").click()
    page.get_by_label("Environment Definition").get_by_role(
        "combobox").filter(has_text="C2M-DEMO-29X-").dblclick()
    page.locator("html").click()
    page.get_by_role("link", name="Environment Definition").click()
    page.get_by_text("C2M_Demo_2.9x", exact=True).click()
    page.get_by_role("table").get_by_text("C2M-DEMO-29X-").click()
    page.get_by_role("button", name="View Details").nth(5).click()
    page.get_by_role("button", name="Build/Deploy").click()
    page.get_by_role("button", name="Workflow").click()
    page.get_by_role("link", name="Release Manager").click()
    page.get_by_role("button", name="C2M_129").click()
    page.get_by_role("menuitem", name="test", exact=True).click()
    page.get_by_role("heading", name="TEST.ACCT.P2").click()
