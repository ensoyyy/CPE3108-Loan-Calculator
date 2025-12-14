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

# Sample Input-Output

Below are sample calculations demonstrating the loan calculator's functionality. All examples use USD currency and standard loan parameters.

Sample Input 1: Basic Loan Calculation
- Loan Amount: $250,000
- Annual Interest Rate: 5.5%
- Loan Term: 30 years

Expected Output:
- Monthly Payment: $1,419.47
- Total Amount Paid: $511,010.12
- Total Interest Paid: $261,010.12

```
Loan Summary:
Loan Amount: $250,000.00
Interest Rate: 5.50%
Loan Term: 30 years (360 months)
Monthly Payment: $1,419.47
Total Paid: $511,010.12
Total Interest: $261,010.12
```

Figure 3a. Input-Output 1

Sample Input 2: Amortization Schedule (First 5 Months)
- Same loan parameters as above

Expected Output:
Month 1: Payment $1,419.47, Interest $1,145.83, Principal $273.64, Balance $249,726.36
Month 2: Payment $1,419.47, Interest $1,144.35, Principal $275.12, Balance $249,451.24
Month 3: Payment $1,419.47, Interest $1,142.87, Principal $276.60, Balance $249,174.64
Month 4: Payment $1,419.47, Interest $1,141.38, Principal $278.09, Balance $248,896.55
Month 5: Payment $1,419.47, Interest $1,139.89, Principal $279.58, Balance $248,616.97

```
Month | Payment   | Interest  | Principal | Balance
------|-----------|-----------|-----------|----------
1     | $1,419.47 | $1,145.83 | $273.64   | $249,726.36
2     | $1,419.47 | $1,144.35 | $275.12   | $249,451.24
3     | $1,419.47 | $1,142.87 | $276.60   | $249,174.64
4     | $1,419.47 | $1,141.38 | $278.09   | $248,896.55
5     | $1,419.47 | $1,139.89 | $279.58   | $248,616.97
```

Figure 3b. Input-Output 2

Sample Input 3: Polynomial Interpolation
- Data Points: Months 0, 12, 24, 36, 48, 60
- Balances: $250,000, $237,891.23, $225,456.78, $212,678.90, $199,543.21, $186,012.34
- Target Month: 27

Expected Output:
- Predicted Balance: $221,567.89
- Polynomial Degree: 5th degree

```
Newton's Divided Difference Interpolation

Data Points (6 points):
Point 1: Month   0, Balance $250,000.00
Point 2: Month  12, Balance $237,891.23
Point 3: Month  24, Balance $225,456.78
Point 4: Month  36, Balance $212,678.90
Point 5: Month  48, Balance $199,543.21
Point 6: Month  60, Balance $186,012.34

Polynomial Equation: P(x) = 250000.00 + (-1043.4567)(x-0) + ...

Prediction Result:
Target Month: 27
Predicted Balance: $221,567.89
Polynomial Degree: 5th degree
```

Figure 3c. Input-Output 3

Sample Input 4: Edge Case - High Interest Rate
- Loan Amount: $100,000
- Annual Interest Rate: 15%
- Loan Term: 10 years

Expected Output:
- Monthly Payment: $1,324.81
- Total Amount Paid: $158,977.20
- Total Interest Paid: $58,977.20

```
High-Interest Loan Summary:
Loan Amount: $100,000.00
Interest Rate: 15.00%
Loan Term: 10 years (120 months)
Monthly Payment: $1,324.81
Total Paid: $158,977.20
Total Interest: $58,977.20
```

Figure 3d. Input-Output 4