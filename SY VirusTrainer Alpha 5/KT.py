import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter.simpledialog
import os
import tkinter.ttk
"""
    更新日志：
    KVT - Alpha 4：
        
    KVT - Alpha 5 20230210：
        1.添加了GUI
        2.用Python3.11重构了用C++写的屎山KVT Alpha 4项目
    SYVT - Alpha 5 20230216：
        #修复了一些已知bug
        #提升了使用体验
        1.更改了窗口标题和开屏显示的文字，更换了激活码
        2.加入了“只杀毒”功能
    SYVT - Alpha 6 20230310：
        1.更改了部分菜单结构
        2.修复了一些已知bug（把一个os.system写成os.esystem了）
        3.更改了版本号
"""
class ActiveKTA5Frame:
    def __init__(self):
        self.root = tkinter.Tk()
        # self.root.title("拾月杀毒 SYVT Alpha 5 GUI Version(内测中)"); #窗口标题
        self.root.geometry("0x0")  # 窗口大小
        # self.root.maxsize(1920,1080);   #窗口最大尺寸
        # self.root["background"] = "red";    #设置背景颜色
        # self.text = tkinter.Text(self.root, width=1920, height=540, font=("Ariel",200));  #？？？
        while True:
            ActiveCode = tkinter.simpledialog.askstring(
                "current", "请输入KTA5的激活码...")  # 默认文字
            if ActiveCode == "卡哇伊永远嘀神！": #kwy：我***！！！！
                break
        # self.text.bind("<Button-1>" ,lambda event:
        #    self.text.delete("0,0","end")); #单击清空数据
        self.root.mainloop()
        self.root.destroy()


