import tkinter as tk
win = tk.Tk()

def sierp(x,y,d,hlbka=12):
   if hlbka > 0:
        hlbka -= 1
        v =(d**2-(d//2)**2)**0.5
        canvas.create_line(x,y,x+d,y)
        canvas.create_line(x+d,y,x+d//2,y-v)
        canvas.create_line(x,y,x+d//2,y-v)
        sierp(x,y,d//2,hlbka)
        sierp(x+d//2,y,d//2,hlbka)
        sierp(x+d//4,y-(v//2),d//2,hlbka)

h = 1000
w = 1000
d = 990
canvas = tk.Canvas(win, height=h, width=w, bg="white")
canvas.pack()

sierp(10,880,d)
win.mainloop()