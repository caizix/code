import tkinter as tk

window = tk.Tk()
window.title('muy window')
window.geometry('200x200')

varl = tk.StringVar()  # 创建变量
l = tk.Label(window, bg='yellow', width=4, textvariable=varl)
l.pack()


def print_selection():
    value = lb.get(lb.curselection())  # 获取当前选中的文本
    varl.set(value)  # 为label设置值


b1 = tk.Button(window,
               text='print slection',
               width=15,
               height=2,
               command=print_selection
               )
b1.pack()

var2 = tk.StringVar()

var2.set((11, 22, 33, 44))  # 为变量设置值
lb = tk.Listbox(window, listvariable=var2)  # 将把var2的值赋给listbox
# 创建一个list并将值循环添加到listbox控件中
list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert('end', item)  # 从最后一个位置添加，
lb.insert(1, 'fi')  # 在第一个位置添加
lb.pack()
window.mainloop()  # 显示主窗口
