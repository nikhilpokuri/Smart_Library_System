from Books_catalog import SingleBook, booksCatalog
from create_media import FlyWeight_factory, StoreMedia
from format_and_title import (
    AudioFormat,
    Book,
    Magazine,
    NewsPaper,
    TextFormat,
    VideoFormat,
)
from loan_decorator import ExtendLoanDecorator, LoanNotificationDecorator
from loan_system_facade import loanSystemFacade
from magazines_catalog import SingleMagazine, magazinesCatalog
from newsPapers_catalog import SingleNewsPaper, newsPapersCatalog
from register_users import UserAdapter
from restricted_section import RestrictedLoansProxy
from store import Store


class Client:
    def __init__(self):
        self.media_factory = {
            "book": Book,
            "magazine": Magazine,
            "news_paper": NewsPaper,
        }
        self.single_media_factory = {
            "book": SingleBook,
            "magazine": SingleMagazine,
            "news_paper": SingleNewsPaper,
        }
        self.format_factory = {
            "text": TextFormat,
            "audio": AudioFormat,
            "video": VideoFormat,
        }
        self.catalog_factory = {
            "book": booksCatalog("Books"),
            "magazine": magazinesCatalog("Magazines"),
            "news_paper": newsPapersCatalog("NewsPaper"),
        }
        self.loan_facade = loanSystemFacade()

    def create_media(self, media_type, _format, title, author, publisher):
        media = self.media_factory[media_type](title, self.format_factory[_format]())
        media.create()
        my_media = media.get_attribute()
        obj = StoreMedia(
            my_media["format"],
            my_media["title"],
            my_media["media_type"],
            author,
            publisher,
            FlyWeight_factory,
        )
        return self.single_media_factory[media_type](obj.create())

    def add_to_catalog(self, media: create_media, media_type):
        catalog = self.catalog_factory[media_type]
        if media_type == "book":
            catalog.add_book(media)
        elif media_type == "magazine":
            catalog.add_magazine(media)
        elif media_type == "news_paper":
            catalog.add_news_paper(media)
        return catalog

    def display_catalog(self, catalog):
        self.catalog_factory[catalog].display()

    def view_store(self):
        print("\nStore Details")
        _store = Store.get_instance().get_store()
        for category in _store:
            print(f"{category} : ")
            print(_store[category], "\n")

    def borrow_media(
        self, user, user_type, media, media_type, loan_obj=loanSystemFacade()
    ):
        loan = loan_obj.borrow_media(user, user_type, media, media_type)
        return loan

    def register_user(self, user, branch, user_type):
        _user = UserAdapter(user, branch, user_type)
        _user.register_user()

    def view_users(self):
        print("\nUser Details:")
        return UserAdapter.get_users_data()


obj = Client()
obj.register_user("nick", "cse", "student")
obj.register_user("steeve", "ece", "student")
obj.register_user("tony", "cse", "faculty")
obj.register_user("clint", "ece", "faculty")

book1 = obj.create_media("book", "audio", "anime_world", "nick", "svs")
book2 = obj.create_media("book", "video", "anime_world1", "nick1", "svs1")

magazine1 = obj.create_media("magazine", "text", "tvd", "steeve", "pns")
magazine2 = obj.create_media("magazine", "text", "forbes", "steeve", "pns")


news_paper1 = obj.create_media("news_paper", "audio", "hindu", "susmi", "pvs")
news_paper2 = obj.create_media("news_paper", "video", "india_today", "susmi", "pvs")

obj.add_to_catalog(book1, "book")
obj.add_to_catalog(book2, "book")
obj.add_to_catalog(magazine1, "magazine")
obj.add_to_catalog(magazine2, "magazine")
obj.add_to_catalog(news_paper1, "news_paper")
obj.add_to_catalog(news_paper2, "news_paper")

obj.display_catalog("book")
obj.display_catalog("magazine")
obj.display_catalog("news_paper")

obj.view_store()
obj.view_users()

loan1 = obj.borrow_media("nick", "student", "tvd", "magazine")
loan2 = obj.borrow_media("nick", "student", "hindu", "news_paper")
loan3 = obj.borrow_media("tony", "faculty", "tvd", "book")
loan4 = obj.borrow_media("clint", "faculty", "tvd", "book")
print(LoanNotificationDecorator(loan1).loan_notification())
print(ExtendLoanDecorator(loan1).extend_loan_notification())

print("Restricted Section\n", RestrictedLoansProxy("Admin").access())
