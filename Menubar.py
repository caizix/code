import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x200')
counter = 0


def do_job():
    global counter
    l.config(text='do' + str(counter))
    counter += 1


l = tk.Label(window, text='', bg='yellow')
l.pack()
menubar = tk.Menu(window)
filemenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='New', command=do_job)
filemenu.add_command(label='Open', command=do_job)
filemenu.add_command(label='Save', command=do_job)
filemenu.add_separator()
filemenu.add_command(label='Exit', command=window.quit)

editmenu = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Cut', command=do_job)
editmenu.add_command(label='Copy', command=do_job)
editmenu.add_command(label='Paste', command=do_job)

submenu = tk.Menu(filemenu)  ##和上面定义菜单一样，不过此处实在`File`上创建一个空的菜单
filemenu.add_cascade(label='Import', menu=submenu, underline=0)  ##给放入的菜单`submenu`命名为`Import`
submenu.add_command(label="Submenu1", command=do_job)  ##这里和上面也一样，在`Import`中加入一个小菜单命令`Submenu1`
window.config(menu=menubar)
window.mainloop()
