#coding:UTF-8
#Copyleft SINOVERSE Groups Ltd. 1963-2024
#This Programme is a work by CS2B Studio
#Original file is written by SY Tech/KWY Technology
#"CS2B Studio","KWY Technology" are trademarks of SINOVERSE Groups.
#环境要求：python 3.10+，仅支持Windows，可能需要Windows 8+才能运行
#Version:0.6.20240804-py
"""
#Original File Version: SYVT-A4-B20230310
#Shit Mountain Start
#-----------------------------------------------------------------------------
import tkinter
from tkinter import *
from tkinter import messagebox
import tkinter.simpledialog
import os
import tkinter.ttk
""
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
""
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

#----------------------------------------------------------------------------------------------------------
#Shit Mountain Ends
"""



#New File（Shit Mountain) Start
#----------------------------------------------------------------------------------------------------------
KVTVersion = 20240812
try: #防止奇葩的运行环境少库报错
    import tkinter
    from tkinter import *
    from tkinter import messagebox
    import tkinter.simpledialog
    import os
    import tkinter.ttk
    import traceback
    import sys
    import requests,bs4 #需要安装
    import psutil #需要安装，暂时先放这里。后面可能会另开一个文件
    import KVTI_options #我自己的私有库
    import Upgrade
    #import Settings #我自己的独有文件，放在同一目录下 #不需要了，代码写进来了
    #LOGO_PATH = "resources" + os.sep + "KVT.ico" #Logo路径
    
except ModuleNotFoundError as err: #缺少必要的组件
    tkinter.messagebox.showinfo(title="警告", message="您的环境中缺少必要组件，NFLS Virus Trainer即将退出……")
    tkinter.messagebox.showinfo(title="错误代码全文", message="%s" % traceback.format_exc())
    exit(1)
except Exception as err:
    print(traceback.format_exc()) #输出错误原因
finally:
    pass;
def get_resource_path(relative_path):
        if getattr(sys, "frozen", False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".")
        return os.path.join(base_path, relative_path)
