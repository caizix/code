from tkinter import *
root =Tk()
#定制面板
root.geometry('250x380')
root.title('才子鑫')

frame_show = Frame(width=300,height=150,bg='#dddddd')


#定义顶部
sv = StringVar()
sv.set('0')

show_label = Label(frame_show,textvariable=sv,bg= 'green',width=12,height=1,font=("黑体",20,'bold'),justify=LEFT,anchor='e')
show_label.pack(padx=10,pady=10)
frame_show.pack()
def delete():
    print("wobeishan")
def clear():
    print("清除")
def fan():
    print("正负号")
def ce():
    print("ce")
def change(num):
    print(num)
#嗯键区域
frame_bord = Frame(width= 400,height=350,bg='#cccccc')

b_del = Button(frame_bord,text="←",width=5,height=1,command=delete)

b_clear = Button(frame_bord,text="C",width=5,height=1,command=clear)
b_fan = Button(frame_bord,text="+_",width=5,height=1,command=fan)
b_ce = Button(frame_bord,text="CE",width=5,height=1,command=ce)
b_del.grid(row=0,column=0)
b_clear.grid(row=0,column=1)
b_fan.grid(row=0,column=2)
b_ce.grid(row=0,column=3)
b_1 = Button(frame_bord,text="1",width=5,height=1,command=lambda:change("1")).grid(row=1,column=0)
b_2 = Button(frame_bord,text="2",width=5,height=1,command=lambda:change("2")).grid(row=1,column=1)
b_3 = Button(frame_bord,text="3",width=5,height=1,command=lambda:change("3")).grid(row=1,column=2)
b_4 = Button(frame_bord,text="4",width=5,height=1,command=lambda:change("4")).grid(row=2,column=0)
b_5 = Button(frame_bord,text="5",width=5,height=1,command=lambda:change("5")).grid(row=2,column=1)
b_6 = Button(frame_bord,text="6",width=5,height=1,command=lambda:change("6")).grid(row=2,column=2)
b_7 = Button(frame_bord,text="7",width=5,height=1,command=lambda:change("7")).grid(row=3,column=0)
b_8 = Button(frame_bord,text="8",width=5,height=1,command=lambda:change("8")).grid(row=3,column=1)
b_9 = Button(frame_bord,text="9",width=5,height=1,command=lambda:change("9")).grid(row=3,column=2)


frame_bord.pack(padx=10,pady=10)
root.mainloop()