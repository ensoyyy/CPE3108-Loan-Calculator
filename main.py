"""
Smart Loan Calculator - Main Entry Point
CPE 3108 Programming Project
Members: Daniel Jon Santos, John Enzu Inigo, Anjoe Paglinawan

"""

import tkinter as tk
from loan_calculator import LoanCalculator

if __name__ == "__main__":
    root = tk.Tk()
    app = LoanCalculator(root)
    root.mainloop()