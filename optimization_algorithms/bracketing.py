from re import S
from optimization_algorithms.base import OptimizationAlgorithms
import typing

class Bracketing(OptimizationAlgorithms):
    def __init__(self) -> None:
        super().__init__()

    def bracket_minimum(self, function_to_optimize: typing.Callable, initial_state:float, step_size: float=1e-2, multiplier: float=2.0) -> tuple:
        a, fa = initial_state, function_to_optimize(initial_state) 
        b, fb = initial_state + step_size, function_to_optimize(initial_state + step_size)

        if fb > fa:
            step_size = -step_size
            a, b, fa, fb = b, a, fb, fa
        
        while True:
            c, fc = b + step_size, function_to_optimize(b + step_size)
            if fc > fb:
                return (round(a, 2), round(c, 2)) if c > a else (round(c, 2), round(a, 2))
            a, b, fa, fb = b, c, fb, fc
            step_size *= multiplier
