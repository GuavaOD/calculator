import tkinter as tk

calculation = ""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation)

# eval function takes the string expression as an argument and returns a float 
def eval_calculations():
    global calculation
    try:
        calculation = str(eval(calculation))
        text_result.delete(1.0, "end")
        text_result.insert(1.0, calculation)
    except:
        clr_display()
        text_result.insert(1.0, "Error")

def clr_display():
    global calculation
    calculation = ""
    text_result.delete(1.0, "end")


# building classic user interface (tk)
root = tk.Tk()
root.geometry("600x525")
# text field for results
text_result = tk.Text(root, height = 4, width = 32, font = ("Arial", 24))
text_result.grid(columnspan = 5)


# buttons on the calculator
button_1 = tk.Button(root, text = "1", command = lambda: add_to_calculation(1), width = 8, font = ("Arial", 16))
button_1.grid(row = 2, column = 1)
button_2 = tk.Button(root, text = "2", command = lambda: add_to_calculation(2), width = 8, font = ("Arial", 16))
button_2.grid(row = 2, column = 2)
button_3 = tk.Button(root, text = "3", command = lambda: add_to_calculation(3), width = 8, font = ("Arial", 16))
button_3.grid(row = 2, column = 3)
button_4 = tk.Button(root, text = "4", command = lambda: add_to_calculation(4), width = 8, font = ("Arial", 16))
button_4.grid(row = 3, column = 1)
button_5 = tk.Button(root, text = "5", command = lambda: add_to_calculation(5), width = 8, font = ("Arial", 16))
button_5.grid(row = 3, column = 2)
button_6 = tk.Button(root, text = "6", command = lambda: add_to_calculation(6), width = 8, font = ("Arial", 16))
button_6.grid(row = 3, column = 3)
button_7 = tk.Button(root, text = "7", command = lambda: add_to_calculation(7), width = 8, font = ("Arial", 16))
button_7.grid(row = 4, column = 1)
button_8 = tk.Button(root, text = "8", command = lambda: add_to_calculation(8), width = 8, font = ("Arial", 16))
button_8.grid(row = 4, column = 2)
button_9 = tk.Button(root, text = "9", command = lambda: add_to_calculation(9), width = 8, font = ("Arial", 16))
button_9.grid(row = 4, column = 3)
button_0 = tk.Button(root, text = "0", command = lambda: add_to_calculation(0), width = 8, font = ("Arial", 16))
button_0.grid(row = 5, column = 2)
button_plus = tk.Button(root, text = "+", command = lambda: add_to_calculation("+"), width = 8, font = ("Arial", 16))
button_plus.grid(row = 2, column = 4)
button_minus = tk.Button(root, text = "-", command = lambda: add_to_calculation("-"), width = 8, font = ("Arial", 16))
button_minus.grid(row = 3, column = 4)
button_mul = tk.Button(root, text = "*", command = lambda: add_to_calculation("*"), width = 8, font = ("Arial", 16))
button_mul.grid(row = 4, column = 4)
button_div = tk.Button(root, text = "/", command = lambda: add_to_calculation("/"), width = 8, font = ("Arial", 16))
button_div.grid(row = 5, column = 4)
button_open = tk.Button(root, text = "(", command = lambda: add_to_calculation("("), width = 8, font = ("Arial", 16))
button_open.grid(row = 5, column = 1)
button_close = tk.Button(root, text = ")", command = lambda: add_to_calculation(")"), width = 8, font = ("Arial", 16))
button_close.grid(row = 5, column = 3)
button_equal = tk.Button(root, text = "=", command = eval_calculations, width = 19, font = ("Arial", 16))
button_equal.grid(row = 6, column = 1, columnspan = 2)
button_clr = tk.Button(root, text = "Clr", command = clr_display, width = 19, font = ("Arial", 16))
button_clr.grid(row = 6, column = 3, columnspan = 2)

root.mainloop()
