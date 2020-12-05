from .membershipFunction  import MembershipFunction
import math

class GaussianMF (MembershipFunction):

    def __init__ (self, c, delta, *args, **kwargs):

        self._c = c
        self._delta = delta
                
    
    @property
    def c(self):
        return self._c
    
    @c.setter
    def c(self, value):
        self._c = value
    
    @property
    def delta(self):
        return self._delta
    
    @delta.setter
    def delta(self, value):
        self._delta = value

    def membership(self, x):
        return math.pow(math.e , (-1/2) * ( ( x - self._c) / self._delta) ** 2)