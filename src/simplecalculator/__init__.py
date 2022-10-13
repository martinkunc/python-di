from src import simplecalculator
import src.simplecalculator.addition as addition
from src.core import container

# Register implementation to container
container.Addition = addition.Addition()