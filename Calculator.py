import tkinter as tk
from tkinter import ttk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operator.get()
        
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 == 0:
                result = "Cannot divide by zero"
            else:
                result = num1 / num2
        else:
            result = "Invalid operation"
        
        result_label.config(text="Result: " + str(result))
    except ValueError:
        result_label.config(text="Invalid input")

window = tk.Tk()
window.title("Simple Calculator")

style = ttk.Style()
style.configure("TButton", padding=10, font=("Helvetica", 12))
style.configure("TLabel", font=("Helvetica", 12))

entry_num1 = tk.Entry(window, font=("Helvetica", 12))
entry_num2 = tk.Entry(window, font=("Helvetica", 12))

result_label = tk.Label(window, text="Result:", font=("Helvetica", 14))

operator = tk.StringVar()
operator.set("Addition")  
operator_dropdown = ttk.Combobox(window, textvariable=operator, values=["Addition", "Subtraction", "Multiplication", "Division"], font=("Helvetica", 12))

calculate_button = ttk.Button(window, text="Calculate", command=calculate)

entry_num1.grid(row=0, column=0, padx=10, pady=10)
entry_num2.grid(row=0, column=1, padx=10, pady=10)
operator_dropdown.grid(row=0, column=2, padx=10, pady=10)
calculate_button.grid(row=1, column=0, columnspan=3, padx=10, pady=10)
result_label.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

window.mainloop()
