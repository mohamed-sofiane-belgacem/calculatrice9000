import tkinter as tk

calculation=""

def add_to_calculation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)

def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")

def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")

def sqrt_calculation():
    global calculation
    try:
        number = float(calculation)
        guess = number / 2
        error = 0.00001
        while abs(guess*guess - number) > error:
            guess = (guess + number/guess) / 2
        calculation = guess
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")

def square_calculation():
    global calculation
    try:
        calculation = str(float(calculation) ** 2)
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")

def cube_calculation():
    global calculation
    try:
        calculation = str(float(calculation) ** 3)
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)
    except:
        clear_field()
        text_result.insert(1.0,"Error")

root=tk.Tk()
root.geometry("375x275")

text_result=tk.Text(root,height=2,width=16,font=('Arial',24))
text_result.grid(columnspan=5)

btn_1=tk.Button(root,text="1",bg="#70757A",fg="white",command=lambda:add_to_calculation(1),width=5,font=('Arial',14))
btn_1.grid(row=2,column=1)

btn_2=tk.Button(root,text="2",bg="#70757A",fg="white",command=lambda:add_to_calculation(2),width=5,font=('Arial',14))
btn_2.grid(row=2,column=2)

btn_3=tk.Button(root,text="3",bg="#70757A",fg="white",command=lambda:add_to_calculation(3),width=5,font=('Arial',14))
btn_3.grid(row=2,column=3)

btn_4=tk.Button(root,text="4",bg="#70757A",fg="white",command=lambda:add_to_calculation(4),width=5,font=('Arial',14))
btn_4.grid(row=3,column=1)

btn_5=tk.Button(root,text="5",bg="#70757A",fg="white",command=lambda:add_to_calculation(5),width=5,font=('Arial',14))
btn_5.grid(row=3,column=2)

btn_6=tk.Button(root,text="6",bg="#70757A",fg="white",command=lambda:add_to_calculation(6),width=5,font=('Arial',14))
btn_6.grid(row=3,column=3)

btn_7=tk.Button(root,text="7",bg="#70757A",fg="white",command=lambda:add_to_calculation(7),width=5,font=('Arial',14))
btn_7.grid(row=4,column=1)

btn_8=tk.Button(root,text="8",bg="#70757A",fg="white",command=lambda:add_to_calculation(8),width=5,font=('Arial',14))
btn_8.grid(row=4,column=2)

btn_9=tk.Button(root,text="9",bg="#70757A",fg="white",command=lambda:add_to_calculation(9),width=5,font=('Arial',14))
btn_9.grid(row=4,column=3)

btn_0=tk.Button(root,text="0",bg="#70757A",fg="white",command=lambda:add_to_calculation(0),width=5,font=('Arial',14))
btn_0.grid(row=5,column=2)

btn_plus=tk.Button(root,text="+",fg="white",bg="#ADB5BD",command=lambda:add_to_calculation("+"),width=5,font=('Arial',14))
btn_plus.grid(row=2,column=5)

btn_sous=tk.Button(root,text="-",fg="white",bg="#ADB5BD",command=lambda:add_to_calculation("-"),width=5,font=('Arial',14))
btn_sous.grid(row=3,column=5)

btn_div=tk.Button(root,text="/",fg="white",bg="#ADB5BD",command=lambda:add_to_calculation("/"),width=5,font=('Arial',14))
btn_div.grid(row=4,column=5)

btn_mul=tk.Button(root,text="x",fg="white",bg="#ADB5BD",command=lambda:add_to_calculation("*"),width=5,font=('Arial',14))
btn_mul.grid(row=5,column=5)

btn_cube=tk.Button(root,text="x³",bg="#F5DB5C",fg="white",command=cube_calculation,width=5,font=('Arial',14))
btn_cube.grid(row=5,column=3)

btn_equal=tk.Button(root,text="=",command=evaluate_calculation,width=10,font=('Arial',14))
btn_equal.grid(row=6,column=3,columnspan=2)

btn_clear=tk.Button(root,text="C",command=clear_field,width=10,font=('Arial',14))
btn_clear.grid(row=6,column=1,columnspan=2)

btn_sqrt=tk.Button(root,text="√ ",fg="white",bg="#F5DB5C",command=sqrt_calculation,width=5,font=('Arial',14))
btn_sqrt.grid(row=5,column=5)

btn_square=tk.Button(root, text="x^2",bg="#F5DB5C",fg="white",command=square_calculation,width=5,font=('Arial',14))
btn_square.grid(row=5,column=1)


root.mainloop()