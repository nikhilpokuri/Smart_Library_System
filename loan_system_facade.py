from abstract_user import User
from loan_decorator import LoanDetails, LoanNotificationDecorator
from store import Store


class Availability:
    def __init__(self):
        self.store = Store.get_instance().get_store()

    def isAvailable(self, book, media_type):
        return book in [book["title"] for book in self.store[media_type]]


class verifiedUsers:
    def __init__(self):
        self.users = User.users_data

    def isVerified(self, user, user_type):
        return user in [data[0] for data in self.users[user_type]]


# class Notification:
#     def send_notification(self, user, user_type, title, media_type):
#         return f"{user_type} {user} Borrowed {title} {media_type}"


class loanSystemFacade:
    def __init__(self):
        self.availability = Availability()
        self.verified_users = verifiedUsers()
        self.loan_details = LoanDetails.get_instance()
        self.notification = LoanNotificationDecorator

    def borrow_media(self, user, user_type, title, media_type):
        if self.availability.isAvailable(title, media_type):
            if self.verified_users.isVerified(user, user_type):
                self.loan_details.add_loan(user, user_type, title, media_type)
                return {user: self.loan_details.get_user_loan(user, user_type)}
            raise Exception("Invalid User")
        return f"{title} {media_type} Not Available"
