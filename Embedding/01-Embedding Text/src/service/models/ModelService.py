from abc import ABC, abstractmethod


class ModelService(ABC):

    @abstractmethod
    def extract_data(self, text):
        pass

    @abstractmethod
    def send_request(self, text):
        pass

    @abstractmethod
    def extract_embeddings(self, response):
        pass

    @abstractmethod
    def extract_tokens(self, response):
        pass
