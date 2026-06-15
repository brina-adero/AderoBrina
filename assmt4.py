import tkinter as tk
from tkinter import messagebox

# Math Functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error"
    return x / y

# Global Variables
first_number = 0.0
current_operator = ""

# Button Click Handlers
def press_num(number):
    current = display_entry.get()
    
    # If the user clicks '.' and there's already one on screen, ignore it to prevent syntax errors
    if number == "." and "." in current:
        return
        
    display_entry.delete(0, tk.END)
    display_entry.insert(0, str(current) + str(number))

def press_clear():
    global first_number, current_operator
    display_entry.delete(0, tk.END)
    first_number = 0.0
    current_operator = ""

def set_operator(op):
    global first_number, current_operator
    try:
        first_number = float(display_entry.get())
        current_operator = op
        display_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Error", "Please enter a number first")

def calculate_total():
    global first_number, current_operator
    try:
        second_number = float(display_entry.get())
        display_entry.delete(0, tk.END)
        
        if current_operator == "+":
            result = add(first_number, second_number)
        elif current_operator == "-":
            result = subtract(first_number, second_number)
        elif current_operator == "*":
            result = multiply(first_number, second_number)
        elif current_operator == "/":
            result = divide(first_number, second_number)
        else:
            display_entry.insert(0, "Error")
            return
            
        # Clean up result formatting: turn whole floats like 5.0 into an int (5)
        if isinstance(result, float) and result.is_integer():
            result = int(result)
            
        display_entry.insert(0, str(result))
    except ValueError:
        messagebox.showerror("Error", "Invalid Input")

# GUI Setup Layout
window = tk.Tk()
window.title("My Calculator ")

# Text Entry screen
display_entry = tk.Entry(window, width=20, font=("Arial", 16), justify="right")
display_entry.grid(row=0, column=0, columnspan=4, pady=10)

# Define buttons in a clean layout matrix (text, row, column)
button_layout = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("C", 4, 0), ("0", 4, 1), (".", 4, 2), ("+", 4, 3),
    ("=", 5, 0) 
]

# Create and grid buttons using a single loop
for text, row, col in button_layout:
    # Set the unique action for each button type
    if text == "C":
        action = press_clear
    elif text == "=":
        action = calculate_total
    elif text in ["+", "-", "*", "/"]:
        action = lambda val=text: set_operator(val)
    else:
        action = lambda val=text: press_num(val)

    # Build and place the button
    btn = tk.Button(window, text=text, padx=20, pady=20, command=action)
    
    # Let the Equals button stretch horizontally across all 4 columns for a cleaner layout
    if text == "=":
        btn.grid(row=row, column=col, columnspan=4, sticky="we")
    else:
        btn.grid(row=row, column=col)

# Run the program loop
window.mainloop()
