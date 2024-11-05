import tkinter as tk
import math

root=tk.Tk()
root.title("Calculator")
root.configure(bg="#5b5bab")
root.resizable(width=False,height=False)

calculation="0"

def add(symbol):
    global calculation
    if calculation == "Error":
        calculation = str(symbol) 
    elif calculation == "0":
        calculation = str(symbol) 
    else:
        calculation += str(symbol)
    update_display()
    
def SQ_Root():
    global calculation
    try:
        calculation=f"{str(math.sqrt(float(calculation)))}"
       
    except (ValueError, ZeroDivisionError):
        calculation = "Error"
    update_display()
    
def evalute():
    global calculation
    try:
          calculation=str(eval(calculation.lstrip("0")or "0"))
        
    except (ZeroDivisionError, ValueError, SyntaxError):
        calculation = "Error"
    update_display()
         
def update_display():
    text_result.delete(1.0, "end")
    text_result.insert(1.0, calculation) 
    text_result.tag_configure("right", justify='right')
    text_result.tag_add("right", 1.0, "end")
    
def clear():
     global calculation
     calculation="0"
     update_display()



text_result=tk.Text(root , height=2, width=14,font=("Arial",24),fg="Darkblue",bg="#99edc3")
text_result.grid(columnspan=4)
update_display() 

btn_Clear=tk.Button(root,text="CE",command=clear,width=5,font=("Arial",14),fg="Red",bg="Black")
btn_Clear.grid(row=2,column=0)

btn_sqroot=tk.Button(root,text="√",command=SQ_Root,width=5,font=("Arial",14),fg="Green",bg="Black")
btn_sqroot.grid(row=2,column=1)

btn_divide=tk.Button(root,text="%",command=lambda:add('%'),width=5,font=("Arial",14),fg="Green",bg="Black")
btn_divide.grid(row=2,column=2)

btn_divide=tk.Button(root,text="/",command=lambda:add('/'),width=5,font=("Arial",14),fg="Green",bg="Black")
btn_divide.grid(row=2,column=3)



btn_1=tk.Button(root,text="7",command=lambda:add(7),width=5,font=("Arial",14),fg="Blue",bg="Black")
btn_1.grid(row=3,column=0)

btn_2=tk.Button(root,text="8",command=lambda:add(8),width=5,font=("Arial",14),fg="Blue",bg="Black")
btn_2.grid(row=3,column=1)

btn_3=tk.Button(root,text="9",command=lambda:add(9),width=5,font=("Arial",14),fg="Blue",bg="Black")
btn_3.grid(row=3,column=2)

btn_product=tk.Button(root,text="X",command=lambda:add('*'),width=5,font=("Arial",14),fg="Green",bg="Black")
btn_product.grid(row=3,column=3)


btn_4=tk.Button(root,text="4",command=lambda:add(4),width=5,font=("Arial",14),fg="Blue",bg="Black")
btn_4.grid(row=4,column=0)

btn_5=tk.Button(root,text="5",command=lambda:add(5),width=5,font=("Arial",14),fg="Blue",bg="Black")
btn_5.grid(row=4,column=1)

btn_6=tk.Button(root,text="6",command=lambda:add(6),width=5,font=("Arial",14),fg="Blue",bg="Black")
btn_6.grid(row=4,column=2)

btn_Minus=tk.Button(root,text="-",command=lambda:add('-'),width=5,font=("Arial",14),fg="Green",bg="Black")
btn_Minus.grid(row=4,column=3)



btn_7=tk.Button(root,text="1",command=lambda:add(1),width=5,font=("Arial",14),fg="Blue",bg="Black")
btn_7.grid(row=5,column=0)

btn_8=tk.Button(root,text="2",command=lambda:add(2),width=5,font=("Arial",14),fg="Blue",bg="Black")
btn_8.grid(row=5,column=1)

btn_9=tk.Button(root,text="3",command=lambda:add(3),width=5,font=("Arial",14),fg="Blue",bg="Black")
btn_9.grid(row=5,column=2)

btn_sum=tk.Button(root,text="+",command=lambda:add('+'),width=5,font=("Arial",14),fg="Green",bg="Black")
btn_sum.grid(row=5,column=3)




btn_10=tk.Button(root,text="0",command=lambda:add(0),width=5,font=("Arial",14),fg="Yellow",bg="Black")
btn_10.grid(row=6,column=0)

btn_11=tk.Button(root,text="00",command=lambda:add('00'),width=5,font=("Arial",14),fg="Yellow",bg="Black")
btn_11.grid(row=6,column=1)

btn_13=tk.Button(root,text=".",command=lambda:add('.'),width=5,font=("Arial",14),fg="olive",bg="Black")
btn_13.grid(row=6,column=2)

btn_equals=tk.Button(root,text="=",command=evalute,width=5,font=("Arial",14),fg="orange",bg="Black")
btn_equals.grid(row=6,column=3)


root.mainloop()


