from .abstractRenderer import AbstractRenderer

import matplotlib.pyplot as plt

class MatplotlibRenderer(AbstractRenderer):

    def renderPertenenceFunction(self, *args):
        plt.plot(*args)
        plt.show()