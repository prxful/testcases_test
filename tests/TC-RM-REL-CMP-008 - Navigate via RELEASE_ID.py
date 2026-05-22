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
    page.get_by_role("heading", name="TEST78").click()
    page.locator("#radix-_r_1rm_").click()
    page.get_by_role("menuitem", name="Compare release").click()
    page.get_by_role("combobox").click()
    page.get_by_role("option", name="C2M-DEMO-29X-").click()
    page.get_by_role("button", name="Perform Comparison").click()
    page.get_by_text("Comparison job started").click()
    page.get_by_role("link", name="Batch Monitor").click()
    page.get_by_role("link", name="1104116900").click()
    page.get_by_text("COMPARE").click()
    page.get_by_text("Pending").click()
    page.get_by_text("Complete", exact=True).click()
    page.get_by_role("tab", name="Batch Parameters").click()
    page.get_by_text("c2m-demo-2.9x-").click()
    page.get_by_role("link", name="4290491837").click()
    expect(page.get_by_role("link", name="TEST78")).to_have_text("TEST78")
