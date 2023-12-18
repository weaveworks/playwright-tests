import os

from playwright.sync_api import Playwright, sync_playwright, expect
from pages.explorer_page import Explorer
import pytest

@pytest.mark.usefixtures("login")
class TestExplorer:

    @pytest.fixture(autouse=True)
    def _obj(self, login):
        self.URL = os.getenv("URL")
        self.page = login
        self.explorer_page = Explorer(self.page, self.URL)

    def test_search(self):
        self.explorer_page.open()
        expect(self.page).to_have_url(f"{self.URL}/explorer/query")
        self.explorer_page.search("flux-system")
        expect(self.page.locator("tbody")).to_contain_text("flux-system")
