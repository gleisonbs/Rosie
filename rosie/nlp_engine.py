import spacy


class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class NLPEngine(metaclass=SingletonMeta):
    def __init__(self):
        self.pt = spacy.load("pt_core_news_lg")
