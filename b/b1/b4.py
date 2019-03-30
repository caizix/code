# 输入密码的小程序，用户输入正确，则显示正确
# encoding:utf-8
import tkinter as tk
window =tk.Tk()
def check_password():
    password = '123456'
    enterd_password = passwordEntry.get()
    if password ==enterd_password:
        confirmLabel.config(text = "正确")
    else:
        confirmLabel.config(text = "不正确")

passwordLabel = tk.Label(window,text = "Password:")
passwordEntry = tk.Entry(window,show = "*")
button = tk.Button(window,text="校验",command=check_password)
confirmLabel = tk.Label(window)


passwordLabel.pack()
passwordEntry.pack()
button.pack()
confirmLabel.pack()

window.mainloop()