import os

from playwright.sync_api import Playwright, sync_playwright, expect
import pytest


@pytest.mark.usefixtures("login")
class TestExplorer:

    @pytest.fixture(autouse=True)
    def _obj(self, login):
        self.page = login
        self.URL = os.getenv("URL")

    def test_open_explorer_page(self):
        self.policies_page.open_policies_page()
        expect(self.page).to_have_url(f"{self.URL}/policies/list")
