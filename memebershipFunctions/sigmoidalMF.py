from .membershipFunction import MembershipFunction
import math

class SigmoidalMF (MembershipFunction):

    def __init__ (self, a, c, *args, **kwargs):
        self._a = a
        self._c = c
                

    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self, value):
        self._a = value


    @property
    def c(self):
        return self._c
    
    @c.setter
    def c(self, value):
        self._c = value
    

    def membership(self, x):
        return 1 / ( 1 + math.e ** (-self._a * (x - self._c) ) )