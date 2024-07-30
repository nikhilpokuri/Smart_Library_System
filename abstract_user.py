from abc import ABC, abstractmethod


class User(ABC):
    users_data = {"student": [], "faculty": []}

    @abstractmethod
    def get_users_data(self):
        pass
