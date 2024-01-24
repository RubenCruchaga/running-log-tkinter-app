from distutils.cmd import Command
import tkinter as tk

#custom function
def draw():
    try:
        d1=float(txt1.get())
        d2=float(txt3.get())
        d3=float(txt3.get())
        #d4=float(txt4.get())
        #d5=float(txt5.get())
        #d6=float(txt6.get())
        #d7=float(txt7.get())
        #gettinmg the varivle to the right size
        d1=350-d1
        d2=350-d2
        d3=350-d3
        #out line
        canvas.create_line(0,350,500,350)# work on this
        #the bar
        canvas.create_rectangle(10,d1,50,500)
        canvas.create_rectangle(60,d2,110,500)
        canvas.create_rectangle(120,d3,170,500)
    except ValueError:
        lblerror.config(text="ERROR only numbers")
def clear():
    canvas.delete("all")

#window properties
window = tk.Tk()
window.title('Graphing with Tkinter')
window.geometry('800x800')

#lables
lbl1 = tk.Label(window, text="Day 1:")
lbl2 = tk.Label(window, text="Day 2:")
lbl3 = tk.Label(window, text="Day 3:")
lbl4 = tk.Label(window, text="Day 4:")
lbl5 = tk.Label(window, text="Day 5:")
lbl6 = tk.Label(window, text="Day 6:")
lbl7 = tk.Label(window, text="Day 7:")
lblerror =tk.Label(window,text="")
#text boxes
txt1 = tk.Entry(window)
txt2 = tk.Entry(window)
txt3 = tk.Entry(window)
txt4 = tk.Entry(window)
txt5 = tk.Entry(window)
txt6 = tk.Entry(window)
txt7 = tk.Label(window)

#bottens
bnt = tk.Button(window,text="DRAW?", command=draw)
bntClear = tk.Button(window,text="Clear",command=clear)

#canvas
canvas = tk.Canvas(window,width=500,height=350)


#GUI 
#day area
lbl1.grid(row=0, column=0, padx=0, pady=5)
lbl2.grid(row=1, column=0, padx=0, pady=5)
lbl3.grid(row=2, column=0, padx=0, pady=5)
lbl4.grid(row=3, column=0, padx=0, pady=5)
txt1.grid(row=0, column=1,padx=0, pady=5)
txt2.grid(row=1, column=1,padx=0, pady=5)
txt3.grid(row=2, column=1,padx=0, pady=5)
txt4.grid(row=3, column=1,padx=0, pady=5)
lbl5.grid(row=4, column=0, padx=0, pady=5)
txt5.grid(row=4, column=1,padx=0, pady=5)
lbl6.grid(row=5, column=0, padx=0, pady=5)
txt6.grid(row=5, column=1,padx=0, pady=5)
lbl7.grid(row=6, column=0, padx=0, pady=5)
txt7.grid(row=6, column=1,padx=0, pady=5)
#the rest 
bnt.grid(row=6,column=3,padx=20,pady=0)
canvas.grid(row=7,column=3)
bntClear.grid(row=2,column=2,padx=20,pady=0)
lblerror.grid(row=4,column=4)
#build Window
window.mainloop()