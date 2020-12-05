from memebershipFunctions.triangularMF import TriangularMF as triangular
from memebershipFunctions.trapezoidalMF import TrapezoidalMF as trapezoidal
from memebershipFunctions.gaussianMF import GaussianMF as gaussian
from memebershipFunctions.generalizedBellMF import GeneralizedBellMF as gBell
from memebershipFunctions.sigmoidalMF import SigmoidalMF as sigmoidal


from renderer.matplotlibRenderer import MatplotlibRenderer
import click

@click.command()
@click.option("--a", default=10.0)
@click.option("--b", default=20)
@click.option("--c", default=30)
@click.option("--d", default=40)
@click.option("--delta", default=10)
@click.option("--x", default=20)
@click.option("--function", type=click.Choice(["triangular", "trapezoidal", "gaussian", "gBell", "sigmoidal"]), default="sigmoidal")
def run(x, function, **kwargs):
    
    if function in globals():
        selectedMf = globals()[function]
    else:
        raise ValueError("{} does not exist as a Memebership Function".format(function))    

    r = MatplotlibRenderer()
    mf = selectedMf(**kwargs)
    arr = [mf.membership(x) for x in  range (0,100)]     

    r.rendermembershipFunction(arr)

if __name__ == "__main__":
    run()
    