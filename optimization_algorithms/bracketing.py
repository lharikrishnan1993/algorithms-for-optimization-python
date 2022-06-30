from re import S
from optimization_algorithms.base import OptimizationAlgorithms
import typing
import math 

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

    def fibonacci_search(self, function_to_optimize: typing.Callable, a:float, b:float, n:float, epsilon:float=1e-2) -> tuple:
        sqrt_five = math.sqrt(5)
        s = (1 - sqrt_five) / (1 + sqrt_five)
        phi = (1 + sqrt_five) / 2
        rho = 1 / (phi * (1 - s**(n+1)) / (1 - s**n))
        d = rho * b + (1 - rho) * a
        yd = function_to_optimize(d)

        for i in range(1, n):
            if i == n-1:
                c = epsilon * a + (1 - epsilon) * d
            else:
                c = rho * a + (1 - rho) * b
            
            yc = function_to_optimize(c)
            
            if yc < yd:
                b, d, yd = d, c, yc
            else:
                a, b = b, c
            
            rho = 1 / (phi * (1 - s**(n-i+1)) / (1 - s**(n-i)))
        
        return (round(a, 2), round(b, 2)) if a < b else (round(b, 2), round(a, 2))
