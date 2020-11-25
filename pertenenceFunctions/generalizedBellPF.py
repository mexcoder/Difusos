from .pertenenceFunction import PertenenceFunction

class GeneralizedBellPF (PertenenceFunction):

    @classmethod
    def pertenence(cls, x, a, b, c, *args, **kwargs):
        return 1 / ( 1 + ( abs( (x - c) / a ) ** (2 * b) ) )