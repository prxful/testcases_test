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
    page.get_by_role("button", name="Data Model C2M2.9_129").click()
    page.get_by_role("menuitem", name="C2M_Demo_2.9x", exact=True).click()
    page.get_by_role("button", name="New Package").click()
    page.locator("#package-name").click()
    page.locator("#package-name").fill("TEST_ACCT_V111")
    page.get_by_role("textbox", name="Enter package description...").click()
    page.get_by_role(
        "textbox", name="Enter package description...").fill("Test by P")
    page.locator("#package-type").click()
    page.get_by_text("Configuration", exact=True).click()
    page.get_by_role("button", name="Save").click()
    page.get_by_role("link", name="Release Manager").click()
    page.get_by_role("heading", name="TEST9876").click()
    page.locator("#radix-_r_d6_").get_by_role("link",
                                              name="Release Manager").click()
    page.get_by_role("button", name="C2M_129").click()
    page.get_by_role("menuitem", name="test", exact=True).click()
    page.get_by_role("heading", name="REL_TEST_ACCT").click()
    page.get_by_role("textbox", name="i.e., CM.MYC.0801.V01").click()
    page.get_by_role("textbox", name="i.e., CM.MYC.0801.V01").fill(
        "TEST_ACCT_V111")
    page.get_by_text("No packages found.").click()
    page.get_by_role("link", name="My Open Packages").click()
    page.get_by_role("link", name="TEST_ACCT_V111").click()
    page.get_by_role("button", name="Take Snapshot").click()
    page.get_by_role("combobox").filter(has_text="DEMO-env- pipeline").click()
    page.get_by_text("C2M-DEMO-29X-").click()
    page.get_by_role("textbox", name="Search dataset...").click()
    page.get_by_role("textbox", name="Search dataset...").fill("acc")
    page.get_by_text("ess Group").click()
    page.get_by_role("button", name="Continue").click()
    page.get_by_label(
        "Key-Based").get_by_role("button").filter(has_text=re.compile(r"^$")).click()
    page.get_by_role("row", name="Select row MICHELIN Michelin").get_by_label(
        "Select row").click()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Continue").click()
    page.get_by_role("button", name="Take Snapshot").click()
    page.get_by_role("tab", name="Migration Requests").click()
    page.get_by_role("button", name="Migration Requests").click()
    page.get_by_role("combobox", name="Target Definition").click()
    page.get_by_text("C2M_Demo_2.9x TEST").click()
    page.get_by_role("button", name="Save").click()
    page.get_by_role("link", name="Release Manager").click()
    page.get_by_role("heading", name="REL_TEST_ACCT").click()
    page.get_by_role("textbox", name="i.e., CM.MYC.0801.V01").click()
    page.get_by_role("textbox", name="i.e., CM.MYC.0801.V01").fill(
        "TEST_ACCT_V111")
    page.get_by_text("No packages found.").click()
    page.locator("#radix-_r_d6_").get_by_role("link",
                                              name="Release Manager").click()
    page.get_by_role("heading", name="REL_TEST_ACCT").click()
    page.get_by_role("link", name="My Open Packages").click()
    page.get_by_role("link", name="TEST_ACCT_V111").click()
    page.get_by_role("tab", name="Migration Requests").click()
    page.get_by_role("button", name="Actions").click()
    page.get_by_role("menuitem", name="Migration Approve").click()
    page.get_by_role("button", name="Approve").click()
    page.get_by_text("Package 1189791350 approved").click()
    page.get_by_role("link", name="Release Manager").click()
    page.get_by_role("heading", name="REL_TEST_ACCT").click()
    page.get_by_role("textbox", name="i.e., CM.MYC.0801.V01").click()
    page.get_by_role("textbox", name="i.e., CM.MYC.0801.V01").fill(
        "TEST_ACCT_V111")
    page.get_by_text("No packages found.").click()
    page.get_by_role("textbox", name="i.e., CM.MYC.0801.V01").click()
    page.get_by_role("textbox", name="i.e., CM.MYC.0801.V01").fill("")
    page.get_by_role("link", name="My Open Packages").click()
    page.get_by_role("link", name="TEST_ACCT_V111").click()
