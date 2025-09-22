import tkinter as tk
from tkinter import messagebox, ttk

# Store employees
myEmployees = {}

# Main App Window
root = tk.Tk()
root.title("Employee Management System")
root.geometry("750x500")
root.resizable(False, False)
root.configure(bg="#f0f4f7")

# ---------- Helper Functions ----------

def clear_inputs():
    emp_id_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    pay_entry.delete(0, tk.END)
    allowance_entry.delete(0, tk.END)
    deduction_entry.delete(0, tk.END)
    tax_entry.delete(0, tk.END)

def update_table():
    for i in tree.get_children():
        tree.delete(i)
    for emp_id, emp in myEmployees.items():
        tree.insert('', 'end', values=(
            emp["Employee ID"], emp["Employee Name"], emp["Basic Pay"],
            emp["Allowance"], emp["Deductions"], emp["NetPay"], emp["GrossPay"]
        ))

def add_employee():
    try:
        emp_id = emp_id_entry.get().strip()
        name = name_entry.get().strip()
        pay = int(pay_entry.get().strip())
        allowance = int(allowance_entry.get().strip())
        deduction = int(deduction_entry.get().strip())
        tax = int(tax_entry.get().strip())

        if not emp_id or not name:
            raise ValueError("ID and Name cannot be empty")

        net_pay = pay + allowance
        gross_pay = net_pay - (deduction + tax)

        myEmployees[emp_id] = {
            "Employee ID": emp_id,
            "Employee Name": name,
            "Basic Pay": pay,
            "Allowance": allowance,
            "Deductions": deduction,
            "NetPay": net_pay,
            "GrossPay": gross_pay
        }

        update_table()
        clear_inputs()
        messagebox.showinfo("Success", "Employee added successfully.")
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))

def delete_employee():
    emp_id = emp_id_entry.get().strip()
    if emp_id in myEmployees:
        del myEmployees[emp_id]
        update_table()
        clear_inputs()
        messagebox.showinfo("Deleted", f"Employee {emp_id} deleted.")
    else:
        messagebox.showerror("Error", "Employee ID not found.")

def modify_employee():
    try:
        emp_id = emp_id_entry.get().strip()
        if emp_id not in myEmployees:
            messagebox.showerror("Error", "Employee not found.")
            return

        name = name_entry.get().strip()
        pay = int(pay_entry.get().strip())
        allowance = int(allowance_entry.get().strip())
        deduction = int(deduction_entry.get().strip())
        tax = int(tax_entry.get().strip())

        net_pay = pay + allowance
        gross_pay = net_pay - (deduction + tax)

        myEmployees[emp_id] = {
            "Employee ID": emp_id,
            "Employee Name": name,
            "Basic Pay": pay,
            "Allowance": allowance,
            "Deductions": deduction,
            "NetPay": net_pay,
            "GrossPay": gross_pay
        }

        update_table()
        clear_inputs()
        messagebox.showinfo("Modified", f"Employee {emp_id} modified.")
    except ValueError as ve:
        messagebox.showerror("Input Error", str(ve))

# ---------- UI Layout ----------

# Input Frame
input_frame = tk.LabelFrame(root, text="Employee Details", padx=10, pady=10, bg="#e3eaf2")
input_frame.place(x=20, y=20, width=710, height=180)

tk.Label(input_frame, text="Employee ID:", bg="#e3eaf2").grid(row=0, column=0, padx=5, pady=5, sticky="e")
tk.Label(input_frame, text="Name:", bg="#e3eaf2").grid(row=0, column=2, padx=5, pady=5, sticky="e")
tk.Label(input_frame, text="Basic Pay:", bg="#e3eaf2").grid(row=1, column=0, padx=5, pady=5, sticky="e")
tk.Label(input_frame, text="Allowance:", bg="#e3eaf2").grid(row=1, column=2, padx=5, pady=5, sticky="e")
tk.Label(input_frame, text="Deductions:", bg="#e3eaf2").grid(row=2, column=0, padx=5, pady=5, sticky="e")
tk.Label(input_frame, text="Taxes:", bg="#e3eaf2").grid(row=2, column=2, padx=5, pady=5, sticky="e")

emp_id_entry = tk.Entry(input_frame)
name_entry = tk.Entry(input_frame)
pay_entry = tk.Entry(input_frame)
allowance_entry = tk.Entry(input_frame)
deduction_entry = tk.Entry(input_frame)
tax_entry = tk.Entry(input_frame)

emp_id_entry.grid(row=0, column=1, padx=5, pady=5)
name_entry.grid(row=0, column=3, padx=5, pady=5)
pay_entry.grid(row=1, column=1, padx=5, pady=5)
allowance_entry.grid(row=1, column=3, padx=5, pady=5)
deduction_entry.grid(row=2, column=1, padx=5, pady=5)
tax_entry.grid(row=2, column=3, padx=5, pady=5)

# Buttons
btn_frame = tk.Frame(root, bg="#f0f4f7")
btn_frame.place(x=20, y=210, width=710, height=50)

tk.Button(btn_frame, text="Add", width=12, command=add_employee, bg="#4CAF50", fg="white").grid(row=0, column=0, padx=10)
tk.Button(btn_frame, text="Modify", width=12, command=modify_employee, bg="#2196F3", fg="white").grid(row=0, column=1, padx=10)
tk.Button(btn_frame, text="Delete", width=12, command=delete_employee, bg="#f44336", fg="white").grid(row=0, column=2, padx=10)
tk.Button(btn_frame, text="Clear", width=12, command=clear_inputs, bg="#9E9E9E", fg="white").grid(row=0, column=3, padx=10)
tk.Button(btn_frame, text="Exit", width=12, command=root.destroy, bg="#FF9800", fg="white").grid(row=0, column=4, padx=10)

# Treeview (Display Table)
tree_frame = tk.Frame(root)
tree_frame.place(x=20, y=270, width=710, height=200)

scrollbar = tk.Scrollbar(tree_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tree = ttk.Treeview(tree_frame, columns=("ID", "Name", "Pay", "Allow", "Deduct", "Net", "Gross"), show='headings', yscrollcommand=scrollbar.set)
tree.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=tree.yview)

for col in ("ID", "Name", "Pay", "Allow", "Deduct", "Net", "Gross"):
    tree.heading(col, text=col)
    tree.column(col, width=90 if col != "Name" else 120)

# Run the app
root.mainloop()