import tkinter as tk
win = tk.Tk()

def sierp(a,b,d,hlbka=6):
   if hlbka > 0:
        hlbka -= 1
        canvas.create_rectangle(a,b,a+d,b+d)
        canvas.create_rectangle(a,b,a+d//3,b+d//3)
        canvas.create_rectangle(a+d//3,b,a+2*d//3,b+d//3)
        canvas.create_rectangle(a+2*d//3,b,a+d,b+d//3)
        canvas.create_rectangle(a,b+d//3,a+d//3,b+2*d//3)
        canvas.create_rectangle(a+2*d//3,b+d//3,a+d,b+2*d//3)
        canvas.create_rectangle(a,b+2*d//3,a+d//3,b+d)
        canvas.create_rectangle(a+d//3,b+2*d//3,a+2*d//3,b+d)
        canvas.create_rectangle(a+2*d//3,b+2*d//3,a+d,b+d)
        sierp(a,b,d//3,hlbka)
        sierp(a+d//3,b,d//3,hlbka)
        sierp(a+2*d//3,b,d//3,hlbka)
        sierp(a,b+d//3,d//3,hlbka)
        sierp(a+2*d//3,b+d//3,d//3,hlbka)
        sierp(a,b+2*d//3,d//3,hlbka)
        sierp(a+d//3,b+2*d//3,d//3,hlbka)
        sierp(a+2*d//3,b+2*d//3,d//3,hlbka)

h = 800
w = 800
d = 781

canvas = tk.Canvas(win, height=h, width=w, bg="white")
canvas.pack()

sierp(10,10,d)
win.mainloop()
