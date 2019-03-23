window = tk.Tk()
window.title（'我的窗口'）
window.geometry（' 200x200 '）

def hit_me（

）：  # tk.messagebox.showinfo（title ='嗨'，message ='hahahaha'）＃ return'ok'  # tk.messagebox.showwarning（title ='嗨'，message ='nononono'）＃return'ok'
# tk.messagebox.showerror（title ='嗨'，message ='No !! never'）# return'ok'
print（tk.messagebox.asktrycancel（title = '嗨'，message = ' hahahaha '））    ＃ return True，False
print（tk.messagebox.askokcancel（title = '嗨'，message = ' hahahaha '））    ＃ return True，False
print（tk.messagebox.askyesnocancel（title = “ Hi ”，message = “ haha ”））      ＃ return，True，False，None

tk.Button（window，text = ' hit me '，command = hit_me）.pack（）
window.mainloop（）
