import os

from playwright.sync_api import Playwright, sync_playwright, expect
from pages.gitopssets_page import GitopsSets
import pytest

@pytest.mark.usefixtures("login")
class TestGitopsSets:
    @pytest.fixture(autouse=True)
    def _create_obj(self, login):
        self.page = login
        self.gitopssets_page = GitopsSets(self.page)
        self.URL = os.getenv("URL")

    def test_open_gitopssets_page(self):
        self.gitopssets_page.open_gitopssets_page()
        expect(self.page).to_have_url(f"{self.URL}/gitopssets")

    def test_open_gitopssets_details_page(self):
        self.gitopssets_page.open_gitopssets_details_page()
        expect(self.page).to_have_url(f"{self.URL}/gitopssets/object/details?"
                                      f"clusterName=management"
                                      f"&name=gitopsset-configmaps"
                                      f"&namespace=default")
        expect(self.page.locator("xpath=//div[contains(@class,'MuiTableContainer-root')]")
               ).to_contain_text("dev-info-configmap")

    def test_open_dev_info_configmap_details(self):
        self.gitopssets_page.open_dev_info_configmap_details()
        (expect(self.page.locator("xpath=//div[contains(@class,'YamlView-sc')]")
                ).to_be_visible())
        self.page.get_by_role("button").click()

    def test_open_staging_info_configmap_details(self):
        self.gitopssets_page.open_staging_info_configmap_details()
        (expect(self.page.locator("xpath=//div[contains(@class,'YamlView-sc')]")
                ).to_be_visible())
        self.page.get_by_role("button").click()

    def test_open_production_info_configmap_details(self):
        self.gitopssets_page.open_production_info_configmap_details()
        (expect(self.page.locator("xpath=//div[contains(@class,'YamlView-sc')]")
                ).to_be_visible())
        self.page.get_by_role("button").click()

    def test_open_gitopssets_events_tab(self):
        self.gitopssets_page.open_gitopssets_events_tab()
        expect(self.page).to_have_url(f"{self.URL}/gitopssets/object/events?"
                                      f"clusterName=management"
                                      f"&name=gitopsset-configmaps"
                                      f"&namespace=default")

    def test_open_gitopssets_graph_tab(self):
        self.gitopssets_page.open_gitopssets_graph_tab()
        expect(self.page).to_have_url(f"{self.URL}/gitopssets/object/graph?"
                                      f"clusterName=management"
                                      f"&name=gitopsset-configmaps"
                                      f"&namespace=default")

    def test_open_gitopssets_yaml_tab(self):
        self.gitopssets_page.open_gitopssets_yaml_tab()
        expect(self.page).to_have_url(f"{self.URL}/gitopssets/object/yaml?"
                                      f"clusterName=management"
                                      f"&name=gitopsset-configmaps"
                                      f"&namespace=default")
        expect(self.page.get_by_text("kubectl get gitopsset gitopsset-configmaps -n default -o yaml")).to_be_visible()

    def test_back_to_gitopssets_list(self):
        self.gitopssets_page.back_to_gitopssets_list()
        expect(self.page).to_have_url(f"{self.URL}/gitopssets")
        expect(self.page.locator("tbody")).to_contain_text("gitopsset-configmaps")
