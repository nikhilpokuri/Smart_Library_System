from abstract_catalog import CatalogManagement
from store import Store


class SingleMagazine(CatalogManagement):
    def __init__(self, details):
        self.details = details
        self.name = details["title"]
        Store.get_instance().add_item(details["media_type"], details)

    def display(self, space=0):
        print(f"{' ' * space}|- {self.name}")


class magazinesCatalog(CatalogManagement):
    def __init__(self, name):
        self.name = name
        self.magazines = []

    def add_magazine(self, magazine: SingleMagazine):
        self.magazines.append(magazine)

    def display(self, space=0):
        print(" " * space + "|--" + self.name)
        for magazine in self.magazines:
            magazine.display(space + 3)


# root = magazinesCatalog("Catalogs")
# fictional = magazinesCatalog("fictional")
# non_fictional = magazinesCatalog("non_fictional")
# b1 = SingleMagazine("tvd")
# b2 = SingleMagazine("to")
# b3 = SingleMagazine("mirchi")
# fictional.add_magazine(b1)
# fictional.add_magazine(b2)
# non_fictional.add_magazine(b3)
# root.add_magazine(fictional)
# root.add_magazine(non_fictional)
# root.display()
