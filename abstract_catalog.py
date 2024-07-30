from abc import ABC, abstractmethod


class CatalogManagement(ABC):
    @abstractmethod
    def display(self, space=0):
        pass
