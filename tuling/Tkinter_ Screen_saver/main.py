import random
import tkinter
class RandomBall():
    """
        定义运动的球类
    """
    def __init__(self,canvas,scrnwidth,scrnheight):
        self.canvas = canvas
        """
        canvas:画布，所有内容都在画布上，
        scrnwidth,scrnheight:屏幕的宽高
        """
        #球的初始位置
        self.xpos = random.randint(10,int(scrnwidth))
        self.ypos = random.randint(10,int(scrnwidth))
        #定义求得运动的运动
        self.xvelocity = random.randint(4,20)
        self.yvelocity = random.randint(4,20)
        #屏幕的大小
        self.scrnwidth = scrnwidth
        self.scrnheight = scrnheight
        #球得大小随机
        self.radius = random.randint(20,120)
        #球的颜色
        #RGB表述法：三个数字取值0-255
        c = lambda :random.randint(0,255)
        self.color='#%02x%02x%02x'%(c(),c(),c())
    def create_ball(self):
        """
        用构造函数定义变量值，在canvas画一个球
        """
        #tkinter没有画圆工具，画椭圆整体化
        x1 = self.xpos - self.radius
        y1 = self.ypos - self.radius
        x2 = self.xpos + self.radius
        y2 = self.ypos + self.radius
        self.item = self.canvas.create_oval(x1,y1,x2,y2,fill = self.color,outline = self.color)

    def move_ball(self):
        #移动球的时候，控制方向
        self.xpos += self.xvelocity
        self.ypos += self.yvelocity
        #判断撞墙
        if self.xpos + self.radius >= self.scrnwidth:
            #撞墙了
            self.xvelocity = -self.xvelocity
        if self.xpos -self.radius <0:
            self.xvelocity = -self.xvelocity
        if self.ypos + self.radius >= self.scrnheight:
            self.yvelocity = -self.yvelocity
        if self.ypos -self.radius < 0:
            self.yvelocity = -self.yvelocity


        #在画板上挪动图画
        self.canvas.move(self.item,self.xvelocity,self.yvelocity)
class ScreenSaver:
    """
        定义屏保的类.可以被启动
    """
    balls = []
    def __init__(self,num_balls):

        #每次启动球的数量
        #self.num_balls =random.randint(6,20)
        self.root = tkinter.Tk()
        #取消边框
        self.root.overrideredirect(1)
        #鼠标
        self.root.bind('<Motion>',self.myquit)
        #键盘

        #得到屏幕的大小
        w,h = self.root.winfo_screenwidth(),self.root.winfo_screenheight()

        #创建画布
        self.canvas = tkinter.Canvas(self.root,width=w,height=h)
        self.canvas.pack()

        #在画布花球
        for i in range(num_balls):
            ball = RandomBall(self.canvas,scrnwidth=w,scrnheight=h)
            ball.create_ball()
            self.balls.append(ball)
        self.run_screen_saver()
        self.root.mainloop()
    def run_screen_saver(self):
        for ball in self.balls:
            ball.move_ball()
        self.canvas.after(200,self.run_screen_saver)
    def myquit(self,evevnt):
        self.root.destroy()


if __name__ == '__main__':
    ScreenSaver(24)