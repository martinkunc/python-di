from os import path
from src.core.addition import Addition
from src.core.multiplication import Multiplication
from src.core.circumference import Circumference
from src.core import container

container.Circumference = Circumference()

PROJECT_NAME = "python-clean-architecture"
PACKAGE_NAME = "core"
VERSION = "0, 0, 7"

PACKAGE_DIR = path.dirname(__file__)
PROJECT_DIR = path.dirname(PACKAGE_DIR)

