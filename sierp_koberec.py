import tkinter as tk
win = tk.Tk()

def sierp(a,b,d,hlbka=12):
   if hlbka > 0:
        hlbka -= 1
        canvas.create_rectangle(a,b,a+d,b+d)
        

h = 1000
w = 1000
d = 900

canvas = tk.Canvas(win, height=h, width=w, bg="white")
canvas.pack()

sierp(50,50,d)
win.mainloop()