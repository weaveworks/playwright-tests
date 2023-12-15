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
        expect(self.page.get_by_role("table")).not_to_be_empty()

    def test_open_first_configmap_yaml(self):
        self.gitopssets_page.open_first_configmap_yaml()
        expect(self.page.get_by_text("kubectl get configmap dev-info-configmap -n default -o yaml")).to_be_visible()
        self.page.get_by_role("button").click()

    def test_open_second_configmap_yaml(self):
        self.gitopssets_page.open_second_configmap_yaml()
        expect(self.page.get_by_text("kubectl get configmap staging-info-configmap -n default -o yaml")).to_be_visible()
        self.page.get_by_role("button").click()

    def test_open_third_configmap_yaml(self):
        self.gitopssets_page.open_third_configmap_yaml()
        expect(self.page.get_by_text("kubectl get configmap production-info-configmap -n default -o yaml")).to_be_visible()
        self.page.get_by_role("button").click()

    def test_open_gitopssets_events_tab(self):
        self.gitopssets_page.open_gitopssets_events_tab()
        expect(self.page).to_have_url(f"{self.URL}/object/events?"
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
        expect(self.page.get_by_role("table")).not_to_be_empty()
