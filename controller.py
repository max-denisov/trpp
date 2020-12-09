from sympy import *


def my_solve(equation):
    return solve(sympify("Eq(" + equation.replace("=", ",") + ")"))
