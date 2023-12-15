class GitopsSets:
    def __init__(self, page):
        self.page = page

    def open_gitopssets_page(self):
        self.page.get_by_role("link", name="GitOpsSets").click()

    def open_gitopssets_details_page(self):
        self.page.get_by_role("link", name="gitopsset-configmaps").click()

    def open_first_configmap_yaml(self):
        self.page.get_by_text("dev-info-configmap").click()

    def open_second_configmap_yaml(self):
        self.page.get_by_text("staging-info-configmap").click()

    def open_third_configmap_yaml(self):
        self.page.get_by_text("production-info-configmap").click()

    def open_gitopssets_events_tab(self):
        self.page.get_by_role("tab", name="Events").click()

    def open_gitopssets_graph_tab(self):
        self.page.get_by_role("tab", name="Graph").click()

    def open_gitopssets_yaml_tab(self):
        self.page.get_by_role("tab", name="Yaml").click()

    def back_to_gitopssets_list(self):
        self.page.get_by_test_id("link-GitOpsSet").click()