LOGO_PATH = get_resource_path(os.path.join("resources", "KVT.ico"))
INFO_IMAGE_PATH = get_resource_path(os.path.join("resources", "KVT.png"))
SETTINGS_LOGO_PATH = get_resource_path(os.path.join("resources", "KVTSettings.png"))
UPGRADE_LOGO_PATH = get_resource_path(os.path.join("resources", "KVTLogo.png"))
class MainForm: #抄的
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("NFLS Virus Trainer")
        try:
            self.root.iconbitmap(LOGO_PATH)
        except Exception as err:
            print(traceback.format_exc())
        finally:
            pass
        self.root.geometry("328x198") #含义明确的窗口大小
        self.root.maxsize(648,328) #含义更明确的窗口最大大小
        self.frame = tkinter.Frame(self.root)
        self.content = tkinter.StringVar() #修改内容
        self.content
        self.label = tkinter.Label(self.root, text="NVT Alpha 6 Py版",
                                   height=1,font=("汉仪文黑-85W",18), justify="right") #字体自行安装
        self.label.pack() #显示标题
        #self.label.place(x=68,y=30)
        #构建选择列表
        tkinter.Label(self.frame, text="请选择一个操作：",font=("SDK_SC_WEB Regular",16), #字体自行安装
            justify="left").grid(row=0,column=0,sticky=tkinter.W) #显示标签
        actions_tuble = ("1.杀毒","2.显示被病毒隐藏的文件","3.以上都做","4.启动或关闭后台防护","5.检查更新","6.显示关于界面","7.设置","8.卸载该程序")
        self.actions_combobox = tkinter.ttk.Combobox(self.frame, values=actions_tuble) #列表项
        self.actions_combobox.bind("<<ComboboxSelected>>", self.debug) #选项改变，传递给debug函数
        self.actions_combobox.grid(row=0,column=1) #显示组件
        #显示选择列表
        self.frame.pack() #frame显示
        #self.frame.place(y=68)#定义位置
        self.label2 = tkinter.Label(self.root, text="初三二班工作室™©出品 Copyleft 2022-2024 \n Nanflas202202.github.io",
                                   height=18,font=("汉仪文黑-85W",6), justify="center") #字体自行安装
        self.label2.pack() #显示label2
        '''self.label3 = tkinter.Label(self.root, text="Nanflas202202.github.io",
                                   height=0,font=("汉仪文黑-85W",6), justify="right") #字体自行安装
        self.label3.pack() #显示标题'''
        #self.title.place(y=30)
        #高 血 压 时 刻
        self.root.protocol("WM_DELETE_WINDOW",self.close_handle) #关闭确认
        self.root.mainloop()
    #主要部分
    def debug(self, event):
        ActionsLabel = str(self.actions_combobox.get())
        match ActionsLabel:    #执行列表
            case "1.杀毒" :
                tkinter.messagebox.showinfo(title="NVT友情提示", message="开始杀毒")
                KillVirus();
                tkinter.messagebox.showinfo(title="NVT友情提示", message="完毕")
                pass
            case "2.显示被病毒隐藏的文件":
                tkinter.messagebox.showinfo(title="NVT友情提示", message="开始解除被隐藏的文件的隐藏状态……（建议优先杀毒）")
                ShowHiddenFiles();
                tkinter.messagebox.showinfo(title="NVT友情提示", message="完毕")                
                pass
            case "3.以上都做":
                tkinter.messagebox.showinfo(title="NVT友情提示", message="开始杀毒")
                KillVirus();
                tkinter.messagebox.showinfo(title="NVT友情提示", message="完毕")
                tkinter.messagebox.showinfo(title="NVT友情提示", message="开始解除被隐藏的文件的隐藏状态……")
                ShowHiddenFiles();
                tkinter.messagebox.showinfo(title="NVT友情提示", message="完毕")
                pass
            case "4.启动或关闭后台防护":#这一项好像用不了，鬼知道为什么
                """
                for proc in psutil.process_iter():
                    try:
                        if proc.name() == "BackgroundProt-V2.exe":
                            if tkinter.messagebox.askyesnocancel(title="NVT提示", message="后台防护正在运行！是否关闭？"):
                                try:
                                    proc.terminate()
                                except Exception:
                                    tkinter.messagebox.showinfo(title="发生错误！", message="错误代码全文： \n %s" % traceback.format_exc())
                                    print(traceback.format_exc())
                                tkinter.messagebox.showinfo(title="NVT提示", message="完成!")
                    except psutil.NoSuchProcess:
                        if tkinter.messagebox.askyesnocancel(title="NVT提示", message="后台防护未运行！是否启动？"):
                                    os.system("start BackgroundProt-V2.exe")
                        tkinter.messagebox.showinfo(title="NVT提示", message="完成!")
                pass
                """
                BackgroundProtOptions("BackgroundProt-V2.exe")
            case "5.检查更新":
                Upgrade.CheckUpgrade();
            case "6.显示关于界面":
                self.ShowKVTInfo()
            case "7.设置":
                self.KVTSettings()
            case "8.卸载该程序":
                os.system("start GF2uninst.exe")
    def close_handle(self):
        if tkinter.messagebox.askyesnocancel("NVT退出确认","你确定要退出NFLS VirusTrainer吗？"): #询问是否要关闭窗口
            tkinter.messagebox.showinfo(title="NVT友情提示", message="做梦！") #我们为了更好的服务用户，我们做出了一个艰难的决定……
    def ShowKVTInfo(self):
        self.root=tkinter.Toplevel()
        self.root.title("关于NFLS Virus Trainer")
        self.root.iconbitmap(LOGO_PATH) 
        self.root.geometry("328x198")
        self.root.resizable(height=False,width=False) #禁止缩放窗口
        photo = tkinter.PhotoImage(file=INFO_IMAGE_PATH)
        label_photo = tkinter.Label(self.root,image=photo)
        label_photo.pack()
        self.root.mainloop()
    def KVTSettings(self):
        self.root = tkinter.Toplevel()
        self.root.title("NVT设置")
        self.root.iconbitmap(LOGO_PATH) #Logo
        self.root.geometry("198x328") #窗口大小
        self.root.maxsize(198,648) #最大窗口大小
        self.BlockedProcesses = [("Rundll32.exe", tkinter.IntVar()), ("Autolt3.exe", tkinter.IntVar()), ("CMD.exe", tkinter.IntVar()), ("Wscript.exe", tkinter.IntVar()), ("AvastSvc.exe", tkinter.IntVar()),("选择此项以保存您的设置",tkinter.IntVar()),("查看当前的设置",tkinter.IntVar())] #要选择是否拦截的文件
        self.label = tkinter.Label(self.root, text="请选择您希望后台拦截的病毒：",
                                   font=("汉仪文黑-85W", 10), justify="left")
        self.label.pack(anchor="w")
        item_row = 1 #设置列索引
        for title, status in self.BlockedProcesses:
            check = tkinter.Checkbutton(self.root, text=title,onvalue=1,offvalue=0,
                                         variable=status, command=self.write_settings) #复选框
            check.pack(anchor="w") #布局显示
            item_row += 1          #修改操作列
        #self.BlockedProcesses[6][1].set(1) #设置默认选中
        self.content = tkinter.StringVar() #标签内容
        self.show_label = tkinter.Label(self.root, textvariable=self.content,
                                        font=("SDK_SC_WEB Regular", 8), justify="left")
        self.show_label.pack(anchor="w")
        self.root.mainloop()
    def write_settings(self):
        for title, status in self.BlockedProcesses:
            if status.get() == 1:
                CommandVar = title;
                print(CommandVar)
                if CommandVar == "选择此项以保存您的设置":
                 for title, status in self.BlockedProcesses:
                  if status.get() == 1:
                   WriteCommand = title
                   print(WriteCommand)
                   match WriteCommand:
                    case "Rundll32.exe":
                        KVTI_options.kvtiWriter("BlockRundll32","True")
                    case "Autolt3.exe":
                        KVTI_options.kvtiWriter("BlockAutolt3","True")
                    case "CMD.exe":
                        KVTI_options.kvtiWriter("BlockCMD","True")
                    case "Wscript.exe":
                        KVTI_options.kvtiWriter("BlockWscript","True")
                    case "AvastSvc.exe":
                        KVTI_options.kvtiWriter("BlockAvastSvc","True")
                  elif status.get() == 0:
                   WriteCommand = title
                   print(WriteCommand)
                   match WriteCommand:
                    case "Rundll32.exe":
                        KVTI_options.kvtiWriter("BlockRundll32","False")
                    case "Autolt3.exe":
                        KVTI_options.kvtiWriter("BlockAutolt3","False")
                    case "CMD.exe":
                        KVTI_options.kvtiWriter("BlockCMD","False")
                    case "Wscript.exe":
                        KVTI_options.kvtiWriter("BlockWscript","False")
                    case "AvastSvc.exe":
                        KVTI_options.kvtiWriter("BlockAvastSvc","False") 
                  else:
                      pass 
                 tkinter.messagebox.showinfo(title="NVT友情提示", message="已保存设置项！") 
                 ShowBack = "您修改的设置："
                 for title, status in self.BlockedProcesses:
                    if status.get() == 1:
                        if title == "选择此项以保存您的设置" or "查看当前的设置":
                            pass
                        else:
                            ShowBack+= title + "-拦截 \n" 
                    elif status.get() == 0:
                        if title == "选择此项以保存您的设置" or "查看当前的设置":
                            pass
                        else:
                            ShowBack+= title + "-不拦截 \n" 
                    else:
                        pass
                 self.content.set(ShowBack)
                 break
                if CommandVar == "查看当前的设置":
                    BlockStatus = "您当前的设置： \n"
                    Rundll32BlockStatus = str(KVTI_options.ReadKVTIFiles("Settings.kvti","BlockRundll32"))
                    Autolt3BlockStatus = KVTI_options.ReadKVTIFiles("Settings.kvti","BlockAutolt3")
                    CMDBlockStatus = KVTI_options.ReadKVTIFiles("Settings.kvti","BlockCMD")
                    WscriptBlockStatus = KVTI_options.ReadKVTIFiles("Settings.kvti","BlockWscript")
                    AvastSvcBlockStatus = KVTI_options.ReadKVTIFiles("Settings.kvti","BlockAvastSvc")
                    DebuggerStatus = KVTI_options.ReadKVTIFiles("Settings.kvti","BlockNotepadSvc")
                    if Rundll32BlockStatus == "True":
                        BlockStatus += "Rundll32.exe - 拦截 \n";
                    else :
                        BlockStatus += "Rundll32.exe - 不拦截 \n";
                    if Autolt3BlockStatus == "True":
                        BlockStatus += "Autolt3.exe - 拦截 \n";
                    else :
                        BlockStatus += "Autolt3.exe - 不拦截 \n";
                    if CMDBlockStatus == "True":
                        BlockStatus += "CMD.exe - 拦截 \n";
                    else :
                        BlockStatus += "CMD.exe - 不拦截 \n";
                    if WscriptBlockStatus == "True":
                        BlockStatus += "WScript.exe - 拦截 \n";
                    else :
                        BlockStatus += "WScript.exe - 不拦截 \n";
                    if AvastSvcBlockStatus == "True":
                        BlockStatus += "AvastSvc.exe - 拦截 \n";
                    else :
                        BlockStatus += "AvastSvc.exe - 不拦截 \n";
                    if DebuggerStatus == "True":
                        BlockStatus += "Debug Mode - 已启用"
                    self.content.set(BlockStatus)
                else:
                    pass
        """
        self.Rundll32Block = [("是",0), ("否", 1)]
        self.Autolt3Block = [("是",0), ("否", 1)]
        self.CMDBlock = [("是",0), ("否", 1)]
        self.WscriptBlock = [("是",0), ("否", 1)]
        self.AvastSvcBlock = [("是",0), ("否", 1)]
        self.status = tkinter.IntVar()
        self.label = tkinter.Label(self.root, text="[后台防护]是否查杀Rundll32.exe ",
                                   font=("SDK_SC_WEB Regular", 6), justify="left")
        self.label.grid(row=0, column=0)
        self.status.set(0)
        item_colomn = 1
        for title, index in self.Rundll32Block:
            radio1 = tkinter.Radiobutton(self.root, text=title, value=index,
                                 variable=self.status, font=("SDK_SC_WEB Regular", 6),
                                 command=self.R32BSet)#传递给写入设置文件的函数
            radio1.grid(row=0, column=item_colomn) #标签内容
            item_colomn += 1   #修改操作列

        self.label2 = tkinter.Label(self.root, text="[后台防护]是否查杀AvastSvc.exe ",
                                   font=("SDK_SC_WEB Regular", 6), justify="left")
        self.label2.grid(row=2, column=0)
        #self.status.set(1)
        item_colomn = 1
        for title, index in self.AvastSvcBlock:
            radio2 = tkinter.Radiobutton(self.root, text=title, value=index,
                                 variable=self.status, font=("SDK_SC_WEB Regular", 6),
                                 command=self.ASvBSet)#传递给写入设置文件的函数
            radio2.grid(row=2, column=item_colomn) #标签内容
            item_colomn += 1   #修改操作列
        
        self.root.mainloop()

    def R32BSet(self):
        for title, index in self.Rundll32Block:
            if index == self.status.get(): #选项值判断满足
                SelectItem = str("%s" % title) #获取选择内容
                print(SelectItem) #测试用
            if SelectItem == "是":
                KVTI_options.kvtiWriter("BlockRundll32","True")  
            elif SelectItem == "否":
                KVTI_options.kvtiWriter("BlockRundll32","False")
            else:
                KVTI_options.kvtiWriter("BlockRundll32","False")

    def ASvBSet(self):
        for title, index in self.AvastSvcBlock:
            if index == self.status.get(): #选项值判断满足
                SelectItem2 = str("%s" % title) #获取选择内容
                print(SelectItem2) #测试用
            if SelectItem2 == "是":
                KVTI_options.kvtiWriter("BlockAvastSvc","True")
            elif SelectItem2 == "否":
                KVTI_options.kvtiWriter("BlockAvastSvc","False")
            else:
                KVTI_options.kvtiWriter("BlockRundll32","False")
                pass
    #连带着老文件里的诗山我也复制进来了，我细致吧？
    """
    """
    def CheckUpgrage(self): #这里我爬不下来我的网页上的数据，不知道为啥 #改成Cloudflare Pages，可以了
        self.root=tkinter.Toplevel()
        self.root.title("NFLS Virus Trainer更新")
        self.root.iconbitmap(UPGRADE_LOGO_PATH) 
        self.root.geometry("328x198")
        self.root.maxsize(328,198) 
        photo = tkinter.PhotoImage(file=UPGRADE_LOGO_PATH)
        label_photo = tkinter.Label(self.root,image=photo)
        label_photo.image = photo
        label_photo.pack()
        Content="当前版本 Build 20220804 \n 正在寻找新版本……"
        self.content=tkinter.StringVar(Content)
        self.show_label = tkinter.Label(self.root, textvariable=self.content(),
                                        font=("SDK_SC_WEB Regular", 8), justify="left")
        self.show_label.pack()
        ServerURL = "https://nanflas202202.pages.dev/LatestVerson.version" #我的更新服务器
        #headers={'Referer': 'https://nanflas202202.github.io/VTUpdrade/LatestVerson.html','User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        try:
            request = requests.get(url=ServerURL,timeout=10);
            request.encoding = "UTF-8"
            LatestKVTVersion = int(request.text)
            print(LatestKVTVersion)
            if KVTVersion < LatestKVTVersion:
                self.content ="当前版本 Build 20220804 \n 正在寻找新版本…… \n 已发现新版本"
                if tkinter.messagebox.askyesnocancel("NVT更新提示","发现新版本，是否更新您的NFLS VirusTrainer?"): #询问是否要更新
                    tkinter.messagebox.showinfo(title="NVT友情提示", message="正在开始下载……") 
                else:
                    tkinter.messagebox.showinfo(title="NVT友情提示", message="做梦！")  #我们为了更好的服务用户，我们做出了一个艰难的决定……
                #os.system("aria2c -x 8192 https://nanflas202202.pages.dev/Upgrade.exe") #自己去找那个吾爱破解上的解锁8192线程的Aria2，Aria2c.exe自备
                os.system("Upgrade.exe")
                tkinter.messagebox.showinfo(title="NVT友情提示", message="完成。") 
                
            else:
                tkinter.messagebox.showinfo(title="NVT友情提示", message="暂未发现新版本！") 
        except ConnectionError as err:
            tkinter.messagebox.showinfo(title="NVT错误", message="无法连接到更新服务器！")
        except ConnectionResetError as err:
            tkinter.messagebox.showinfo(title="NVT错误", message="更新服务器错误！")
        except ConnectionAbortedError as err:
            tkinter.messagebox.showinfo(title="NVT错误", message="更新服务器错误！访问被拒绝！")
        #似乎报错原因并不是前三种错误
        except Exception as err:
            tkinter.messagebox.showinfo(title="错误代码全文", message="%s" % traceback.format_exc())
            print(traceback.format_exc())
        finally:
            pass
        tkinter.mainloop()
"""
def KillVirus():
    #以下为正常内容，你自己删掉注释吧
    #因为我要测试，不可能在我的电脑上干这些事情
    
    print("----------------Killing Viruses----------------")
    print("---------------Killing Processes---------------")
    os.system("TASKKILL -F -IM py.exe -T")
    os.system("TASKKILL -F -IM Rundll32.exe -T")
    os.system("TASKKILL -F -IM AvastSvc.exe -T")
    os.system("TASKKILL -F -IM wscript.exe -T")
    os.system("TASKKILL -F -IM Autolt3.exe -T")
    os.system("TASKKILL -F -IM cmd.exe -T")
    print("----------------------FINISH-------------------")
    
    pass

