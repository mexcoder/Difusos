from .trapezoidalMF import TrapezoidalMF

class TriangularMF(TrapezoidalMF):

    def __init__(self, a, b, c, *args, **kwargs):
        # triangular can be represented by a trapezoidaal where c  and b are equal
        super().__init__(a, b, b, c)


    @property
    def b(self):
        return self._b
    
    # when changing _b also change _c
    @b.setter
    def b(self, value):
        self._b = value
        self._c = value
    
    # treat  _d as if it was c
    @property
    def c(self):
        return self._d
    
    @c.setter
    def c(self, value):
        self._d = value

    def membership(self, x):
        """returns the pertenence value of an indeterminate number of parameters
        """

        return super().membership(x)

        # return max( 
        #             min(
        #                 (x-a) / (b-a),
        #                 (c-x) / (c-b)
        #             ),
        #             0
        #         )

