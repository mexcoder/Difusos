from .networkInterface import NetworkInterface
from .networkRule import NetworkRule

class TakagiSugenoNetwork(NetworkInterface):

    def __init__(self, rules:[NetworkRule]):
        self._rules = rules

    def agregateRules(self, x):
        inferences =  [self.getRuleValue(rule, x) for rule in self._rules]    
        memebreshipValues = [rule.membershipFunction.membership(x) for rule in self._rules]
        return sum(inferences) / sum(memebreshipValues)

    def getRuleValue(self, rule, x):
        return rule.membershipFunction.membership(x) * ( rule.p * x + rule.q )


def run():
    from ..memebershipFunctions.gaussianMF import GaussianMF
    from ..renderer.matplotlibRenderer import MatplotlibRenderer
    
    network = TakagiSugenoNetwork([
        NetworkRule( GaussianMF(0, 1.8), p=-80, q=-15),
        NetworkRule( GaussianMF(2.8, 2.9), p=40, q=78),
        NetworkRule( GaussianMF(10.6, 1.9), p=0.9, q=-10)
    ])

    r = MatplotlibRenderer()
    # r.setBackground("difusos/media/bg.png")
    # r.limitAxis((0,120), (18, 36))

    arr = [network.agregateRules(x/10) for x in  range (0,120)]
    # draw the precipitation bars as comparison
    r.drawBars(range(0,12), [20, 5 , 5, 10, 15, 165, 280, 220, 160, 48, 15, 5])
    #draw each mf
    x = [x/10 for x in range(0,120)]

    for rule in network._rules:
        mf = rule.membershipFunction.membership
        r.rendermembershipFunction(x, [mf(x/10)* 250 for x in range(120)], "--g")

    r.rendermembershipFunction(x, arr, "r")
    r.display()
    

if __name__ == "__main__":
    run()

