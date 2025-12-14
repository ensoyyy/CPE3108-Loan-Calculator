# Main

The Smart Loan Calculator is a GUI application built with Python's tkinter library that provides loan calculation, amortization scheduling, and polynomial interpolation features. The program consists of three main tabs: Loan Calculator, Amortization Schedule, and Polynomial Interpolation. Users can input loan parameters to calculate monthly payments and view detailed amortization schedules, then select data points for polynomial interpolation to predict future balances.

```
+---------------------+
|      Start          |
+---------------------+
           |
           v
+---------------------+
|  Import Modules     |
+---------------------+
           |
           v
+---------------------+
|  Initialize Tkinter |
+---------------------+
           |
           v
+---------------------+
|  Create GUI Tabs    |
+---------------------+
           |
           v
+---------------------+
|  Setup Calculator   |
|     Tab             |
+---------------------+
           |
           v
+---------------------+
|  Setup Amortization |
|     Tab             |
+---------------------+
           |
           v
+---------------------+
|  Setup Interpolation|
|     Tab             |
+---------------------+
           |
           v
+---------------------+
|  Display GUI        |
+---------------------+
           |
           v
+---------------------+
|  Wait for User      |
|  Interactions       |
+---------------------+
           |
           v
+---------------------+
|      End            |
+---------------------+
```

Figure 2.1a. Main Flowchart

# Function/Module 1

The loan calculations module ([`NumericalMethods/loan_calculations.py`](NumericalMethods/loan_calculations.py )) contains three core functions for financial computations: [`calculate_monthly_payment`](NumericalMethods/loan_calculations.py ), [`generate_amortization_schedule`](NumericalMethods/loan_calculations.py ), and [`calculate_loan_totals`](NumericalMethods/loan_calculations.py ). These functions implement standard amortization formulas to compute loan payments and schedules. The monthly payment calculation uses the standard loan formula, while the amortization schedule generates a month-by-month breakdown of payments, interest, and remaining balance.

```
+---------------------+
|  Input Parameters   |
|  (Principal, Rate,  |
|   Years)            |
+---------------------+
           |
           v
+---------------------+
|  Validate Inputs    |
+---------------------+
           |
           v
+---------------------+
|  Calculate Monthly  |
|  Payment            |
+---------------------+
           |
           v
+---------------------+
|  Generate Schedule  |
|  Loop for Each Month|
+---------------------+
           |
           v
+---------------------+
|  Calculate Interest |
|  for Month          |
+---------------------+
           |
           v
+---------------------+
|  Calculate Principal|
|  Payment            |
+---------------------+
           |
           v
+---------------------+
|  Update Balance     |
+---------------------+
           |
           v
+---------------------+
|  Store Month Data   |
+---------------------+
           |
           v
+---------------------+
|  Loop End?          |
+---------------------+
    |          |
    | No       | Yes
    v          v
+---------------------+
|  Calculate Totals   |
+---------------------+
           |
           v
+---------------------+
|  Return Results     |
+---------------------+
```

Figure 2.1b. Function/Module 1 Flowchart

# Function/Module 2

The interpolation module ([`NumericalMethods/interpolation.py`](NumericalMethods/interpolation.py )) implements Newton's Divided Difference method for polynomial interpolation. It consists of three functions: [`newton_divided_difference_interpolation`](NumericalMethods/interpolation.py ) for computing interpolated values, [`get_divided_difference_table`](NumericalMethods/interpolation.py ) for building the divided difference table, and [`format_newton_polynomial`](NumericalMethods/interpolation.py ) for displaying the polynomial equation. The module uses NumPy for efficient numerical computations and can handle up to 4th-degree polynomials with higher-order terms truncated for display.

```
+---------------------+
|  Input Data Points  |
|  (Months, Balances) |
+---------------------+
           |
           v
+---------------------+
|  Validate Data      |
|  (Min 4 points)     |
+---------------------+
           |
           v
+---------------------+
|  Initialize Divided |
|  Difference Table   |
+---------------------+
           |
           v
+---------------------+
|  Build Table        |
|  (Compute Differences|
|   for each order)    |
+---------------------+
           |
           v
+---------------------+
|  Input Target Month |
+---------------------+
           |
           v
+---------------------+
|  Calculate          |
|  Interpolated Value |
+---------------------+
           |
           v
+---------------------+
|  Format Polynomial  |
|  Equation           |
+---------------------+
           |
           v
+---------------------+
|  Display Results    |
+---------------------+
```

Figure 2.1c. Function/Module 2 Flowchart
