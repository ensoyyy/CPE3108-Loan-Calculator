"""
Smart Loan Calculator with Polynomial Interpolation
CPE 3108 Programming Project
Members: Daniel Jon Santos, John Enzu Inigo, Anjoe Paglinawan

"""

import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext, filedialog
import numpy as np
from datetime import datetime, timedelta
import csv
import os
from utils import ToolTip
from NumericalMethods.loan_calculations import calculate_monthly_payment, generate_amortization_schedule, calculate_loan_totals
from NumericalMethods.interpolation import newton_divided_difference_interpolation, get_divided_difference_table, format_newton_polynomial

class LoanCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Loan Calculator")
        self.root.geometry("1000x800")
        
        # Apply modern styling
        style = ttk.Style()
        style.theme_use('clam')
        
        # Configure styles
        style.configure('TButton', font=('Segoe UI', 10, 'bold'), padding=8, relief='raised')
        style.configure('TLabel', font=('Segoe UI', 10), background='#f8f9fa')
        style.configure('TEntry', font=('Segoe UI', 10), padding=5, relief='solid', borderwidth=1)
        style.configure('TCombobox', font=('Segoe UI', 10), padding=5)
        style.configure('TNotebook', font=('Segoe UI', 10, 'bold'))
        style.configure('TNotebook.Tab', font=('Segoe UI', 9, 'bold'), padding=[10, 5])
        style.configure('Treeview', font=('Segoe UI', 9), rowheight=25, background='white', fieldbackground='white')
        style.configure('Treeview.Heading', font=('Segoe UI', 10, 'bold'), background='#e9ecef', relief='raised')
        style.configure('Card.TLabelframe', background='#f8f9fa', borderwidth=2, relief='solid')
        style.configure('Card.TLabelframe.Label', font=('Segoe UI', 11, 'bold'), background='#f8f9fa')
        
        # Create menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="About", command=self.show_about)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Create notebook (tabs)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create three tabs
        self.tab1 = ttk.Frame(self.notebook)
        self.tab2 = ttk.Frame(self.notebook)
        self.tab3 = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab1, text="Loan Calculator")
        self.notebook.add(self.tab2, text="Amortization Schedule")
        self.notebook.add(self.tab3, text="Polynomial Interpolation")
        
        # Initialize variables
        self.amortization_data = []
        self.selected_points = []
        
        # Setup each tab
        self.setup_calculator_tab()
        self.setup_amortization_tab()
        self.setup_interpolation_tab()
        
    def show_about(self):
        """Show about dialog"""
        about_text = """🧮 Smart Loan Calculator with Polynomial Interpolation

📚 CPE 3108 Programming Project

👥 Developed by:
   • Daniel Jon Santos
   • John Enzu Inigo  
   • Anjoe Paglinawan

✨ Features:
   • 📊 Loan payment calculation
   • 📅 Amortization schedule generation
   • 📈 Polynomial interpolation for balance prediction
   • 💾 Export to CSV functionality
   • 🎨 Modern, user-friendly interface

📅 Version: 2.0
🗓️  Date: December 2025

🎉 Thank you for using our calculator!"""
        
        # Create a custom about dialog
        about_window = tk.Toplevel(self.root)
        about_window.title("About - Smart Loan Calculator")
        about_window.geometry("500x400")
        about_window.resizable(False, False)
        about_window.configure(bg='#f8f9fa')
        
        # Center the window
        about_window.transient(self.root)
        about_window.grab_set()
        
        # Content
        title_label = tk.Label(about_window, text="🧮 Smart Loan Calculator", 
                              font=('Segoe UI', 16, 'bold'), bg='#f8f9fa', fg='#007bff')
        title_label.pack(pady=20)
        
        text_widget = tk.Text(about_window, wrap=tk.WORD, font=('Segoe UI', 10), 
                             bg='#f8f9fa', relief='flat', height=15, width=50)
        text_widget.insert(tk.END, about_text)
        text_widget.config(state='disabled')
        text_widget.pack(padx=20, pady=10)
        
        # OK button
        ok_btn = ttk.Button(about_window, text="OK", command=about_window.destroy)
        ok_btn.pack(pady=20)
        
    def setup_calculator_tab(self):
        """Tab 1: Basic Loan Calculator"""
        frame = ttk.LabelFrame(self.tab1, text="Loan Information", padding=20, style='Card.TLabelframe')
        frame.pack(fill='both', expand=True, padx=30, pady=30)
        
        # Input fields
        ttk.Label(frame, text="Loan Amount ($):").grid(row=0, column=0, sticky='w', pady=10)
        self.amount_entry = ttk.Entry(frame, width=25)
        self.amount_entry.grid(row=0, column=1, pady=10, padx=(10,0))
        self.amount_entry.insert(0, "250000")
        ToolTip(self.amount_entry, "Enter the total loan amount (e.g., 250000)")
        
        ttk.Label(frame, text="Annual Interest Rate (%):").grid(row=1, column=0, sticky='w', pady=10)
        self.rate_entry = ttk.Entry(frame, width=25)
        self.rate_entry.grid(row=1, column=1, pady=10, padx=(10,0))
        self.rate_entry.insert(0, "5.5")
        ToolTip(self.rate_entry, "Enter the annual interest rate as a percentage (e.g., 5.5)")
        
        ttk.Label(frame, text="Loan Term (Years):").grid(row=2, column=0, sticky='w', pady=10)
        self.term_entry = ttk.Entry(frame, width=25)
        self.term_entry.grid(row=2, column=1, pady=10, padx=(10,0))
        self.term_entry.insert(0, "30")
        ToolTip(self.term_entry, "Enter the loan term in years (e.g., 30)")
        
        ttk.Label(frame, text="Currency:").grid(row=3, column=0, sticky='w', pady=10)
        self.currency_var = tk.StringVar(value="USD")
        currency_combo = ttk.Combobox(frame, textvariable=self.currency_var, 
                                      values=["USD", "PHP"], width=23, state='readonly')
        currency_combo.grid(row=3, column=1, pady=10, padx=(10,0))
        ToolTip(currency_combo, "Select the currency for display")
        
        # Calculate button
        calc_btn = ttk.Button(frame, text="📊 Calculate Loan", command=self.calculate_loan)
        calc_btn.grid(row=4, column=0, columnspan=2, pady=25)
        
        # Results display
        results_frame = ttk.LabelFrame(frame, text="Calculation Results", padding=10)
        results_frame.grid(row=5, column=0, columnspan=2, pady=15, sticky='ew')
        
        self.result_text = scrolledtext.ScrolledText(results_frame, width=70, height=18, wrap=tk.WORD, font=('Consolas', 10))
        self.result_text.pack(fill='both', expand=True)
        
    def setup_amortization_tab(self):
        """Tab 2: Amortization Schedule"""
        frame = ttk.Frame(self.tab2, padding=20)
        frame.pack(fill='both', expand=True)
        
        # Button frame
        btn_frame = ttk.Frame(self.tab2)
        btn_frame.pack(fill='x', padx=30, pady=10)
        
        # Configure grid weights for responsive layout
        btn_frame.grid_columnconfigure(0, weight=1)
        btn_frame.grid_columnconfigure(1, weight=1)
        
        ttk.Button(btn_frame, text="🎯 Auto-Select Every 12 Months", 
                  command=self.auto_select_points).grid(row=0, column=0, padx=5, pady=5, sticky='ew')
        ttk.Button(btn_frame, text="🧹 Clear Selection", 
                  command=self.clear_selection).grid(row=0, column=1, padx=5, pady=5, sticky='ew')
        ttk.Button(btn_frame, text="💾 Export to CSV", 
                  command=self.export_to_csv).grid(row=1, column=0, padx=5, pady=5, sticky='ew')
        ttk.Button(btn_frame, text="📈 Use Selected for Interpolation", 
                  command=self.prepare_interpolation).grid(row=1, column=1, padx=5, pady=5, sticky='ew')
        
        # Info label
        info_label = ttk.Label(frame, text="📅 Full amortization schedule - scroll to view all months", 
                              font=('Segoe UI', 10, 'italic'))
        info_label.pack(pady=5)
        
        # Treeview for amortization table
        columns = ('Month', 'Payment', 'Interest', 'Principal', 'Balance', 'Select')
        self.amort_tree = ttk.Treeview(frame, columns=columns, show='headings', height=20)
        
        for col in columns:
            self.amort_tree.heading(col, text=col)
            if col == 'Month':
                self.amort_tree.column(col, width=80)
            elif col == 'Select':
                self.amort_tree.column(col, width=100)
            else:
                self.amort_tree.column(col, width=120)
        
        # Scrollbar
        scrollbar = ttk.Scrollbar(frame, orient='vertical', command=self.amort_tree.yview)
        self.amort_tree.configure(yscrollcommand=scrollbar.set)
        
        self.amort_tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
        
        # Bind click event
        self.amort_tree.bind('<Double-1>', self.toggle_row_selection)
        
    def setup_interpolation_tab(self):
        """Tab 3: Polynomial Interpolation"""
        frame = ttk.Frame(self.tab3, padding=20)
        frame.pack(fill='both', expand=True)
        
        # Left side: Data points input
        left_frame = ttk.LabelFrame(frame, text="📊 Data Points (Minimum 4)", padding=15, style='Card.TLabelframe')
        left_frame.pack(side='left', fill='both', expand=True, padx=(0,10))
        
        # Data points treeview
        columns = ('Point', 'Month', 'Balance')
        self.points_tree = ttk.Treeview(left_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            self.points_tree.heading(col, text=col)
            self.points_tree.column(col, width=100)
        
        self.points_tree.pack(fill='both', expand=True)
        
        # Right side: Results
        right_frame = ttk.LabelFrame(frame, text="🔮 Interpolation Results", padding=15, style='Card.TLabelframe')
        right_frame.pack(side='right', fill='both', expand=True, padx=(10,0))
        
        # Target month input
        input_frame = ttk.Frame(right_frame)
        input_frame.pack(fill='x', pady=10)
        
        ttk.Label(input_frame, text="🎯 Target Month:").pack(side='left', padx=5)
        self.target_month_entry = ttk.Entry(input_frame, width=15)
        self.target_month_entry.pack(side='left', padx=5)
        self.target_month_entry.insert(0, "27")
        ToolTip(self.target_month_entry, "Enter the month number to predict the remaining balance")
        
        ttk.Button(input_frame, text="⚡ Calculate Polynomial", 
                  command=self.calculate_interpolation).pack(side='left', padx=10)
        
        # Results display
        self.interp_result_text = scrolledtext.ScrolledText(right_frame, width=55, height=28, wrap=tk.WORD, font=('Consolas', 9))
        self.interp_result_text.pack(fill='both', expand=True, pady=10)
        
    def calculate_loan(self):
        """Calculate monthly payment and generate amortization schedule"""
        try:
            # Get inputs
            principal = float(self.amount_entry.get())
            annual_rate = float(self.rate_entry.get())
            years = int(self.term_entry.get())
            currency = self.currency_var.get()
            
            # Calculate number of payments
            num_payments = years * 12
            
            # Validate inputs
            if principal <= 0:
                messagebox.showerror("Invalid Input", "Loan amount must be greater than 0.")
                self.amount_entry.focus()
                return
            if principal > 10000000:
                messagebox.showerror("Invalid Input", "Loan amount cannot exceed $10,000,000.")
                self.amount_entry.focus()
                return
            if annual_rate <= 0 or annual_rate > 30:
                messagebox.showerror("Invalid Input", "Interest rate must be between 0.01% and 30%.")
                self.rate_entry.focus()
                return
            if years <= 0 or years > 50:
                messagebox.showerror("Invalid Input", "Loan term must be between 1 and 50 years.")
                self.term_entry.focus()
                return
            
            # Calculate monthly payment
            monthly_payment = calculate_monthly_payment(principal, annual_rate, years)
            total_paid = monthly_payment * num_payments
            total_interest = total_paid - principal
            
            # Generate amortization schedule
            self.amortization_data = generate_amortization_schedule(principal, annual_rate, years)
            
            # Display results
            symbol = "$" if currency == "USD" else "₱"
            result = f"""
╔{'═'*68}╗
║{' '*20}🏠 LOAN SUMMARY {' '*30}║
╠{'═'*68}╣
║  💰 Loan Amount:          {symbol}{principal:>12,.2f} {' '*20}║
║  📈 Interest Rate:        {annual_rate:>12.2f}% per year {' '*14}║
║  ⏰ Loan Term:            {years:>12.0f} years ({num_payments:>3.0f} months){' '*8}║
╠{'═'*68}╣
║  💳 Monthly Payment:      {symbol}{monthly_payment:>12,.2f} {' '*20}║
║  💸 Total Amount Paid:    {symbol}{total_paid:>12,.2f} {' '*20}║
║  📊 Total Interest Paid:  {symbol}{total_interest:>12,.2f} {' '*20}║
╚{'═'*68}╝

✅ Calculation complete!
📊 Amortization schedule generated ({num_payments} months)
📈 Go to "Amortization Schedule" tab to view details
🎯 Select data points for polynomial interpolation
"""
            
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(1.0, result)
            
            # Populate amortization table (show first 12 and last 12 months)
            self.populate_amortization_table()
            
            messagebox.showinfo("Success", "Loan calculated successfully!")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    
    def populate_amortization_table(self):
        """Populate the amortization table with all months"""
        try:
            # Clear existing data
            for item in self.amort_tree.get_children():
                self.amort_tree.delete(item)
        except AttributeError:
            # amort_tree not created yet
            return
        
        if not self.amortization_data:
            return
        
        currency = "$" if self.currency_var.get() == "USD" else "₱"
        
        # Show all months
        for data in self.amortization_data:
            self.amort_tree.insert('', 'end', values=(
                data['month'],
                f"{currency}{data['payment']:,.2f}",
                f"{currency}{data['interest']:,.2f}",
                f"{currency}{data['principal']:,.2f}",
                f"{currency}{data['balance']:,.2f}",
                "☐"  # Modern checkbox symbol
            ), tags=('selectable',))
        
        # Bind click event
        self.amort_tree.bind('<Double-1>', self.toggle_row_selection)
    
    def toggle_row_selection(self, event):
        """Toggle row selection for interpolation"""
        if not self.amort_tree.selection():
            return
        item = self.amort_tree.selection()[0]
        values = list(self.amort_tree.item(item, 'values'))
        
        if values[0] == '...':
            return
        
        # Toggle selection marker
        if values[5] == "☐":
            values[5] = "☑"
        else:
            values[5] = "☐"
        
        self.amort_tree.item(item, values=values)
    
    def auto_select_points(self):
        """Auto-select every 12 months for interpolation"""
        if not self.amortization_data:
            messagebox.showwarning("Warning", "Generate loan calculation first!")
            return
        
        self.clear_selection()
        
        # Select every 12 months starting from 0
        selected_months = list(range(0, len(self.amortization_data) + 1, 12))
        
        count = 0
        for item in self.amort_tree.get_children():
            values = list(self.amort_tree.item(item, 'values'))
            if values[0] != '...' and int(values[0]) in selected_months:
                values[5] = "☑"
                self.amort_tree.item(item, values=values)
                count += 1
        
        messagebox.showinfo("Success", f"Auto-selected {count} data points")
    
    def clear_selection(self):
        """Clear all selections"""
        for item in self.amort_tree.get_children():
            values = list(self.amort_tree.item(item, 'values'))
            if values[0] != '...':
                values[5] = "☐"
                self.amort_tree.item(item, values=values)
    
    def export_to_csv(self):
        """Export amortization schedule to CSV"""
        if not self.amortization_data:
            messagebox.showwarning("Warning", "Generate loan calculation first!")
            return
        
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", 
                                                filetypes=[("CSV files", "*.csv")],
                                                title="Save Amortization Schedule")
        if not file_path:
            return
        
        try:
            with open(file_path, 'w', newline='') as csvfile:
                fieldnames = ['Month', 'Payment', 'Interest', 'Principal', 'Balance']
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                for data in self.amortization_data:
                    writer.writerow({
                        'Month': data['month'],
                        'Payment': f"{data['payment']:.2f}",
                        'Interest': f"{data['interest']:.2f}",
                        'Principal': f"{data['principal']:.2f}",
                        'Balance': f"{data['balance']:.2f}"
                    })
            messagebox.showinfo("Success", f"Amortization schedule exported to {os.path.basename(file_path)}")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to export: {str(e)}")
    
    def prepare_interpolation(self):
        """Prepare selected points for interpolation"""
        self.selected_points = []
        
        # Get selected rows
        for item in self.amort_tree.get_children():
            values = self.amort_tree.item(item, 'values')
            if values[5] == "☑":
                month = int(values[0])
                # Get balance from original data
                balance = self.amortization_data[month - 1]['balance'] if month > 0 else float(self.amount_entry.get())
                self.selected_points.append((month, balance))
        
        # Add month 0 if not included
        if self.selected_points and self.selected_points[0][0] != 0:
            principal = float(self.amount_entry.get())
            self.selected_points.insert(0, (0, principal))
        
        if len(self.selected_points) < 4:
            messagebox.showerror("Error", "Please select at least 4 data points!\n" + 
                               "Tip: Use 'Auto-Select Every 12 Months' button")
            return
        
        # Populate points tree
        for item in self.points_tree.get_children():
            self.points_tree.delete(item)
        
        currency = "$" if self.currency_var.get() == "USD" else "₱"
        for i, (month, balance) in enumerate(self.selected_points):
            self.points_tree.insert('', 'end', values=(i + 1, month, f"{currency}{balance:,.2f}"))
        
        # Switch to interpolation tab
        self.notebook.select(self.tab3)
        messagebox.showinfo("Success", f"Loaded {len(self.selected_points)} data points for interpolation!")
    
    def calculate_interpolation(self):
        """Calculate polynomial interpolation using Newton's Divided Difference"""
        if len(self.selected_points) < 4:
            messagebox.showerror("Error", "Need at least 4 data points!")
            return
        
        try:
            target_month = float(self.target_month_entry.get())
            
            # Extract x and y values
            months = np.array([point[0] for point in self.selected_points])
            balances = np.array([point[1] for point in self.selected_points])
            
            # Calculate polynomial value at target month
            result = newton_divided_difference_interpolation(months, balances, target_month)
            
            # Build divided difference table for display
            dd_table = get_divided_difference_table(months, balances)
            
            # Display results
            currency = "$" if self.currency_var.get() == "USD" else "₱"
            n = len(self.selected_points)
            degree = n - 1
            
            output = f"""
{'='*70}
           NEWTON'S DIVIDED DIFFERENCE INTERPOLATION
{'='*70}

DATA POINTS ({n} points):
"""
            for i, (month, balance) in enumerate(self.selected_points):
                output += f"  Point {i + 1}: Month {month:>3}, Balance {currency}{balance:>12,.2f}\n"
            
            output += f"\n{'='*70}\nDIVIDED DIFFERENCE TABLE:\n{'='*70}\n"
            output += f"{'Point':<8} {'Month':<8} {'f(x)':<15}"
            for j in range(1, min(5, n)):
                output += f" {j}st Diff" if j == 1 else f" {j}nd Diff" if j == 2 else f" {j}rd Diff" if j == 3 else f" {j}th Diff"
            output += "\n" + "-" * 70 + "\n"
            
            for i in range(n):
                output += f"{i:<8} {months[i]:<8.0f} {dd_table[i, 0]:<15,.2f}"
                for j in range(1, min(5, n - i)):
                    output += f" {dd_table[i, j]:<10,.4f}"
                output += "\n"
            
            output += f"\n{'='*70}\nPOLYNOMIAL EQUATION (Newton Form):\n{'='*70}\n"
            output += format_newton_polynomial(dd_table, months)
            
            output += f"\n{'='*70}\n"
            output += f"Polynomial Degree: {degree}{'st' if degree == 1 else 'nd' if degree == 2 else 'rd' if degree == 3 else 'th'} degree"
            output += f"\nNumber of Data Points: {n}"
            output += f"\n{'='*70}\n\n"
            
            output += f"""╔{'='*68}╗
║{' '*20}PREDICTION RESULT{' '*30}║
╠{'='*68}╣
║  Target Month:        {target_month:<45.0f} ║
║  Predicted Balance:   {currency}{result:<43,.2f} ║
║  Polynomial Degree:   {degree}{'st' if degree == 1 else 'nd' if degree == 2 else 'rd' if degree == 3 else 'th'} degree{' ' * (43 - len(str(degree)) - 9)} ║
║  Method Used:         Newton's Divided Difference{' ' * 18} ║
╚{'='*68}╝

✓ Polynomial passes through all {n} data points
✓ Prediction calculated successfully
"""
            
            self.interp_result_text.delete(1.0, tk.END)
            self.interp_result_text.insert(1.0, output)
            
            messagebox.showinfo("Success", f"Predicted balance at month {target_month}: {currency}{result:,.2f}")
            
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid target month!")
        except Exception as e:
            messagebox.showerror("Error", f"Calculation error: {str(e)}")