from .membershipFunction import MembershipFunction

class GeneralizedBellMF (MembershipFunction):

    def __init__ (self, a, b, c, *args, **kwargs):
        self._a = a
        self._b = b
        self._c = c
                

    @property
    def a(self):
        return self._a
    
    @a.setter
    def a(self, value):
        self._a = value


    @property
    def b(self):
        return self._b
    
    @b.setter
    def b(self, value):
        self._b = value
    
    @property
    def c(self):
        return self._c
    
    @c.setter
    def c(self, value):
        self._c = value
    
    def membership(self, x):
        return 1 / ( 1 + ( abs( (x - self._c) / self._a ) ** (2 * self._b) ) )