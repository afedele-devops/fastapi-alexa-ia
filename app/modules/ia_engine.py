from abc import ABC, abstractmethod

class IAEngine(ABC):
    @abstractmethod
    def query(self, prompt: str) -> str:
        pass
