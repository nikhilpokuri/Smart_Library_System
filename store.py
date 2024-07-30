class Store:
    __instance = None

    @staticmethod
    def get_instance():
        if Store.__instance == None:
            Store()
        return Store.__instance

    def __init__(self):
        if Store.__instance != None:
            raise Exception("Cannot Create New Store Instance")
        else:
            Store.__instance = self
        self.__store = {"book": [], "magazine": [], "news_paper": []}

    def add_item(self, media_type, details):
        self.__store[media_type].append(details)

    def get_store(self):
        return self.__store
