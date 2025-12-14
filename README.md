# CPE3108-Loan-Calculator
Smart Loan Calculator with Polynomial Interpolation - CPE 3108 Final Project

## Project Structure

```
CPE3108-Loan-Calculator/
├── main.py                     # 🚀 Application entry point
├── loan_calculator.py          # 🏗️  Main LoanCalculator GUI class
├── utils.py                   # 🛠️  Utility classes (ToolTip)
├── NumericalMethods/          # 🔢 Numerical methods package
│   ├── __init__.py
│   ├── loan_calculations.py   # 💰 Loan payment & amortization
│   └── interpolation.py       # 📈 Polynomial interpolation
├── requirements.txt            # 📦 Dependencies
└── README.md                  # 📖 Documentation
```

## Numerical Methods Implemented

### 🔢 Loan Calculations (`NumericalMethods/loan_calculations.py`)
- **Monthly Payment Calculation**: Standard amortization formula
- **Amortization Schedule Generation**: Complete monthly breakdown
- **Loan Totals**: Total paid and total interest calculations

### 📈 Polynomial Interpolation (`NumericalMethods/interpolation.py`)
- **Newton's Divided Difference Method**: For polynomial interpolation
- **Divided Difference Table Generation**: Complete table construction
- **Polynomial Equation Formatting**: Human-readable equation display

## Features

- 🧮 **Loan Calculation**: Calculate monthly payments, total interest, and loan summaries
- 📅 **Amortization Schedule**: View complete monthly breakdown with selection for interpolation
- 📈 **Polynomial Interpolation**: Predict remaining balance at any future month
- 💾 **Export to CSV**: Save amortization schedules
- 🎨 **Modern UI**: Clean, responsive interface with tooltips and validation

## Requirements

- Python 3.7+
- tkinter (usually included with Python)
- numpy

## Installation

1. Clone the repository:
```bash
git clone https://github.com/ensoyyy/CPE3108-Loan-Calculator.git
cd CPE3108-Loan-Calculator
```

3. Create Virtual Environment
```bash
python -m venv venv
```

4. Activate
```bash
.\venv\scripts\activate
```

5. Install dependencies:
```bash
pip install numpy
```

## Usage

Run the application:
```bash
python main.py
```

## Team Members

- Daniel Jon Santos
- John Enzu Inigo
- Anjoe Paglinawan

## License

This project is part of CPE 3108 Programming course work.
