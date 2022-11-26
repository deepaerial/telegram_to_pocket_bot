class Pocket:
    """Wrapper class to interact with Pocket official API"""

    def __init__(self, consumer_key: str):
        self.__consumer_key = consumer_key

    def add(self, url: str):
        """Add new URL link to Pocket"""
        ...