class KTGUI:
    def __init__(self):
        #        ActiveKTA5Frame();
        # self.root.destroy();
        while True:
            ActiveCode = tkinter.simpledialog.askstring(
                "current", "请输入KTA5的激活码...")  # 默认文字
            if ActiveCode == "卡哇伊永远滴神！":  # 设置激活码
                break
            else:
                tkinter.messagebox.showinfo(
                    title="重要信息", message="你输入的激活码错误！")  # 弹窗
        self.root = tkinter.Tk()
        self.root.title("JYVT Alpha 5 GUI Version(内测中)")  # 窗口标题
        self.root.geometry("720x480")  # 窗口大小
        self.root.maxsize(1920, 1080)  # 窗口最大尺寸
        self.root["background"] = "red"  # 设置背景颜色
        self.treeview = tkinter.ttk.Treeview(
            self.root, columns=("GongNeng"), show="headings")  # 创建列表树
        self.treeview.heading(column="GongNeng", text="功能")
        self.treeview.column("GongNeng", width=720, anchor=tkinter.W)
        lable_text = tkinter.Label(self.root, text="十月杀毒 SYVT Alpha 5 内部测试版 Build 20230216",
                                   width=100, height=8, fg="yellow",
                                   font=("华文新魏", 20), bg="red")
        lable_text.pack()
        self.AllGongNengs = self.treeview.insert(
            parent="", index=tkinter.END, text="1.", values=("功能大全"))
        self.treeview.insert(parent=self.AllGongNengs,
                             index=tkinter.END, text="1.", values=("一键杀毒（做第二与第三项）"))
        self.treeview.insert(parent=self.AllGongNengs,
                             index=tkinter.END, text="2.", values=("一键恢复所有被隐藏的文件"))
        self.treeview.insert(parent=self.AllGongNengs,
                             index=tkinter.END, text="3.", values=("只杀毒"))
        self.HiddenThings = self.treeview.insert(
            parent="",index=tkinter.END,text="",values=(""));
        self.treeview.insert(parent=self.HiddenThings,
                            index=tkinter.END,text="4.", values=("删除病毒文件（不推荐）"))
        self.HiddenThings_Pro = self.treeview.insert(
            parent=self.HiddenThings,index=tkinter.END,text="", values=(""))
        self.LabFunctions = self.treeview.insert(
            parent=self.HiddenThings_Pro,index=tkinter.END,text="", values=("测试功能（慎用！！！）"))
        self.treeview.insert(parent=self.LabFunctionss,
                            index=tkinter.END,text="5.", values=("后台防护（Alpha）"))
        
        self.treeview.bind("<Double-Button-1>", self.ZhiXingDeGongNeng)  # 事件绑定
        self.treeview.pack()
        self.root.mainloop()

    def ZhiXingDeGongNeng(self, event):
        for index in self.treeview.selection():  # 获得选中项
            Everything = self.treeview.item(index, "values")  # 获得选中内容
            WhatToDo = "%s" % Everything
            match WhatToDo:
              case "一键杀毒（做第二与第三项）":
                print("----------------Killing Viruses----------------")
                print("---------------Killing Processes---------------")
                os.system("TASKKILL -F -IM py.exe -T")
                os.system("TASKKILL -F -IM Rundll32.exe -T")
                os.system("TASKKILL -F -IM AvastSvc.exe -T")
                os.system("TASKKILL -F -IM wscript.exe -T")
                os.system("TASKKILL -F -IM Autolt3.exe -T")
                os.system("TASKKILL -F -IM cmd.exe -T")
                print("----------------------FINISH-------------------")
                print("----------------Renaming Files-----------------")
                os.system("ren E:\*.lnk *.vir")
                os.system("ren F:\*.lnk *.vir")
                os.system("ren G:\*.lnk *.vir")
                os.system("ren H:\*.lnk *.vir")
                os.system("ren I:\*.lnk *.vir")
                os.system("ren J:\*.lnk *.vir")
                os.system("ren K:\*.lnk *.vir")
                os.system(
                    "ren E:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
                os.system(
                    "ren F:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
                os.system(
                    "ren G:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
                os.system(
                    "ren H:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
                os.system(
                    "ren I:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
                os.system(
                    "ren J:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
                os.system(
                    "ren K:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
                os.system("cd C:\ProgramData\AvastSvcp")
                os.system("ren Avastsvc.exe Avastsvc.exe.vf")
                os.system(
                    "ren E:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")
                os.system(
                    "ren F:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")
                os.system(
                    "ren G:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")
                os.system(
                    "ren H:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")
                os.system(
                    "ren I:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")
                os.system(
                    "ren J:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")
                os.system(
                    "ren K:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")
                os.system("ren E:\*.vbe *.vbe-vf")
                os.system("ren F:\*.vbe *.vbe-vf")
                os.system("ren G:\*.vbe *.vbe-vf")
                os.system("ren H:\*.vbe *.vbe-vf")
                os.system("ren I:\*.vbe *.vbe-vf")
                os.system("ren J:\*.vbe *.vbe-vf")
                os.system("ren K:\*.vbe *.vbe-vf")
                os.system("ren C:\Google\Autolt3.exe Al3ScriprRunner.com")
                print("----------------------FINSIH-------------------")
                print("-----------------Showing Files-----------------")
                os.system("attrib -s -h E:\*");
                os.system("attrib -s -h F:\*");
                os.system("attrib -s -h G:\*");
                os.system("attrib -s -h H:\*");
                os.system("attrib -s -h I:\*");
                print("----------------------FINSIH-------------------")
                tkinter.messagebox.showinfo(title="提示", message="清除并恢复文件完毕！")
              case "一键恢复所有被隐藏的文件":
                print("-----------------Showing Files-----------------")
                os.system("attrib -s -h E:\*");
                os.system("attrib -s -h F:\*");
                os.system("attrib -s -h G:\*");
                os.system("attrib -s -h H:\*");
                os.system("attrib -s -h I:\*");
                print("----------------------FINSIH-------------------")
                tkinter.messagebox.showinfo(title="提示", message="解除文件隐藏完毕！") 
              case "只杀毒":
                print("----------------Killing Viruses----------------")
                print("---------------Killing Processes---------------")
                os.system("TASKKILL -F -IM py.exe -T")
                os.system("TASKKILL -F -IM Rundll32.exe -T")
                os.system("TASKKILL -F -IM AvastSvc.exe -T")
                os.system("TASKKILL -F -IM wscript.exe -T")
                os.system("TASKKILL -F -IM Autolt3.exe -T")
                os.system("TASKKILL -F -IM cmd.exe -T")
                print("----------------------FINISH-------------------")
                print("----------------Renaming Files-----------------")
                os.system("ren E:\*.lnk *.vir")
                os.system("ren F:\*.lnk *.vir")
                os.system("ren G:\*.lnk *.vir")
                os.system("ren H:\*.lnk *.vir")
                os.system("ren I:\*.lnk *.vir")
                os.system("ren J:\*.lnk *.vir")
                os.system("ren K:\*.lnk *.vir")
                os.system(
                    "ren E:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
                os.system(
                    "ren F:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
                os.system(
                    "ren G:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
                os.system(
                    "ren H:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
                os.system(
                    "ren I:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
                os.system(
                    "ren J:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
                os.system(
                    "ren K:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
                os.system("cd C:\ProgramData\AvastSvcp")
                os.system("ren Avastsvc.exe Avastsvc.exe.vf")
                os.system(
                    "ren E:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")
                os.system(
                    "ren F:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")
                os.system(
                    "ren G:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")
                os.system(
                    "ren H:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")
                os.system(
                    "ren I:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")
                os.system(
                    "ren J:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")
                os.system(
                    "ren K:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")
                os.system("ren E:\*.vbe *.vbe-vf")
                os.system("ren F:\*.vbe *.vbe-vf")
                os.esystem("ren G:\*.vbe *.vbe-vf")
                os.system("ren H:\*.vbe *.vbe-vf")
                os.system("ren I:\*.vbe *.vbe-vf")
                os.system("ren J:\*.vbe *.vbe-vf")
                os.system("ren K:\*.vbe *.vbe-vf")
                os.system("ren C:\Google\Autolt3.exe Al3ScriprRunner.com")
                print("----------------------FINSIH-------------------")
                tkinter.messagebox.showinfo(title="提示", message="清除病毒完毕！")
              case "删除病毒文件（不推荐）":
                    pass;
            print(WhatToDo)


def main():
    KTGUI()


if __name__ == "__main__":
    main()
