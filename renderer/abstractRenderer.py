from abc import ABC, abstractmethod

class AbstractRenderer (ABC):

    @abstractmethod
    def rendermembershipFunction(self, *args, **kwargs):
        raise NotImplementedError