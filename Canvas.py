import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')

canvas = tk.Canvas(window, bg='blue', height=100, width=200)
# image_file=tk.PhotoImage(file='123.jpg')
# image=canvas.create_image(0,0,anchor='nw',image=image_file)
x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)
canvas.pack()

b = tk.Button(window, text='move', command=moveit)
b.pack()

window.mainloop()
