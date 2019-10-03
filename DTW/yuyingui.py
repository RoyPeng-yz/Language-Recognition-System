# -*- coding: utf-8 -*-

#这是系统界面  
import tkinter  
from tkinter import messagebox
  

class Login(object):  
    def __init__(self):  
        # 创建主窗口,用于容纳其它组件  
        self.root = tkinter.Tk()  
        # 给主窗口设置标题内容  
        self.root.title("智能家居人机交互(语音版)")  
        self.root.geometry('450x300')  
        #运行代码时记得添加一个gif图片文件，不然是会出错的
        self.canvas = tkinter.Canvas(self.root, height=200, width=500)#创建画布  
        self.image_file = tkinter.PhotoImage(file='GIF.gif')#加载图片文件  
        self.image = self.canvas.create_image(0,0, anchor='nw', image=self.image_file)#将图片置于画布上  
        self.canvas.pack(side='top')#放置画布（为上端）  
        #创建一个`label`名为`检测结果: `  
        self.label_result = tkinter.Label(self.root, text='检测结果: ') 
        # 创建一个账号输入框,并设置尺寸  
        self.output_result = tkinter.Entry(self.root, width=30)  
        # 创建一个登录系统的按钮  
        self.input_button = tkinter.Button(self.root, command = self.output_fu, text = "录入语音", width=10)  

    # 完成布局  
    def gui_arrang(self):  
        self.label_result.place(x=60, y= 170)  
        self.output_result.place(x=135, y=170)  
        self.input_button.place(x=190, y=235)  

    # 进入注册界面  
    def output_fu(self):  
        self.output_result.insert(0 ,'打开冰箱')

  

def main():  
    # 初始化对象  
    L = Login()  
    # 进行布局  
    L.gui_arrang()  
    # 主程序执行  
    tkinter.mainloop()  
  

if __name__ == '__main__':  

    main()  