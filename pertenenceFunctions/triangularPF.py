from .pertenenceFunction import PertenenceFunction

class TriangularPF(PertenenceFunction):

    @classmethod
    def pertenence(cls, x, a, b, c, *args):
        """returns the pertenence value of an indeterminate number of parameters
        """

        # return super(x, a, b, b, c)

        return max( 
                    min(
                        (x-a) / (b-a),
                        (c-x) / (c-b)
                    ),
                    0
                )


if __name__ == "__main__":

    a = 10
    b = 5
    c = 3

    for x in range (0,100):
        print(TriangularPF.pertenence(x, a, b, c))