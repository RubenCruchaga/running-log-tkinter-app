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
        canvas.create_line(0,351,500,351)
        #draws the br graph
        canvas.create_rectangle(10,d1,50,500, fill='#E56A6A')
        canvas.create_rectangle(60,d2,100,500,fill='#E5A022')
        canvas.create_rectangle(110,d3,150,500,fill="#E0DB47")
        canvas.create_rectangle(160,d4,200,500,fill="#64AF52")
        canvas.create_rectangle(210,d5,250,500,fill="#527AAF")
        canvas.create_rectangle(260,d6,300,500,fill="#934ABA")
        canvas.create_rectangle(310,d7,350,500,fill="#D340B2")
        #will make teh tick marcks every 50 pixles/5 miles
        x1=0
        y1=0
        x2=10
        y2=0
        #draws the dashed lines
        for i in range(8):
            y1=y1+50
            y2=y2+50
            canvas.create_line(x1,y1,x2,y2)
            #the error code that the user sees
    except ValueError:
        lblerror.config(text="ERROR: only numbers")

#window properties
window = tk.Tk()
window.title('Running bar graph')
window.geometry('800x800') 
window.config(bg = "#6AE1E0")
#lables
lbl1 = tk.Label(window, text="Day 1:",bg='#E56A6A')
lbl2 = tk.Label(window, text="Day 2:",bg='#E5A022')
lbl3 = tk.Label(window, text="Day 3:",bg="#E0DB47")
lbl4 = tk.Label(window, text="Day 4:",bg="#64AF52")
lbl5 = tk.Label(window, text="Day 5:",bg="#527AAF")
lbl6 = tk.Label(window, text="Day 6:",bg="#934ABA")
lbl7 = tk.Label(window, text="Day 7:",bg="#D340B2")
lblerror =tk.Label(window,text="",bg="#6AE1E0")
lblname = tk.Label(window, text="Running log",bg="#6AE1E0",font=("times new roman",15))

#intruction for the user
lblex1 = tk.Label(window,text="Step 1: Enter the amout of miles you have run in the day text box",bg="#6AE1E0")
lblex2 = tk.Label(window,text="Step 2: Hit the go botton ay the top to get your bar graph",bg="#6AE1E0")
lblex3 = tk.Label(window,text="you need to put all the miles you ran that week befor you hit go",bg="#6AE1E0")
lblex4 = tk.Label(window,text="every dash line is 5 miles",bg="#6AE1E0")

#text boxes
txt1 = tk.Entry(window,bg="#6AE1E0")
txt2 = tk.Entry(window,bg="#6AE1E0")
txt3 = tk.Entry(window,bg="#6AE1E0")
txt4 = tk.Entry(window,bg="#6AE1E0")
txt5 = tk.Entry(window,bg="#6AE1E0")
txt6 = tk.Entry(window,bg="#6AE1E0")
txt7 = tk.Entry(window,bg="#6AE1E0")

#bottens
bnt = tk.Button(window,text="Go", command=draw,bg="#6AE1E0")

#canvas
canvas = tk.Canvas(window,width=360,height=350,bg="#6AE1E0",highlightthickness=0)


#GUI 
#day area
lbl1.grid(row=1, column=0, padx=0, pady=5)
lbl2.grid(row=2, column=0, padx=0, pady=5)
lbl3.grid(row=3, column=0, padx=0, pady=5)
lbl4.grid(row=4, column=0, padx=0, pady=5)
txt1.grid(row=1, column=1, padx=0, pady=5)
txt2.grid(row=2, column=1, padx=0, pady=5)
txt3.grid(row=3, column=1, padx=0, pady=5)
txt4.grid(row=4, column=1, padx=0, pady=5)
lbl5.grid(row=5, column=0, padx=0, pady=5)
txt5.grid(row=5, column=1, padx=0, pady=5)
lbl6.grid(row=6, column=0, padx=0, pady=5)
txt6.grid(row=6, column=1, padx=0, pady=5)
lbl7.grid(row=7, column=0, padx=0, pady=5)
txt7.grid(row=7, column=1, padx=0, pady=5)
#the rest 
lblname.grid(row=0, column=4, padx=0,pady=5)
bnt.grid(row=0,column=0,padx=20,pady=0)
canvas.grid(row=8,column=4)
lblerror.grid(row=5,column=4)
lblex1.grid(row=1,column=4,padx=0,pady=5)
lblex2.grid(row=2,column=4,padx=0,pady=5)
lblex3.grid(row=4,column=4,padx=0,pady=5)
lblex4.grid(row=3,column=4,padx=0,pady=5)
#build Window
window.mainloop()