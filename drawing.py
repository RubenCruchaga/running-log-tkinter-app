from distutils.cmd import Command
import tkinter as tk

#custom function
def draw():
    x1 = int(txtX1.get())
    y1 = int(txty1.get())
    x2 = int(txtX2.get())
    y2 = int(txty2.get())
    canvas.create_line(x1,y1,x2,y2)
def clear():
    canvas.delete("all")

#window properties
window = tk.Tk()
window.title('Graphing with Tkinter')
window.geometry('800x800')

#lables
lblX1 = tk.Label(window, text="X1:")
lbly1 = tk.Label(window, text="Y1:")
lblX2 = tk.Label(window, text="X2:")
lbly2 = tk.Label(window, text="Y2:")
#text boxese
txtX1 = tk.Entry(window)
txty1 = tk.Entry(window)
txtX2 = tk.Entry(window)
txty2 = tk.Entry(window)
#bottens
bnt = tk.Button(window,text="DRAW?", command=draw)
bntClear = tk.Button(window,text="Clear",command=clear)

#canvas
canvas = tk.Canvas(window)


#GUI 
lblX1.grid(row=0, column=0, padx=0, pady=5)
lbly1.grid(row=1, column=0, padx=0, pady=5)
lblX2.grid(row=2, column=0, padx=0, pady=5)
lbly2.grid(row=3, column=0, padx=0, pady=5)
txtX1.grid(row=0, column=1,padx=0, pady=5)
txty1.grid(row=1, column=1,padx=0, pady=5)
txtX2.grid(row=2, column=1,padx=0, pady=5)
txty2.grid(row=3, column=1,padx=0, pady=5)
bnt.grid(row=3,column=2,padx=20,pady=0)
canvas.grid(row=4,column=3)
bntClear.grid(row=2,column=2,padx=20,pady=0)
#build Window
window.mainloop()