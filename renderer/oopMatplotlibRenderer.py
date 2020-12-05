from .abstractRenderer import AbstractRenderer

import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class OOPMatplotlibRenderer(AbstractRenderer):

    def __init__(self, figure, canvas = None):
        self.figure = figure
        self.plot = self.figure.add_subplot(111)
        self.canvas = canvas
        
    def rendermembershipFunction(self, *args):
        self.drawPlot(*args)

    def drawPlot(self, *args):
        self.plot.plot(*args)

    def drawBars(self, *args):
        self.plot.bar(* args)

    def configurePlot(self):
        self.plot.clear()
        self.plot.grid(True)

    def render(self):
        if self.canvas is None:
            self.plot.draw()
        else: 
            self.canvas.draw()