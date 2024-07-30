from loan_decorator import LoanDetails


class Loans:
    def __init__(self):
        self.__loan_details = LoanDetails.get_instance().get_loan_details()

    def accesss(self):
        return self.__loan_details


class RestrictedLoansProxy:
    def __init__(self, role):
        self.role = role.lower()

    def access(self):
        if self.role == "admin":
            return Loans().accesss()
        raise Exception("(Sensitive Information)....Access Denied")
