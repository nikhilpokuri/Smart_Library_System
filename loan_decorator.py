class LoanDetails:
    __instance = None

    @staticmethod
    def get_instance():
        if LoanDetails.__instance == None:
            LoanDetails()
        return LoanDetails.__instance

    def __init__(self):
        if LoanDetails.__instance == None:
            LoanDetails.__instance = self
        else:
            raise Exception("Cannot Create New Loan Details Instance")
        self.loan_details = {"student": {}, "faculty": {}}

    def add_loan(self, user, user_type, title, media_type):
        if user in self.loan_details[user_type]:
            self.loan_details[user_type][user].append(
                {"title": title, "media_type": media_type}
            )
        else:
            self.loan_details[user_type][user] = [
                {"title": title, "media_type": media_type}
            ]

    def get_loan_details(self):
        return self.loan_details

    def get_user_loan(self, user, user_type):
        return self.loan_details[user_type][user]


class LoanNotificationDecorator:
    def __init__(self, details):
        self.loan_details = details

    def loan_notification(self):
        return f"Loan Details Notification:\n{self.loan_details}\n"


class ExtendLoanDecorator:
    def __init__(self, details):
        self.loan_details = details

    def extend_loan_notification(self):
        return f"Loan Extension Notification:\n{self.loan_details}\n"
