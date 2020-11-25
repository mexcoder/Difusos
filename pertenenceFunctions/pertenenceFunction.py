from abc import ABC, abstractmethod

class PertenenceFunction(ABC):

    @classmethod
    @abstractmethod
    def pertenence(cls, x, *args, **kwargs):
        """returns the pertenence value of an indeterminate number of parameters
        """
        raise NotImplementedError