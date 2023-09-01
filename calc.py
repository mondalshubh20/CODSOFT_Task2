import tkinter as tk

def on_button_click(symbol):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + symbol)

def calculate():
    try:
        expression = entry.get()
        result = eval(expression)
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Calculator for codsoft")

# Create an entry widget for displaying input and results
entry = tk.Entry(root, width=25, font=("Arial", 16))
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Create buttons for numbers and symbols
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+'
]

row_num = 1
col_num = 1

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=("Arial", 16), command=lambda b=button: on_button_click(b)).grid(row=row_num, column=col_num)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

# Create a button to clear the entry
clear_button = tk.Button(root, text="C", padx=20, pady=20, font=("Arial", 16), command=lambda: entry.delete(0, tk.END))
clear_button.grid(row=row_num, column=col_num)

# Create a button to calculate the result
equal_button = tk.Button(root, text="=", padx=20, pady=20, font=("Arial", 16), command=calculate)
equal_button.grid(row=row_num, column=col_num + 1)

root.mainloop()