def ShowHiddenFiles():
    #同上，自己删注释
    
    print("----------------Renaming Files-----------------")
    os.system("ren E:\*.lnk *.vir")
    os.system("ren F:\*.lnk *.vir")
    os.system("ren G:\*.lnk *.vir")
    os.system("ren H:\*.lnk *.vir")
    os.system("ren I:\*.lnk *.vir")
    os.system("ren J:\*.lnk *.vir")
    os.system("ren K:\*.lnk *.vir")
    os.system("ren E:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
    os.system("ren F:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
    os.system("ren G:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
    os.system("ren H:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
    os.system("ren I:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
    os.system("ren J:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
    os.system("ren K:\RECYCLER.BIN $Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}")
    os.system("cd C:\ProgramData\AvastSvcp")
    os.system("ren Avastsvc.exe Avastsvc.exe.vf")
    os.system("ren E:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")
    os.system("ren F:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")
    os.system("ren G:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")
    os.system("ren H:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")
    os.system("ren I:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")   
    os.system("ren J:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")                   
    os.system("ren K:\Skypee Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}")                   
    os.system("ren E:\*.vbe *.vbe-vf")
    os.system("ren F:\*.vbe *.vbe-vf")
    os.esystem("ren G:\*.vbe *.vbe-vf")
    os.system("ren H:\*.vbe *.vbe-vf")
    os.system("ren I:\*.vbe *.vbe-vf")
    os.system("ren J:\*.vbe *.vbe-vf")
    os.system("ren K:\*.vbe *.vbe-vf")
    os.system("ren C:\Google\Autolt3.exe Al3ScriprRunner.com")
    print("----------------------FINSIH-------------------")
    
    pass

def DeleteVirus():
    tkinter.messagebox.showinfo(title="NVT友情提示", message="做梦！") #万能答复
    pass

#由于文件修改而不再需要的诗山
#这一段我改到MainForm里了
"""
class ShowKVTInfo_old:
    def __init__(self):
        self.root=tkinter.Toplevel()
        self.root.title("关于NFLS Virus Trainer")
        self.root.iconbitmap(LOGO_PATH) 
        self.root.geometry("328x198")
        self.root.resizable(height=False,width=False) #禁止缩放窗口
        \"""self.canvas = tkinter.Canvas(self.root, height=328, width=198) #创建绘图板
        self.image = tkinter.PhotoImage(file=INFO_IMAGE_PATH) #外链图片
        self.canvas.create_image((0,0), anchor=tkinter.NW, image=self.image)
        self.canvas.pack(fill="both")\"""
        photo = tkinter.PhotoImage(file=INFO_IMAGE_PATH)
        label_photo = tkinter.Label(self.root,image=photo)
        label_photo.pack()
        self.root.mainloop()   
"""

def BackgroundProtOptions(process_name): #通义千问写的
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            if proc.info['name'] == process_name:
                if messagebox.askyesnocancel(title="NVT提示", message="后台防护正在运行！是否关闭？") is True:
                    try:
                        proc.terminate()
                    except Exception:
                        messagebox.showinfo(title="发生错误！", message="错误代码全文：\n%s" % traceback.format_exc())
                        print(traceback.format_exc())
                    messagebox.showinfo(title="NVT提示", message="完成!")
                return  # 如果找到了进程，直接退出函数
        except psutil.NoSuchProcess:
            pass  # 忽略NoSuchProcess异常，继续下一个进程

    # 如果循环结束都没有找到进程，则执行以下代码
    if messagebox.askyesnocancel(title="NVT提示", message="后台防护未运行！是否启动？"):
        os.system(f"start {process_name}")
        messagebox.showinfo(title="NVT提示", message="完成!")

def main(): #没啥用的主函数

    MainForm()

if __name__ == "__main__":
    main()