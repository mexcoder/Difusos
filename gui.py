from .guiItems import customWindow, ruleConfigPanel
from .renderer.oopMatplotlibRenderer import  OOPMatplotlibRenderer
from .memebershipFunctions.gaussianMF import GaussianMF
from .renderer.matplotlibRenderer import MatplotlibRenderer
from .networks.takagiSugenoNetwork import TakagiSugenoNetwork
from .networks.networkRule import NetworkRule
from tkinter import ttk, Toplevel

def drawGraph(r, network):
    arr = [network.agregateRules(x/10) for x in  range (0,120)]

    r.configurePlot()
    # draw the precipitation bars as comparison
    r.drawBars(range(0,12), [20, 5 , 5, 10, 15, 165, 280, 220, 160, 48, 15, 5])
    #draw each mf
    x = [x/10 for x in range(0,120)]

    for rule in network._rules:
        mf = rule.membershipFunction.membership
        r.rendermembershipFunction(x, [mf(x/10)* 250 for x in range(120)], "--g")
    r.rendermembershipFunction(x, arr, "r")
    r.render()

# function to open a new window  
# on a button click 
def openConfigWindow(owner, network): 
      
    # Toplevel object which will  
    # be treated as a new window 
    newWindow = Toplevel(owner) 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("Configure Network") 
  
    # sets the geometry of toplevel 
    newWindow.geometry("200x200") 
  
    for rule in network._rules:
        ruleConfigPanel.RuleConfigPanel(rule, newWindow, callback=lambda: drawGraph(r,network))

app = customWindow.App()
r = OOPMatplotlibRenderer(app.getFigure(), app.getCanvas())
buttonFrame = app.mainFrame.buttonsFrame

network = TakagiSugenoNetwork([
    NetworkRule( GaussianMF(0, 1.8), p=-80, q=-15),
    NetworkRule( GaussianMF(2.8, 2.9), p=40, q=78),
    NetworkRule( GaussianMF(10.6, 1.9), p=0.9, q=-10)
])
ttk.Button(buttonFrame, text="configure", command=lambda: openConfigWindow(app.mainFrame, network)).pack()

drawGraph(r, network)

app.mainloop()