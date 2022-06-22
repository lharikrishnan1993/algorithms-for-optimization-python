import streamlit as st


class AforO_Introduction:
    def __init__(self) -> None:
        pass

    def basic_optimization_problem(self):
        st.subheader("Basic Optimization Problem")
        st.write("The basic optimization problem is:")
        _, _, center, _, _ = st.columns([1, 1, 1, 1, 1])
        with center:
            st.latex(
                r"""
                $$
                $\underset{x}{\text{minimize}} \quad f(x) \\$
                $\text{subject to} \quad x \in \chi \\$
                $$
            """
            )

        st.write(
            "Here, $x$ is the design variable. $x$ can be adjusted to minimize the objective function $f$. The value of $x$ that minimizes the objective function is called the **minimizer** or **solution** and is usually represented as **$x^{*}$**"
        )

    def constraints(self):
        st.subheader("Constraints")
        st.write(
            "Constraints can be added to the optimization problem by restricting the feasible solution set $\chi$"
        )
        st.write("For example, consider the optimization problem:")
        _, _, center, _, _ = st.columns([1, 1, 1, 1, 1])
        with center:
            st.latex(
                r"""
                $$
                $\underset{x_1, x_2}{\text{minimize}} \quad f(x_1, x_2) \\$
                $\text{subject to} \\$
                $ \quad x_1 \geq 0 \\$
                $ \quad x_2 \geq 0 \\$
                $ \quad x_1 + x_2 \leq 1 \\$                
                $$
            """
            )

    def critical_points(self):
        st.subheader("Critical Points")
        st.write(
            "Unfortunately, it is generally difficult to prove that a given candidate point is at a global minimum unlesss we can exhaust the search space. The best check we can do is to check whether it is a local minimum. A point $x^*$ is at a local minimum if there exists a $\delta > 0$ such that $f(x^*) < f(x)$ for all $x$ with $|x - x^*| < \delta$."
        )
        st.write(
            "A local minima can be *strong local minima* or *weak local minima* depending on the whether the minimizing point is unique. If the minimizing point is the only candidate point within the \delta range, then it is classified as **strong local minima**."
        )
        st.write(
            "A derivative of **0.0** is a **necessary condition** but not a **sufficient condition**. Derivative of 0.0 could happen at local minima/maxima, global minima/maxima or even an inflection point, but a minima will definitely have the derivative as 0.0."
        )

    def conditions_for_local_minima(self):
        st.subheader("Conditions for Local Minima")
        st.write(
            "A design point is guaranteed to be at a strong local minimum if the local derivative is zero ad the second derivative is positive."
        )

        st.write("")
        st.write("Univariate")
        st.write("- $f{'}(x^*) = 0$, the *first order necessary condition*, **FONC**")
        st.write("- $f{''}(x^*) > 0$, the *second order necessary condition*, **SONC**")

        st.write("")
        st.write("Multivariate")
        st.write("- $\Delta f(x) = 0$, the *first order necessary condition*, **FONC**")
        st.write(
            "- $\Delta^2 f(x)$ is positive semidefinite, the *second order necessary condition*, **SONC**"
        )

        st.write(
            "While necessary for optimality, the **FONC** and **SONC** are not sufficient for optimality. For unconstrained optimization of a twice-differentiable function, a point is guaranteed to be at a strong local minimum if the **FONC** is satisfied and $\Delta^2 f(x)$ is positive definite. These conditions are collectively known as the *second ortder sufficient conditions*, **SOSC**."
        )

    def summary(self):
        st.subheader("Summary")
        st.write(
            "- Optimization in engineering is the process of finding the best system design subject to a set of constraints."
        )
        st.write(
            "- Optimization is concerned with finding global minima of a function."
        )
        st.write(
            "- Minima occurs where the gradient is zero, but zero-gradient does not imply optimality."
        )

    def run(self):
        _, center, _ = st.columns([1, 1, 1])
        with center:
            st.header("Chapter 01 - Introduction")
        self.basic_optimization_problem()
        self.constraints()
        self.critical_points()
        self.conditions_for_local_minima()
        self.summary()


aforo_introduction = AforO_Introduction()
