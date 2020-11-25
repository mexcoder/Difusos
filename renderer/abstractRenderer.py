from abc import ABC, abstractmethod

class AbstractRenderer (ABC):

    @abstractmethod
    def renderPertenenceFunction(self, *args, **kwargs):
        raise NotImplementedError