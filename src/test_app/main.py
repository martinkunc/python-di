from src.core import circumference
import src.simplecalculator as simplecalculator
import src.complexcalculator as complexcalculator
import src.core as core
from src.core import container

# Addition: core.Addition

def main() -> int:
    """Echo the input arguments to standard output
    """
    
    a,b = 3,5
    res = container.Addition.add(a,b)
    print(f"{a} + {b} = {res}")

    a,b = 3,5
    res = container.Multiplication.multiply(a,b)
    print(f"{a} * {b} = {res}")

    r = 1
    res = container.Circumference.Calculate(r)
    
    print(f"Circumference of circle with radius {r} is {res}")

    return 0

