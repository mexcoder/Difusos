from .abstractRenderer import AbstractRenderer

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class MatplotlibRenderer(AbstractRenderer):

    def __init__(self):
        self.bg = None
        self._limitAxis = False

    def setBackground(self, filename):
        self.bg = mpimg.imread(filename)
        

    def limitAxis(self, x, y):
        self._limitAxis = x is not None or y is not None
        self.xLimit = x
        self.yLimit = y

    def rendermembershipFunction(self, *args):
        if self._limitAxis:
            plt.xlim(self.xLimit[0], self.xLimit[1])
            plt.ylim(self.yLimit[0], self.yLimit[1])
        if self.bg is not None:
            plt.imshow(self.bg)
        plt.plot(*args)

    def drawBars(self, *args):
        plt.bar(* args)
    

    def display(self):
        plt.show()