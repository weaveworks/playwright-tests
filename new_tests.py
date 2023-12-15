from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:

    page.get_by_role("link", name="GitOpsSets").click()
    page.get_by_role("link", name="gitopsset-configmaps").click()
    page.get_by_text("dev-info-configmap").click()
    page.get_by_role("button").click()
    page.get_by_role("cell", name="staging-info-configmap").click()
    page.get_by_role("button").click()
    page.get_by_text("production-info-configmap").click()
    page.get_by_role("button").click()
    page.get_by_role("tab", name="Events").click()
    page.get_by_role("tab", name="Graph").click()
    page.get_by_role("tab", name="Yaml").click()
    page.get_by_test_id("link-GitOpsSet").click()
