import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x100')
# 这里是窗口内容

var = tk.StringVar()
# 这是文字变量储存器
l = tk.Label(window,
             textvariable=var,  # 使用textvariable替换text
             bg='green',
             font=('Arial', 12),
             width=15, height=2
             )
l.pack()
on_hit = False


def hit_me():
    global on_hit
    if on_hit == False:
        on_hit = True
        var.set('you hit me')
    else:
        on_hit = False
        var.set('')


b = tk.Button(window, text='hit me',  # 显示在嗯扭上的文字
              width=15, height=2,
              command=hit_me)  # 点击按钮执行的命令
b.pack()  # 按钮位置
window.mainloop()
