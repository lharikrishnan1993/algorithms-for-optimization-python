import streamlit as st
import numpy as np
import sympy as sy


class AforO_Derivates_And_Gradients:
    def __init__(self) -> None:
        pass

    def derivatives(self):
        st.subheader("Derivatives")
        st.write(
            "The *derivative* $f{'}(x)$ of a function $f$ of a single variable $x$ is the rate at which the value of $f$ change at $x$"
        )

        _, center, _ = st.columns([1, 1, 1])
        with center:
            code = """x = sy.symbols("x")\nf = x**2 + x/2 - sy.sin(x)/x\nprint(f)"""
            st.code(code, language="python")

            x = sy.symbols("x")
            f = x**2 + x / 2 - sy.sin(x) / x
            st.write(f)

            code = """dx = sy.diff(f)\nprint(dx)"""
            st.code(code, language="python")

            dx = sy.diff(f)
            st.write(dx)

        st.write(
            "The *directional derivative* $\Delta_{s} f(x)$ of a multivariate function $f$ is the instantaneous rate of change of $f(x)$ as $x$ is moved with velocity **$s$**."
        )
        st.write(
            "The directional derivative can be computed using the gradient of the function:"
        )
        _, center, _ = st.columns([1, 1, 1])
        with center:
            st.latex(r"""\Delta_{s} f(x) = \Delta f(x)^T s""")

    def numerical_differentiation(self):
        st.subheader("Numerical Differentiation")
        st.write(
            "The process of estimating derivatives numerically is refereed to as *numerical differentiation*."
        )

        st.write("Finite Difference Methods")
        st.write(
            "Finite difference methods compute the difference between two values that differ by a finite step size."
        )
        st.latex(
            r"""f{'}(x) = \frac{f(x + h) - f(x)}{h} = \frac{f(x + h/2) - f(x - h/2)}{h} = \frac{f(x) - f(x - h)}{h}"""
        )
        st.write(
            "Mathetically, the smaller step size $h$, the better the derivative estimate. Practically, values for $h$ that are too small can result in numerical cancellation errors."
        )

    def automatic_differentiation(self):
        st.subheader("Automatic Differentiation")
        st.write(
            "This makes use of a computational graph  to perform the differentiation. *Forward accumulation* will automatically differentiate a function using a single forward pass through the function's computaional graph. The method is iteratively expanding the chain rule of the inner equation."
        )

    def summary(self):
        st.subheader("Summary")
        st.write(
            "- Derivatives are useful in optimization because they provide information about how to change a given point in order to improve the objective function."
        )
        st.write(
            "- For multivariate functions, various derivartive based concepts are useful for directing the search for an optimum, including the gradient, the Hessian, and the directional directive."
        )
        st.write(
            "- Analytic differentiation methods include forward and reverse accumulation on computational graphs."
        )

    def run(self):
        _, center, _ = st.columns([1, 1, 1])
        with center:
            st.header("Chapter 02 - Derivatives and Gradients")
        self.derivatives()
        self.numerical_differentiation()
        self.automatic_differentiation()
        self.summary()


aforo_derivatives_and_gradients = AforO_Derivates_And_Gradients()
