from abc import ABC, abstractmethod


class ChatPlugin(ABC):
    @abstractmethod
    def should_handle(self, query: str) -> bool:
        pass

    @abstractmethod
    def handle(self, query: str) -> str:
        pass
