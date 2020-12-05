from .membershipFunction import MembershipFunction

class TrapezoidalMF (MembershipFunction):

    def __init__ (self, a, b, c, d, *args, **kwargs):
        self._a = a
        self._b = b
        self._c = c
        self._d = d
                

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
    
    @property
    def d(self):
        return self._d
    
    @d.setter
    def d(self, value):
        self._d = value
    
    
    def membership(self, x):
        
        return max(
                   min( 
                       (x - self._a) / (self._b - self._a),
                       1,
                       (self._d - x) / (self._d - self._c)
                   ),
                   0
                  )