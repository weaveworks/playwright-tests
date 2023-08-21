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
        expect(self.page).to_have_url(f"{self.URL}/policies/list")

    def test_open_policy_details_page(self):
        self.policies_page.open_policy_details_page()
        expect(self.page).to_have_url(f"{self.URL}/policy_details/"
                                      f"details?clusterName=management"
                                      f"&id=weave.policies.containers-minimum-replica-count"
                                      f"&name=Containers%20Minimum%20Replica%20Count")



@pytest.mark.usefixtures("login")
class TestApplications:
    @pytest.fixture(autouse=True)
    def _create_obj(self, login):
        self.page = login
        self.applications_page = Applications(self.page)
        self.URL = os.getenv("URL")

    def test_open_applications_page(self):
        self.applications_page.open_application_page()
        expect(self.page).to_have_url(f"{self.URL}/applications")

    def test_open_application_details_page(self):
        self.applications_page.open_application_details_page()
        expect(self.page).to_have_url(f"{self.URL}/kustomization/"
                                      f"details?clusterName=management"
                                      f"&name=violating-podinfo&namespace=default")

    def test_open_application_yaml(self):
        self.applications_page.open_application_yaml_tab()
        expect(self.page .get_by_text("kubectl get kustomization violating-podinfo -n default -o yaml")).to_be_visible()

    # page.pause()
    def test_open_application_violations_page(self):
        self.applications_page.open_application_violations_tab()
        expect(self.page).to_have_url(f"{self.URL}/kustomization/"
                                      f"violations?clusterName=management"
                                      f"&name=violating-podinfo&namespace=default")


    def test_open_application_violations_details(self):
        self.applications_page.open_application_violations_details()
        assert f"{self.URL}/policy_violation?clusterName=management&id=" in self.page.url
        expect(
            self.page.get_by_text("imagePolicyPolicy must be 'IfNotPresent'; found 'Always'")
        ).to_be_visible()

    def test_open_policy_details_from_app_violations_details_page(self):
        self.applications_page.open_policy_details_from_application_violations_details_page()
        expect(self.page.get_by_text("weave.policies.container-image-pull-policy")).to_be_visible()

    def test_open_policy_violations_page(self):
        self.applications_page.open_policy_violations_page()
        expect(self.page).to_have_url(f"{self.URL}/policy_details/violations?clusterName=management"
                                      f"&id=weave.policies.container-image-pull-policy"
                                      f"&name=Container%20Image%20Pull%20Policy")


    def test_open_policy_violations_details_page(self):
        self.applications_page.open_policy_violations_details_page()
        assert f"{self.URL}/policy_violation?clusterName=management&id=" in self.page.url
        expect(self.page.locator("text=imagePolicyPolicy must be 'IfNotPresent'; found 'Always'")).to_be_visible()

