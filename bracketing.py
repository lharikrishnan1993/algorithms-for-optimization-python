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

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[i for i in range(-15, 16)], y=[self.univariate_function(i) for i in range(-15, 16)], mode='lines', name='Univariate Function'))
        fig.add_trace(go.Scatter(x=[x for x in bracket], y=[self.univariate_function(x) for x in bracket], mode='markers', name='Intervals'))
        fig.update_xaxes(title='x')
        fig.update_yaxes(title='f(x)')
        fig.update_layout(title='Bracket for the function, x**2 - 3.5*x + 2.5')
        st.plotly_chart(fig)

        st.subheader('Fibonacci Search')

        bracket = self.bracketer.fibonacci_search(self.univariate_function, -10, 10, 3)
        st.write(f"For the example univariate function, $x^2 - 3.5x + 2.5$, the resulting bracket is **{bracket}**")

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[i for i in range(-15, 16)], y=[self.univariate_function(i) for i in range(-15, 16)], mode='lines', name='Univariate Function'))
        fig.add_trace(go.Scatter(x=[x for x in bracket], y=[self.univariate_function(x) for x in bracket], mode='markers', name='Intervals'))
        fig.update_xaxes(title='x')
        fig.update_yaxes(title='f(x)')
        fig.update_layout(title='Bracket for the function, x**2 - 3.5*x + 2.5')
        st.plotly_chart(fig)

aforo_bracketing = AforO_Bracketing()
