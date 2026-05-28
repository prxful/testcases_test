import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "ignore_https_errors": True,
    }


@pytest.fixture(autouse=True)
def set_page_timeout(page):
    page.set_default_timeout(360000)
    page.set_default_navigation_timeout(360000)
