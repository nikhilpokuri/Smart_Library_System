from abstract_catalog import CatalogManagement
from store import Store


class SingleNewsPaper(CatalogManagement):
    def __init__(self, details):
        self.details = details
        self.name = details["title"]
        Store.get_instance().add_item(details["media_type"], details)

    def display(self, space=0):
        print(f"{' ' * space}|- {self.name}")


class newsPapersCatalog(CatalogManagement):
    def __init__(self, name):
        self.name = name
        self.newsPapers = []

    def add_news_paper(self, newsPaper: SingleNewsPaper):
        self.newsPapers.append(newsPaper)

    def display(self, space=0):
        print(" " * space + "|--" + self.name)
        for newsPaper in self.newsPapers:
            newsPaper.display(space + 3)


# root = newsPapersCatalog("Catalogs")
# fictional = newsPapersCatalog("fictional")
# non_fictional = newsPapersCatalog("non_fictional")
# b1 = SingleNewsPaper("tvd")
# b2 = SingleNewsPaper("to")
# b3 = SingleNewsPaper("mirchi")
# fictional.add_news_paper(b1)
# fictional.add_news_paper(b2)
# non_fictional.add_news_paper(b3)
# root.add_news_paper(fictional)
# root.add_news_paper(non_fictional)
# root.display()
