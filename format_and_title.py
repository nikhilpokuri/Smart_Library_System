from abstract_format_and_title import Format, MediaContent


class TextFormat(Format):
    def get_format(self, content):
        print(f"Displaying {content} in text\n")
        return "text"


class AudioFormat(Format):
    def get_format(self, content):
        print(f"Displaying {content} in audio\n")
        return "audio"


class VideoFormat(Format):
    def get_format(self, content):
        print(f"Displaying {content} in video\n")
        return "video"


class Book(MediaContent):
    my_book = {}

    def create(self):
        print(f"title:{self.title}")
        self.my_book["title"] = self.title
        self.my_book["format"] = self.format.get_format(self.title)
        self.my_book["media_type"] = "book"

    def get_attribute(self):
        return self.my_book


class Magazine(MediaContent):
    my_magazine = {}

    def create(self):
        print(f"title:{self.title}")
        self.my_magazine["title"] = self.title
        self.my_magazine["format"] = self.format.get_format(self.title)
        self.my_magazine["media_type"] = "magazine"

    def get_attribute(self):
        return self.my_magazine


class NewsPaper(MediaContent):
    my_news_paper = {}

    def create(self):
        print(f"title:{self.title}")
        self.my_news_paper["title"] = self.title
        self.my_news_paper["format"] = self.format.get_format(self.title)
        self.my_news_paper["media_type"] = "news_paper"

    def get_attribute(self):
        return self.my_news_paper


# b1 = Book("tvd", VideoFormat())
# b2 = Book("to", AudioFormat())
# m1 = Magazine("legacies", TextFormat())
# m2 = Magazine("dark", TextFormat())
# b1.create()
# b2.create()
# m1.create()
# m2.create()
# print(b2.my_book)
# print(m2.my_magazine)
