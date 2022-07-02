from unicodedata import name
import streamlit as st
import numpy as np
from optimization_algorithms.bracketing import Bracketing
from plotly import graph_objects as go

class AforO_Bracketing:
    def __init__(self) -> None:
        self.bracketer = Bracketing()
        self.univariate_function = lambda x: x**2 - 3.5*x + 2.5     # Minima -> 1.75

    def run(self):
        _, center, _ = st.columns([1, 1, 1])
        with center:
            st.header("Chapter 03 - Bracketing")
        st.write('Bracketing is the process of identifying an interval in which the local minimum lies and then successively shrinking the interval.')
        st.write("We can *bracket* an interval *[a, c]* containing the global minimum if we can find three points *a < b < c* such that *f(a) < f(b) < f(c)*.")
        st.subheader('Finding an Initial Bracket')
        st.write("When optimizing a function, we often start by first bracketing an interval containing a local minimum. We then successively reduce the size of the bracketed interval to converge on the local minimum.")

        initial_start = 5.0
        bracket = self.bracketer.bracket_minimum(self.univariate_function, initial_start)
        st.write(f"For the example univariate function, $x^2 - 3.5x + 2.5$, the resulting bracket is **{bracket}**")
        bracket_minimum_code = '''
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
'''
        st.code(bracket_minimum_code, language="python")

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[i for i in range(-15, 16)], y=[self.univariate_function(i) for i in range(-15, 16)], mode='lines', name='Univariate Function'))
        fig.add_trace(go.Scatter(x=[x for x in bracket], y=[self.univariate_function(x) for x in bracket], mode='markers', name='Intervals'))
        fig.update_xaxes(title='x')
        fig.update_yaxes(title='f(x)')
        fig.update_layout(title='Bracket for the function, x**2 - 3.5*x + 2.5')
        st.plotly_chart(fig)

        st.subheader('Fibonacci Search')

        bracket = self.bracketer.fibonacci_search(self.univariate_function, -10, 10, 4)
        st.write(f"For the example univariate function, $x^2 - 3.5x + 2.5$, the resulting bracket is **{bracket}** for an initial bracket of **[-10, 10]** for 4 iterations")

        fibonacci_search_code = '''
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
'''
        st.code(fibonacci_search_code, language="python")

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[i for i in range(-15, 16)], y=[self.univariate_function(i) for i in range(-15, 16)], mode='lines', name='Univariate Function'))
        fig.add_trace(go.Scatter(x=[x for x in bracket], y=[self.univariate_function(x) for x in bracket], mode='markers', name='Intervals'))
        fig.update_xaxes(title='x')
        fig.update_yaxes(title='f(x)')
        fig.update_layout(title='Bracket for the function, x**2 - 3.5*x + 2.5')
        st.plotly_chart(fig)

        st.subheader('Golden Section Search')

        bracket = self.bracketer.golden_section_search(self.univariate_function, -10, 10, 4)
        st.write(f"For the example univariate function, $x^2 - 3.5x + 2.5$, the resulting bracket is **{bracket}** for an initial bracket of **[-10, 10]** for 4 iterations")

        golden_section_search_code = '''
def golden_section_search(self, function_to_optimize: typing.Callable, a:float, b:float, n:float) -> tuple:
  sqrt_five = math.sqrt(5)
  phi = (1 + sqrt_five) / 2
  rho = phi - 1
  d = rho * b + (1 - rho) * a
  yd = function_to_optimize(d)

  for i in range(1, n):
    c = rho * a + (1 - rho) * b
    yc = function_to_optimize(c)
    if yc < yd:
      b, d, yd = d, c, yc
    else:
      a, b = b, c

  return (round(a, 2), round(b, 2)) if a < b else (round(b, 2), round(a, 2))
'''
        st.code(golden_section_search_code, language="python")

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[i for i in range(-15, 16)], y=[self.univariate_function(i) for i in range(-15, 16)], mode='lines', name='Univariate Function'))
        fig.add_trace(go.Scatter(x=[x for x in bracket], y=[self.univariate_function(x) for x in bracket], mode='markers', name='Intervals'))
        fig.update_xaxes(title='x')
        fig.update_yaxes(title='f(x)')
        fig.update_layout(title='Bracket for the function, x**2 - 3.5*x + 2.5')
        st.plotly_chart(fig)


aforo_bracketing = AforO_Bracketing()
