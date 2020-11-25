from .pertenenceFunction import PertenenceFunction
import math

class SigmoidalPF (PertenenceFunction):

    @classmethod
    def pertenence(cls, x, a, c, *arrgs, **kwargs):
        return 1 / ( 1 + math.e ** (-a * (x - c) ) )