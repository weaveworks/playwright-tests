class Explorer:
    def __init__(self, page, url):
        self.page = page
        self.url = url

    def open(self):
        self.page.get_by_role("link", name="Explorer").click()

    def search(self, term):
        self.page.goto(f"{self.url}/explorer/query?descending=false&terms={term}")


