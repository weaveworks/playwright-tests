import os

from playwright.sync_api import Playwright, sync_playwright, expect
from pages.policies_page import Policies
from pages.application_page import Applications
import pytest


@pytest.mark.usefixtures("login")
class TestPolicies:

    @pytest.fixture(autouse=True)
    def _obj(self, login):
        self.page = login
        self.policies_page = Policies(self.page)
        self.URL = os.getenv("URL")

    def test_open_policies_page(self):
        self.policies_page.open_policies_page()
        expect(self.page).to_have_url(f"{self.URL}/policies")

    def test_open_policy_details_page(self):
        self.policies_page.open_policy_details_page()
        expect(self.page).to_have_url(f"{self.URL}/policy_details/"
                                      f"details?clusterName=management"
                                      f"&id=weave.policies.containers-running-with-privilege-escalation"
                                      f"&name=Containers%20Running%20With%20Privilege%20Escalation")

@pytest.mark.usefixtures("login")
class TestApplications:
    @pytest.fixture(autouse=True)
    def _create_obj(self, login):
        self.page = login
        self.applications_page = Applications(self.page)

    def test_open_applications_page(self):
        self.applications_page.open_application_page()
        expect(self.page).to_have_url(f"{self.URL}/applications")

    def test_open_application_details_page(self):
        self.applications_page.open_application_details_page()
        expect(self.page).to_have_url(f"{self.URL}/kustomization/"
                                      "details?clusterName=management&name=canaries&namespace=flux-system")

    def test_open_application_yaml(self):
        self.applications_page.open_application_yaml_tab()
        expect(self.page .get_by_text("kubectl get kustomization canaries -n flux-system -o yaml")).to_be_visible()

    # page.pause()
    def test_open_application_violations_page(self):
        self.applications_page.open_application_violations_tab()
        expect(self.page).to_have_url(f"{self.URL}/kustomization/"
                                      "violations?clusterName=management&name=canaries&namespace=flux-system")

    def test_open_application_violations_details(self):
        self.applications_page.open_application_violations_details()
        assert f"{self.URL}/policy_violation?clusterName=management&id=" in self.page.url
        expect(self.page .locator("text=Containers Minimum Replica Count in deployment podinfo (1 occurrences)")).to_be_visible()

    def test_open_policy_details_from_app_violations_details_page(self):
        self.applications_page.open_policy_details_from_application_violations_details_page()
        expect(self.page .locator("text=weave.policies.containers-minimum-replica-count")).to_be_visible()

