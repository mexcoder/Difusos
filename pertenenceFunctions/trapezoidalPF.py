from .pertenenceFunction import PertenenceFunction

class TrapezoidalPF (PertenenceFunction):

    @classmethod
    def pertenence(cls, x, a, b, c, d):
        
        return max(
                   min( 
                       (x - a) / (b - a),
                       1,
                       (d - x) / (d - c)
                   ),
                   0
                  )