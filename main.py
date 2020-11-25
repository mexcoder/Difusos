# from pertenenceFunctions.triangularPF import TriangularPF as pf
# from  pertenenceFunctions.trapezoidalPF import TrapezoidalPF as pf
# from  pertenenceFunctions.gaussianPF import GaussianPF as pf
#from  pertenenceFunctions.generalizedBellPF import GeneralizedBellPF as pf
from  pertenenceFunctions.sigmoidalPF import SigmoidalPF as pf


from renderer.matplotlibRenderer import MatplotlibRenderer
import click

@click.command()
@click.option("--a", default=10.0)
@click.option("--b", default=20)
@click.option("--c", default=30)
@click.option("--d", default=40)
@click.option("--delta", default=10)
@click.option("--x", default=20)
def run(x, **kwargs):

    print (kwargs)
    
    r = MatplotlibRenderer()
    arr = [pf.pertenence(x, **kwargs) for x in  range (0,100)]     

    r.renderPertenenceFunction(arr)

if __name__ == "__main__":
    run()
    