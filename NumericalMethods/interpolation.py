"""
Interpolation Module
Contains functions for polynomial interpolation using Newton's Divided Difference method
"""

import numpy as np

def newton_divided_difference_interpolation(months, balances, target_month):
    """
    Perform polynomial interpolation using Newton's Divided Difference method.

    Args:
        months (list): List of month values (x-coordinates)
        balances (list): List of balance values (y-coordinates)
        target_month (float): Month to interpolate balance for

    Returns:
        float: Interpolated balance value
    """
    months = np.array(months, dtype=float)
    balances = np.array(balances, dtype=float)

    n = len(months)
    dd_table = np.zeros((n, n))
    dd_table[:, 0] = balances

    # Build divided difference table
    for j in range(1, n):
        for i in range(n - j):
            dd_table[i, j] = (dd_table[i + 1, j - 1] - dd_table[i, j - 1]) / (months[i + j] - months[i])

    # Calculate interpolated value
    result = dd_table[0, 0]
    term = 1
    for i in range(1, n):
        term *= (target_month - months[i - 1])
        result += dd_table[0, i] * term

    return result


def get_divided_difference_table(months, balances):
    """
    Generate the divided difference table for Newton's interpolation method.

    Args:
        months (list): List of month values
        balances (list): List of balance values

    Returns:
        numpy.ndarray: Divided difference table
    """
    months = np.array(months, dtype=float)
    balances = np.array(balances, dtype=float)

    n = len(months)
    dd_table = np.zeros((n, n))
    dd_table[:, 0] = balances

    for j in range(1, n):
        for i in range(n - j):
            dd_table[i, j] = (dd_table[i + 1, j - 1] - dd_table[i, j - 1]) / (months[i + j] - months[i])

    return dd_table


def format_newton_polynomial(dd_table, months):
    """
    Format the Newton polynomial equation as a string.

    Args:
        dd_table (numpy.ndarray): Divided difference table
        months (list): List of month values

    Returns:
        str: Formatted polynomial equation
    """
    n = len(months)
    equation = f"P(x) = {dd_table[0, 0]:.2f}"

    for i in range(1, min(4, n)):
        term = f" + ({dd_table[0, i]:.4f})"
        for j in range(i):
            term += f"(x - {months[j]:.0f})"
        equation += term

    if n > 4:
        equation += " + ... (higher order terms)"

    return equation