class Policies:
    def __init__(self, page):
        self.page = page

    def open_policies_page(self):
        self.page.get_by_role("link", name="Policies").click()

    def open_policy_details_page(self):
        self.page.get_by_role("link", name="Controller ServiceAccount Tokens Automount").click()
