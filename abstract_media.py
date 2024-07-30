from abc import ABC, abstractmethod


class Media(ABC):
    @abstractmethod
    def create(self):
        pass
