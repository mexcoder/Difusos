from abc import ABC, abstractmethod, abstractproperty

class MembershipFunction(ABC):

    def __init__ (self, *args, **kwargs):
        pass

    @abstractmethod
    def membership(self, x):
        """returns the pertenence value of an indeterminate number of parameters
        """
        raise NotImplementedError