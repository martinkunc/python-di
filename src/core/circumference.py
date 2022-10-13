from __future__ import annotations

import math
import src.core.addition
import src.core.multiplication
from src.core import container


class Circumference:

    @property
    def addition(self):
        return container.Addition

    @property
    def multiplication(self):
        return container.Multiplication

    def Calculate(self: Circumference, r: int) -> int:
        d = self.addition.add(r, r)
        c = self.multiplication.multiply(math.pi, d)
        return c
