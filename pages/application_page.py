class Applications:
    def __init__(self, page):
        self.page = page

    def open_application_page(self):
        self.page.get_by_role("link", name="Applications").click()

    def open_application_details_page(self):
        self.page.get_by_role("link", name="flux-system").click()

    def open_application_yaml_tab(self):
        self.page.get_by_role("tab", name="Yaml").click()

    def open_application_violations_tab(self):
        self.page.get_by_role("tab", name="Violations").click()

    def open_application_violations_details(self):
        self.page.get_by_role("link", name="Container Image Pull Policy in deployment violated-podinfo (1 occurrences)").nth(0).click()

    def open_policy_details_from_application_violations_details_page(self):
        self.page.get_by_role("link", name="Container Image Pull Policy").click()

    def open_policy_violations_page(self):
        self.page.get_by_role("link", name="Violations").click()

    def open_policy_violations_details_page(self):
        self.page.get_by_role("link", name="Container Image Pull Policy in deployment violated-podinfo (1 occurrences)").click()
