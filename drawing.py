from distutils.cmd import Command
import tkinter as tk

#custom function
def draw():
    canvas.delete("all")
    try:
        d1=float(txt1.get())
        d2=float(txt2.get())
        d3=float(txt3.get())
        d4=float(txt4.get())
        d5=float(txt5.get())
        d6=float(txt6.get())
        d7=float(txt7.get())
        #makes it better to see
        d1=d1*10
        d2=d2*10
        d3=d3*10
        d4=d4*10
        d5=d5*10
        d6=d6*10
        d7=d7*10
        #gettinmg the varivle to the right size
        d1=350-d1
        d2=350-d2
        d3=350-d3
        d4=350-d4
        d5=350-d5
        d6=350-d6
        d7=350-d7
        #out line
        canvas.create_line(2,1,2,351)
        canvas.create_line(0,351,500,351)# work on this
        #the bar
        canvas.create_rectangle(10,d1,50,500)
        canvas.create_rectangle(60,d2,100,500)
        canvas.create_rectangle(110,d3,150,500)
        canvas.create_rectangle(160,d4,200,500)
        canvas.create_rectangle(210,d5,250,500)
        canvas.create_rectangle(260,d6,300,500)
        canvas.create_rectangle(310,d7,350,500)
        #will make teh tick marcks every 50 pixles/5 miles
        x1=0
        y1=0
        x2=10
        y2=0
        for i in range(8):
            y1=y1+50
            y2=y2+50
            canvas.create_line(x1,y1,x2,y2)
    except ValueError:
        lblerror.config(text="ERROR only numbers")

#window properties
window = tk.Tk()
window.title('Running bar graph')
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
lblname = tk.Label(window, text="")
#text boxes
txt1 = tk.Entry(window)
txt2 = tk.Entry(window)
txt3 = tk.Entry(window)
txt4 = tk.Entry(window)
txt5 = tk.Entry(window)
txt6 = tk.Entry(window)
txt7 = tk.Entry(window)

#bottens
bnt = tk.Button(window,text="DRAW?", command=draw)


#canvas
canvas = tk.Canvas(window,width=360,height=350)


#GUI 
#day area
lbl1.grid(row=0, column=0, padx=0, pady=5)
lbl2.grid(row=1, column=0, padx=0, pady=5)
lbl3.grid(row=2, column=0, padx=0, pady=5)
lbl4.grid(row=3, column=0, padx=0, pady=5)
txt1.grid(row=0, column=1, padx=0, pady=5)
txt2.grid(row=1, column=1, padx=0, pady=5)
txt3.grid(row=2, column=1, padx=0, pady=5)
txt4.grid(row=3, column=1, padx=0, pady=5)
lbl5.grid(row=4, column=0, padx=0, pady=5)
txt5.grid(row=4, column=1, padx=0, pady=5)
lbl6.grid(row=5, column=0, padx=0, pady=5)
txt6.grid(row=5, column=1, padx=0, pady=5)
lbl7.grid(row=6, column=0, padx=0, pady=5)
txt7.grid(row=6, column=1, padx=0, pady=5)
#the rest 
lblname.grid(row=0, column=4, padx=)
bnt.grid(row=6,column=3,padx=20,pady=0)
canvas.grid(row=7,column=4)
lblerror.grid(row=4,column=4)
#build Window
window.mainloop()