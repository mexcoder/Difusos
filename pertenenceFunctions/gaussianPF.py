from .pertenenceFunction  import PertenenceFunction
import math

class GaussianPF (PertenenceFunction):

    @classmethod
    def pertenence(cls, x, c, delta, **kwargs):
        return math.pow(math.e , (-1/2) * ( ( x - c) / delta) ** 2)