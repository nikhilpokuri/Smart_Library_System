from abstract_catalog import CatalogManagement
from store import Store


class SingleBook(CatalogManagement):
    def __init__(self, details):
        self.details = details
        self.name = details["title"]
        Store.get_instance().add_item(details["media_type"], details)

    def display(self, space=0):
        print(f"{' ' * space}|- {self.details["title"]}")


class booksCatalog(CatalogManagement):
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book: SingleBook):
        self.books.append(book)

    def display(self, space=0):
        print(" " * space + "|--" + self.name)
        for book in self.books:
            book.display(space + 3)


# root = booksCatalog("Catalogs")
# fictional = booksCatalog("fictional")
# non_fictional = booksCatalog("non_fictional")
# b1 = SingleBook("tvd")
# b2 = SingleBook("to")
# b3 = SingleBook("mirchi")
# fictional.add_book(b1)
# fictional.add_book(b2)
# non_fictional.add_book(b3)
# root.add_book(fictional)
# root.add_book(non_fictional)
# root.display()
