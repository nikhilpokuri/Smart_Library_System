from abc import ABC, abstractmethod


class Format(ABC):
    @abstractmethod
    def get_format(self, content):
        pass


class MediaContent(ABC):
    def __init__(self, title, format: Format):
        self.title = title
        self.format = format

    @abstractmethod
    def create(self):
        pass
