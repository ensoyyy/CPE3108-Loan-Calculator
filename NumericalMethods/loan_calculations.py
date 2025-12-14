"""
Loan Calculations Module
Contains functions for calculating loan payments and amortization schedules
"""

def calculate_monthly_payment(principal, annual_rate, years):
    """
    Calculate the monthly payment for a loan using the standard amortization formula.

    Args:
        principal (float): Loan amount
        annual_rate (float): Annual interest rate as percentage
        years (int): Loan term in years

    Returns:
        float: Monthly payment amount
    """
    monthly_rate = annual_rate / 100 / 12
    num_payments = years * 12

    if monthly_rate == 0:
        return principal / num_payments

    return principal * (monthly_rate * (1 + monthly_rate)**num_payments) / \
           ((1 + monthly_rate)**num_payments - 1)


def generate_amortization_schedule(principal, annual_rate, years):
    """
    Generate a complete amortization schedule for a loan.

    Args:
        principal (float): Loan amount
        annual_rate (float): Annual interest rate as percentage
        years (int): Loan term in years

    Returns:
        list: List of dictionaries containing monthly payment details
    """
    monthly_payment = calculate_monthly_payment(principal, annual_rate, years)
    monthly_rate = annual_rate / 100 / 12
    num_payments = years * 12

    amortization_data = []
    balance = principal

    for month in range(1, num_payments + 1):
        interest_payment = balance * monthly_rate
        principal_payment = monthly_payment - interest_payment
        balance -= principal_payment

        if balance < 0:
            balance = 0

        amortization_data.append({
            'month': month,
            'payment': monthly_payment,
            'interest': interest_payment,
            'principal': principal_payment,
            'balance': balance
        })

    return amortization_data


def calculate_loan_totals(principal, annual_rate, years):
    """
    Calculate total amounts paid and total interest for a loan.

    Args:
        principal (float): Loan amount
        annual_rate (float): Annual interest rate as percentage
        years (int): Loan term in years

    Returns:
        tuple: (monthly_payment, total_paid, total_interest)
    """
    monthly_payment = calculate_monthly_payment(principal, annual_rate, years)
    total_paid = monthly_payment * years * 12
    total_interest = total_paid - principal

    return monthly_payment, total_paid, total_interest