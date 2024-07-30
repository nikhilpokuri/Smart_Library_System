from abstract_media import Media


class AuthorPublisher_FlyWeight:
    def __init__(self, author, publisher):
        self.author = author
        self.publisher = publisher

    def create_media(self, _format, title, media_type):
        print(
            f"media_type: {media_type}\nformat: {_format}\ntitle: {title}\nauthor: {self.author}\npublisher: {self.publisher}"
        )
        return {
            "media_type": media_type,
            "format": _format,
            "title": title,
            "author": self.author,
            "publisher": self.publisher,
        }


class FlyWeight_factory:
    def __init__(self):
        self.factory = {}

    def get_author_publisher(self, author, publisher):
        key = (author, publisher)
        if key not in self.factory:
            self.factory[key] = AuthorPublisher_FlyWeight(author, publisher)
        return self.factory[key]


class StoreMedia(Media):
    def __init__(self, _format, title, media_type, author, publisher, factory):
        self.flyWeight = factory().get_author_publisher(author, publisher)
        self.format = _format
        self.title = title
        self.media_type = media_type

    def create(self):
        return self.flyWeight.create_media(self.format, self.title, self.media_type)
