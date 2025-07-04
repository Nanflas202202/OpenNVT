#coding:utf-8
"""
About this program
-------------------------------------------------------
NFLS Virus Trainer
Version:Alpha 7.5 RC3
Codename:ProjectYSF
Build Time:2025-Jan-30th
Developer:Yusulif
Copyleft CS2B Studio 2022-2025 No lefts reserved
CS2B Studio Official Website:CS2BStudio.pages.dev

Online Upgrade Information
-------------------------------------------------------
KVTVersion = 0.750130
KVTIModuleVersion = 3.0.20250129
KVTIEModuleVersion = 3.0.20250129
OnlineUpgradeServerLink=https://nanflas202202.pages.dev/Latestversion.html

Environment Information
-------------------------------------------------------
Python Version = 3.12.4 64-bit
NT Kernel Version = 10.0.19045.3208 64-bit
Pyinstaller Version = 6.9.0

Upgrade Log
-------------------------------------------------------
2023-2-10  --KWY Tech
KVT Alpha 5 --From:
1.添加了GUI
2.用Python3.11重构了用C++写的屎山KVT Alpha 4项目

2023-2-16 --From:SY Technology
SYVT Alpha 5
#修复了一些已知bug
#提升了使用体验
1.更改了窗口标题和开屏显示的文字，更换了激活码
2.加入了“只杀毒”功能

2023-3-10 --From:SY Technology
SYVT Alpha 6 
1.更改了部分菜单结构
2.修复了一些已知bug（把一个os.system写成os.esystem了）
3.更改了版本号

2023-6-1
KVT 5 SE  --From:Yusulif
用C++重构了项目。删除了除一键杀毒外的所有功能。
由于KWY Tech（十月科技/SY Tech）解散了，该项目可能不会继续更新了
从此版本起，KVT不再需要激活。

2024-8-7  -From:CS2B Studio
NVT Alpha 6.0807 PyVer
-重构了UI
-增加了一些功能

2024-8-13 --From:CS2B Studio
NVT Alpha 6 PyVer
-优化了UI
-支持了保存设置项
-支持了在线更新
-支持了后台防护
-更新了KVTI库
-加入了"关于"页

2024-10-6 --CS2B Studio
NVT Alpha 6.5 
-用C++重构了项目
-增加了对命令行启动参数的支持
-移除了在线更新中对GitHub的服务器的支持(天天被墙)
[补]2025-1-30 CS2B Studio
该版本并未完成

2024-11-3 --CS2B Studio
NVT Alpha 7 Hybrid
-加入了Python版本的GUI支持
[补]2025-1-30 CS2B Studio
该版本并未完成

2025-1-16 --CS2B Studio
Alpha 7.5 Testing
-重构了UI
-重构了杀毒模块和显示被木马隐藏的文件的逻辑
-暂时移除了对重命名木马文件的支持
-由于服务器过于不稳定,暂时删去了在线升级功能
-删除了自定义设置项与"关于"页面

2025-1-28 --CS2B Studio
Alpha 7.5 RC1 [KVTVersion0.750128]
-优化了UI
-更新了KVTI库,将其整合进了主文件里

2025-1-29 --From:CS2B Studio
Alpha 7.5 RC2
-支持了本地更新
-增加了对提权的支持
-增加了日志记录模块
-更新KVTI库
-优化了UI的显示逻辑

2025-1-30 --From:CS2B Studio
Alpha 7.5 RC3
-完成了命令行交互模式
-完成了指定病毒查杀
-修复了提权模块的bug
-升级了后台防护[3.0.0130-testing]

2025-2-1  --From:Yugoros Group
Alpha 7.5 RC4
-修复了一点已知bug

2025-2-11 --From:CS2B Studio
Alpha 7.5 RC5
-恢复了更改病毒文件名的功能
-bug修复
-完成了提权逻辑的更改
-加入了NTK的主菜单（虽然还无法正常使用）
-------------------------------------------------------
If you have any problems,please report to mailto:elysiaisdead@hotmail.com
CS2B Studio is a Yugoros Group company
Yugoros Group 1963-2025,All rights reserved
"""
#####################################
import tkinter, os, sys, argparse, ctypes, logging, base64, subprocess
import tkinter.messagebox

##########
import ttkbootstrap as ttk
# from ttkbootstrap.constants import *
##########
########################################################################################################################

def get_res_path(relative_path):                 #动态处理路径
    if getattr(sys, "frozen", False):            #是否绑定资源
        base_path = sys._MEIPASS                 #获取应用临时路径
    else:                                        #否则
        base_path = os.path.abspath('.')         #手动拼接路径
    return os.path.join(base_path,relative_path) #返回处理后路径
ICON_PATH = get_res_path(os.path.join("resources","ProjectYSFIcon.ico"))
LOGO_PATH = get_res_path(os.path.join("resources","ProjectYSFBackground2.png"))
########################################################################################################################

def KillerMain(): #杀毒的主函数
    ProcessNames = ["avastsvc.exe","autolt3.exe","rundll32.exe","cmd.exe","wscript.exe"] #刺杀名单
    LocateVirProcName = 0 #用来辨别刺杀哪个进程的变量
    while LocateVirProcName <= 4:#循环操作，直至列表尾
        os.system("taskkill -f -im " + ProcessNames[LocateVirProcName] + " -t") #拼接进程名和taskkill的过程
        LocateVirProcName += 1 #移到下个进程名
    return 0

########################################################################################################################

def ShowHiddenFilesMain(): #显示文件的主函数
    ProcessNames = ["E:\\*","F:\\*","G:\\*","H:\\*","I:\\*"] #恢复名单
    LocateVirProcName = 0 #用来辨别从哪个盘显示文件的变量
    while LocateVirProcName <= 4:#循环操作，直至列表尾
                os.system("attrib -s -h" + ProcessNames[LocateVirProcName] + " -l -d") #拼接进程名和taskkill的过程
                LocateVirProcName += 1 #移到下个进程名
    return 0

########################################################################################################################

def RenVirFilesMain(): #显示文件的主函数
    DriveNames = ["E:\\","F:\\","G:\\","H:\\","I:\\"] #恢复名单
    VirFileNameBefore = ["*.lnk","RECYCLER.BIN","Skypee","*.vbe"]
    VirFileNameAfter = ["*.vir","$Recycle.Bin.{645FF040-5081-101B-9F08-00AA002F954E}","Autolt3VirusScriptFolder.{208D2C60-3AEA-1069-A2D7-08002B30309D}","*.vbe-vf"]
    LocateDiskName = 0 #用来辨别从哪个盘显示文件的变量
    while LocateDiskName <= 4:#循环操作，直至列表尾
        LocateWhichVirFile = 0 #定位文件名
        while LocateWhichVirFile < len(VirFileNameBefore):
                FileDictionaryPath1 = str(DriveNames[LocateDiskName]) + str(VirFileNameBefore[LocateWhichVirFile])
                FileDictionaryPath2 = str(DriveNames[LocateDiskName]) + str(VirFileNameAfter[LocateWhichVirFile])
                os.system("REN" , FileDictionaryPath1 , FileDictionaryPath2) #拼接进程名和taskkill的过程
                LocateWhichVirFile += 1
        LocateDiskName += 1 #移到下个进程名
    os.system("cd C:\\ProgramData\\AvastSvcp")
    os.system("ren Avastsvc.exe Avastsvc.exe.vf")
    os.system("ren C:\\Google\\Autolt3.exe Autolt3.exe.vf")
    return 0
class NTKMainForm():
    def __init__(self):
        #self.root = tkinter.Tk()
        self.root =ttk.Window("NVTA7MainWindow", "litera")
        self.root.title("NFLS Toolkit Alpha")
        self.root.iconbitmap(ICON_PATH)
        self.root.geometry("328x648")
        self.root.minsize(328,648)
        #self.root.maxsize(540,808)
        self.root["background"] = "white"
        #self.photo = tkinter.PhotoImage(file=LOGO_PATH)
        #self.label = tkinter.Label(self.root, image=self.photo)
        self.label.grid(row=0,column=0)

        button1 = tkinter.Button(self.root, text="Auto Kill(Kill Viruses + Show Files)", fg="black",width=30,
                                 font=("Segoe UI", 10), command=self.button1_event_handle)
        #button1.pack()
        button1.grid(row=1,column=0,pady=2)

        button9 = tkinter.Button(self.root, text="Enable all features", fg="black",width=30,
                                 font=("Segoe UI", 10), command=self.button9_event_handle)
        #button7.pack()
        if not ctypes.windll.shell32.IsUserAnAdmin():
            button9.grid(row=9,column=0,pady=2)

        #main.StartCommand.print_help()
        self.root.mainloop()   

    def button1_event_handle(self):
        #KillerMain()
        #ShowHiddenFilesMain()
        os.system("TASKKILL -f -im wps.exe -t");
        tkinter.messagebox.showinfo(title="NVT7消息提示",message="完毕！\n 如果没有反应，请以管理员身份运行重试！")
    def button9_event_handle(self):
        try:
            if not is_admin():
                # 使用ctypes的WinDLL加载Shell32.dll
                shell32 = ctypes.windll.shell32
                # 获取当前脚本的绝对路径
                script_path = os.path.abspath(sys.argv[0])
                print(script_path)
                print(f"Attempting to restart with elevated privileges: {script_path}")
                # 调用ShellExecuteW函数执行命令并要求UAC提升权限
                result = shell32.ShellExecuteW(
                    None,  # hwnd
                    "runas",  # lpOperation (请求管理员权限)
                    sys.executable,  # lpFile (Python解释器)
                    script_path,  # lpParameters (仅传递脚本路径)
                    None,  # lpDirectory (工作目录)
                    1  # nShowCmd (SW_SHOWNORMAL, 显示窗口)
                )
                if result <= 32:  # 如果返回值小于等于32，表示调用失败
                    raise RuntimeError(f"Failed to elevate privileges. Result code: {result}")
                # 退出当前非特权进程
                print("Privilege elevation successful. Exiting non-elevated process.")
                sys.exit()
            else:
                print("Already running with elevated privileges.")
                # 如果已经有管理员权限，则继续运行主窗口
                KVTMainForm()
        except Exception as e:
            print(f"An error occurred while trying to elevate privileges: {e}")
            tkinter.messagebox.showerror(title="NVT7错误提示", message=f"无法请求UAC提升权限: {e}")
########################################################################################################################
class KVTMainForm():
    def __init__(self):
        #self.root = tkinter.Tk()
        self.root =ttk.Window("NVTA7MainWindow", "litera")
        self.root.title("Nanflas Virus Trainer V0.7.5 RC-2")
        self.root.iconbitmap(ICON_PATH)
        self.root.geometry("328x648")
        self.root.minsize(328,648)
        #self.root.maxsize(540,808)
        self.root["background"] = "white"
        self.photo = tkinter.PhotoImage(file=LOGO_PATH)
        self.label = tkinter.Label(self.root, image=self.photo)
        self.label.grid(row=0,column=0)

        button1 = tkinter.Button(self.root, text="Auto Kill(Kill Viruses + Show Files)", fg="black",width=30,
                                 font=("Segoe UI", 10), command=self.button1_event_handle)
        #button1.pack()
        if ctypes.windll.shell32.IsUserAnAdmin():
            button1.grid(row=1,column=0,pady=2)

        button2 = tkinter.Button(self.root, text="Show Files only", fg="black",width=30,
                                 font=("Segoe UI", 10), command=self.button2_event_handle)
        #button2.pack()
        if ctypes.windll.shell32.IsUserAnAdmin():
            button2.grid(row=2,column=0,pady=2)

        button3 = tkinter.Button(self.root, text="Kill Viruses only", fg="black",width=30,
                                 font=("Segoe UI", 10), command=self.button3_event_handle)
        #button3.pack()
        button3.grid(row=3,column=0,pady=2)

        button4 = tkinter.Button(self.root, text="Kill Selected Viruses", fg="black",width=30,
                                 font=("Segoe UI", 10), command=self.button4_event_handle)
        #button4.pack()
        button4.grid(row=4,column=0,pady=2)

        button5 = tkinter.Button(self.root, text="Record Log", fg="black",width=30,
                                 font=("Segoe UI", 10), command=self.button5_event_handle)
        #button5.pack()
        button5.grid(row=5,column=0,pady=2)
             
        button6 = tkinter.Button(self.root, text="Start/Close Background Protect", fg="black",width=30,
                                 font=("Segoe UI", 10), command=self.button6_event_handle)
        #button6.pack()
        button6.grid(row=6,column=0,pady=2)

        button7 = tkinter.Button(self.root, text="Force Kill", fg="black",width=30,
                                 font=("Segoe UI", 10), command=self.button7_event_handle)
        #button7.pack()
        if ctypes.windll.shell32.IsUserAnAdmin():
            button7.grid(row=7,column=0,pady=2)
        
        button8 = tkinter.Button(self.root, text="Enter NVT Toolkit", fg="black",width=30,
                                 font=("Segoe UI", 10), command=self.button8_event_handle)
        button8.grid(row=8,column=0,pady=2)
        button9 = tkinter.Button(self.root, text="Enable all features", fg="black",width=30,
                                 font=("Segoe UI", 10), command=self.button9_event_handle)
        #button7.pack()
        if not ctypes.windll.shell32.IsUserAnAdmin():
            button9.grid(row=9,column=0,pady=2)

        #main.StartCommand.print_help()
        self.root.mainloop()   

    def button1_event_handle(self):
        KillerMain()
        ShowHiddenFilesMain()
        RenVirFilesMain()
        tkinter.messagebox.showinfo(title="NVT7消息提示",message="杀毒并恢复被隐藏的文件完毕！\n 如果没有反应，请以管理员身份运行重试！")
    def button2_event_handle(self):
        ShowHiddenFilesMain()
        tkinter.messagebox.showinfo(title="NVT7消息提示",message="恢复被隐藏的文件完毕！\n 如果没有反应，请以管理员身份运行重试！")
    def button3_event_handle(self):
        KillerMain()
        RenVirFilesMain()
        tkinter.messagebox.showinfo(title="NVT7消息提示",message="杀毒完毕！\n 如果没有反应，请以管理员身份运行重试！")
    def button4_event_handle(self):
        print("BKGD Prot Launched!")
        self.root = tkinter.Toplevel()
        self.root.title("Select Viruses")
        self.root.iconbitmap(LOGO_PATH)
        self.root.geometry("360x230")
        self.root.maxsize(width=360,height=230)
        self.virus = [("Autolt3.exe", tkinter.IntVar()), ("AvastSvc.exe", tkinter.IntVar()), ("CMD.exe", tkinter.IntVar()), ("Rundll32.exe", tkinter.IntVar()), ("WScript.exe", tkinter.IntVar()), ("Submit", tkinter.IntVar())]
        self.label = tkinter.Label(self.root, text="Select The Viruses You Want To Kill:",
                                   font=("Segoe UI", 12), justify="left")
        self.label.pack(anchor="w")
        item_row = 1
        for title, status in self.virus:
            check = tkinter.Checkbutton(self.root, text=title, onvalue=1, offvalue=0, variable=status, command=self.kill_proc_choose_handle)
            check.pack(anchor="w")
            item_row += 1
        self.content = tkinter.StringVar()
        self.show_label = tkinter.Label(self.root, textvariable=self.content,
                                        font=("Segoe UI", 10), justify="left")
        self.show_label.pack(anchor="w")
        self.root.mainloop()
    def kill_proc_choose_handle(self):
            SelectedProcess = "Selected Processes:"
            for title, status in self.virus:
                if status.get() == 1:
                    SelectedProcess += title + "、"
                    if title == "Submit":
                        for title,status in self.virus:
                            if status.get() == 1 and not title == "Submit":
                                print("TASKKILL -F -IM",title,"-T")
            self.content.set(SelectedProcess)
    def button5_event_handle(self):
        log_file_path = os.path.abspath('.') + os.sep + 'KVTA75Log.kvtl'
        if not os.path.exists(log_file_path):
            try:
                with open(log_file_path, 'w') as f:
                    f.write("")  # 创建空文件
            except Exception as e:
                print(f"无法创建日志文件: {e}")
                return
        
        NVT7Logger = setup_logger('NVT7Logger', log_file_path, level=logging.DEBUG)

        # 重定向 stdout 和 stderr 到日志文件
        sys.stdout = ConsoleToLogger(NVT7Logger, logging.INFO)
        sys.stderr = ConsoleToLogger(NVT7Logger, logging.ERROR)

        NVT7Logger.debug("工程模式已启用，开始记录详细日志...")
        tkinter.messagebox.showinfo(title="NVT7消息提示", message="已开启日志记录！")
    def button8_event_handle(self):
        tkinter.messagebox.showinfo(title="NVT7消息提示",message="开发中！将在后续版本集成")
        NTKMainForm()
        print("TLKT Launched!")
    def button7_event_handle(self):
        if tkinter.messagebox.askyesnocancel("NVT7警告","请确保您的所有工作已保存。\n保存后请点击确定……"):
            command = "-c \"import os; os.system('taskkill /f /im wininit.exe /t')\""
    
        # 请求UAC提升权限并执行命令
            request_uac_and_execute(command) 
    def button6_event_handle(self):
        print("BKGD Prot Launched!")
        self.root = tkinter.Toplevel()
        self.root.title("Background Protection Config")
        self.root.iconbitmap(LOGO_PATH)
        self.root.geometry("360x230")
        self.root.maxsize(width=360,height=230)
        self.virus = [("Autolt3.exe", tkinter.IntVar()), ("AvastSvc.exe", tkinter.IntVar()), ("CMD.exe", tkinter.IntVar()), ("Rundll32.exe", tkinter.IntVar()), ("WScript.exe", tkinter.IntVar()), ("Submit", tkinter.IntVar())]
        self.label = tkinter.Label(self.root, text="Select The Viruses You Want To Block:",
                                   font=("Segoe UI", 12), justify="left")
        self.label.pack(anchor="w")
        item_row = 1
        for title, status in self.virus:
            check = tkinter.Checkbutton(self.root, text=title, onvalue=1, offvalue=0, variable=status, command=self.bgp_proc_choose_handle)
            check.pack(anchor="w")
            item_row += 1
        self.content = tkinter.StringVar()
        self.show_label = tkinter.Label(self.root, textvariable=self.content,
                                        font=("Segoe UI", 10), justify="left")
        self.show_label.pack(anchor="w")
        self.root.mainloop()
    def bgp_proc_choose_handle(self):
            SelectedProcess = "Selected Processes:"
            for title, status in self.virus:
                if status.get() == 1:
                    SelectedProcess += title + "、"
                    if title == "Submit":
                        KBPSSettingCommand = "BackgroundProtV3.exe"
                        for title,status in self.virus:
                            if status.get() == 1 and not title == "Submit":
                                if title == "Autolt3.exe":
                                    KBPSSettingCommand = KBPSSettingCommand + " -u"
                                if title == "AvastSvc.exe":
                                    KBPSSettingCommand = KBPSSettingCommand + " -a"
                                if title == "CMD.exe":
                                    KBPSSettingCommand = KBPSSettingCommand + " -c"
                                if title == "Rundll32.exe":
                                    KBPSSettingCommand = KBPSSettingCommand + " -r"
                                if title == "WScript.exe":
                                    KBPSSettingCommand = KBPSSettingCommand + " -w"
                        print(KBPSSettingCommand)
            self.content.set(SelectedProcess)
    def button9_event_handle(self):
        try:
            if not is_admin():
                # 使用ctypes的WinDLL加载Shell32.dll
                shell32 = ctypes.windll.shell32
                # 获取当前脚本的绝对路径
                script_path = os.path.abspath(sys.argv[0])
                print(script_path)
                print(f"Attempting to restart with elevated privileges: {script_path}")
                # 调用ShellExecuteW函数执行命令并要求UAC提升权限
                result = shell32.ShellExecuteW(
                    None,  # hwnd
                    "runas",  # lpOperation (请求管理员权限)
                    sys.executable,  # lpFile (Python解释器)
                    script_path,  # lpParameters (仅传递脚本路径)
                    None,  # lpDirectory (工作目录)
                    1  # nShowCmd (SW_SHOWNORMAL, 显示窗口)
                )
                if result <= 32:  # 如果返回值小于等于32，表示调用失败
                    raise RuntimeError(f"Failed to elevate privileges. Result code: {result}")
                # 退出当前非特权进程
                print("Privilege elevation successful. Exiting non-elevated process.")
                sys.exit()
            else:
                print("Already running with elevated privileges.")
                # 如果已经有管理员权限，则继续运行主窗口
                KVTMainForm()
        except Exception as e:
            print(f"An error occurred while trying to elevate privileges: {e}")
            tkinter.messagebox.showerror(title="NVT7错误提示", message=f"无法请求UAC提升权限: {e}")
########################################################################################################################
#AI代码开始
#--------------------------------日志模块--------------------------------
class ConsoleToLogger:
    def __init__(self, logger, log_level=logging.INFO):
        self.logger = logger
        self.log_level = log_level
        self.linebuf = ''

    def write(self, buf):
        for line in buf.rstrip().splitlines():
            self.logger.log(self.log_level, line.rstrip())

    def flush(self):
        pass

def setup_logger(name, log_file, level=logging.INFO, console_output=True):
    """设置一个新的日志记录器或获取现有的日志记录器。
    
    参数:
        name (str): 日志记录器的名字。
        log_file (str): 日志文件的路径。
        level (int): 日志级别（DEBUG, INFO, WARNING, ERROR, CRITICAL）。
        console_output (bool): 是否输出到控制台，默认是 True。
        
    返回:
        logging.Logger: 配置好的日志记录器对象。
    """
    # 获取或创建一个名为 'name' 的日志记录器
    logger = logging.getLogger(name)
    
    # 如果日志记录器已经有了处理器，则直接返回，避免重复添加
    if logger.handlers:
        return logger
    
    logger.setLevel(level)

    # 创建格式化器
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    handlers = []

    # 文件处理器
    if log_file is not None:
        log_dir = os.path.dirname(log_file)
        if log_dir and not os.path.exists(log_dir):
            os.makedirs(log_dir)  # 创建日志文件所在目录
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(formatter)
        handlers.append(file_handler)
    
    # 控制台处理器，根据参数决定是否添加
    if console_output:
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        handlers.append(console_handler)

    # 添加处理器到记录器
    for handler in handlers:
        handler.setLevel(level)
        logger.addHandler(handler)

    return logger
#--------------------------------KVTI模块--------------------------------

def convert_kvti_to_array(file_path):
    """
    将一个KVTI文件的内容转化为一个Python数组，其中每个键值对作为元组(x, y)存储。

    参数:
    file_path (str): 输入的KVTI文件的路径。

    返回:
    list: 包含键值对的数组，格式为 [(x1, y1), (x2, y2), ...]
    """
    data_array = []

    try:
        with open(file_path, 'r') as file:
            content = file.read()
            lines = [line.strip() for line in content.splitlines() if line.strip()]

            for line in lines:
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip('[]').strip()  # Remove brackets from the value

                    # Handle Base64 encoded media files
                    if value.startswith('base64:'):
                        value = value[7:]  # Remove 'base64:' prefix

                    data_array.append((key, value))

    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
    except Exception as e:
        print(f"Error reading or parsing file: {e}")

    return data_array
#--------------------------------KVTIE模块--------------------------------
def convert_kvtie_to_array(file_path):
    """
    将一个KVTIE文件的内容转化为一个Python数组，其中每个键值对作为元组(x, y)存储。

    参数:
    file_path (str): 输入的KVTIE文件的路径。

    返回:
    list: 包含键值对的数组，格式为 [(x1, y1), (x2, y2), ...]
    """
    data_array = []

    try:
        with open(file_path, 'rb') as file:
            encrypted_content = file.read()
            decrypted_content = base64.b64decode(encrypted_content).decode('utf-8')
            lines = [line.strip() for line in decrypted_content.splitlines() if line.strip()]

            for line in lines:
                if '=' in line:
                    key, value = line.split('=', 1)
                    key = key.strip()
                    value = value.strip('[]').strip()  # Remove brackets from the value

                    # Handle Base64 encoded media files
                    if value.startswith('base64:'):
                        value = value[7:]  # Remove 'base64:' prefix

                    data_array.append((key, value))

    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
    except Exception as e:
        print(f"Error reading or parsing file: {e}")

    return data_array
#--------------------------------检索模块--------------------------------
def get_base64_value_by_key(data_array, key):
    """
    根据给定的键在数据数组中查找对应的Base64编码的值。

    参数:
    data_array (list): 包含键值对的数组，格式为 [(x1, y1), (x2, y2), ...]
    key (str): 要查找的键。

    返回:
    str or None: 对应的Base64编码的值，如果未找到则返回 None。
    """
    for k, v in data_array:
        if k == key:
            return v
    return None
#--------------------------------文件输出模块--------------------------------
def save_base64_to_file(base64_data, output_file_path):
    """
    将Base64编码的数据解码并保存到指定路径的文件中。

    参数:
    base64_data (str): Base64编码的数据。
    output_file_path (str): 目标文件的路径。

    返回:
    bool: 操作是否成功。
    """
    try:
        decoded_data = base64.b64decode(base64_data)
        with open(output_file_path, 'wb') as file:
            file.write(decoded_data)
        print(f"File saved successfully to {output_file_path}")
        return True
    except Exception as e:
        print(f"Error saving file: {e}")
        return False
#--------------------------------提权模块--------------------------------
def request_uac_and_execute(command):
    try:
        # 使用ctypes的WinDLL加载Shell32.dll
        shell32 = ctypes.windll.shell32
        
        # 调用ShellExecuteW函数执行命令并要求UAC提升权限
        result = shell32.ShellExecuteW(
            None,  # hwnd
            "runas",  # lpOperation
            sys.executable,  # lpFile
            command,  # lpParameters
            None,  # lpDirectory
            1  # nShowCmd (SW_SHOWNORMAL)
        )

        if result <= 32:  # 如果返回值小于等于32，表示调用失败
            raise RuntimeError("Failed to elevate privileges")

    except Exception as e:
        print(f"无法请求UAC提升权限: {e}")
##--------------------------------提权模块2--------------------------------
def is_admin():
    """检查当前进程是否有管理员权限"""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

#AI代码结束
########################################################################################################################

def main():
    os.system('chcp 65001')#来自：Auto_release_virus1.py From Xyz Studio
    StartCommand = argparse.ArgumentParser() #接受启动参数
    #以下变量中的action='store_true'是AI让加的，我不知道为什么要这么干（AI给的解释是自动传参为True，但是我找的参考文章里没说。）
    #argparse的官网：https://docs.python.org/zh-cn/3.9/library/argparse.html#parents
    StartCommand.add_argument('-a', '--AutoKill', action='store_true', help="自动查杀")
    StartCommand.add_argument('-c','--CommandLine', action='store_true', help="命令行模式")
    StartCommand.add_argument('-t', "--TUI", action='store_true', help="TUI模式")
    StartCommand.add_argument('-f', "--ForceKill", action='store_true', help="强行查杀（慎用！）")
    StartCommand.add_argument("-s","--KillSelectedProc", nargs='+', help="查杀指定进程")
    StartCommand.add_argument("-d", "--EnableDebugMode", action='store_true', help="开启工程模式（记录日志）")
    StartCommand.add_argument("-u", "--Upgrade" , help="导入升级文件")
    #定义启动参数完毕
    Command = StartCommand.parse_args()#接收启动参数
    print(os.path.abspath('.'))
    #AI写的
    if Command.Upgrade and any([Command.CommandLine, Command.TUI, Command.AutoKill, Command.EnableDebugMode, Command.KillSelectedProc, Command.ForceKill]):
        StartCommand.error("-u/--Upgrade 不能与其他参数共同使用。")

    if Command.AutoKill:
        if any([Command.CommandLine, Command.TUI, Command.KillSelectedProc, Command.ForceKill]) or (not Command.EnableDebugMode and len(sys.argv) > 2):
            StartCommand.error("-a/--AutoKill 只能与 -d/--EnableDebugMode 一起使用，不能与其他参数共同使用。")

    if sum([Command.CommandLine, Command.TUI, bool(Command.KillSelectedProc)]) > 1:
        StartCommand.error("-c/--CommandLine, -t/--TUI 与 -s/--KillSelectedProc 无法共同使用。")
    if Command.AutoKill:
        print("开始自动查杀...")
        KillerMain()  # 调用杀毒主函数
        if Command.EnableDebugMode:
            log_file_path = os.path.abspath('.') + os.sep + 'KVTA75Log.kvtl'
            if not os.path.exists(log_file_path):
                try:
                    with open(log_file_path, 'w') as f:
                        f.write("")  # 创建空文件
                except Exception as e:
                    print(f"无法创建日志文件: {e}")
                    return
        
            NVT7Logger = setup_logger('NVT7Logger', log_file_path, level=logging.DEBUG)

            # 重定向 stdout 和 stderr 到日志文件
            sys.stdout = ConsoleToLogger(NVT7Logger, logging.INFO)
            sys.stderr = ConsoleToLogger(NVT7Logger, logging.ERROR)

            NVT7Logger.debug("工程模式已启用，开始记录详细日志...")
            print("开启工程模式，记录日志...")

    elif Command.CommandLine:
        print("进入命令行模式...")
        print("꧁~-----WELCOME TO NFLS VirusTrainer Alpha 7.5 RC2!-----~꧂")
        print("_____________________________________________________________")
        print("|                        [WARNING]                           |")
        print("|            This is a testing version of NVT                |")
        print("|           Do not use it in working environment             |")
        print("| For more information, please visit Nanflas202202.pages.dev |")
        print("|____________________________________________________________|")
        while True:
            option = input("ENTER YOUR OPTION>")
            match(option):
                case "Autokill":
                    print("Start Killing Viruses...")
                    KillerMain()
                    print("Start Showing Hidden Files...")
                    ShowHiddenFilesMain
                case "KillVirOnly":
                    print("Start Killing Viruses...")
                    KillerMain()
                case "ShowHiddenFileOnly":
                    print("Start Showing Hidden Files...")
                    ShowHiddenFilesMain
                case "KillSelectedVir":
                    KillRundll32 = input("Kill Rundll32.exe?(y/N)>")
                    KillAvastSvc = input("Kill AvastSvc.exe?>(y/N)")
                    KillAutolt3 = input("Kill Autolt3.exe>(y/N)>")
                    KillCMD = input("Kill CMD.exe?(y/N)>")
                    KillWScript = input("Kill WScript.exe?(y/N)>")
                    if KillAutolt3 == "y":
                        print("TASKKILL -F -IM Autolt3.exe -T")
                    if KillAvastSvc == "y":
                        print("TASKKILL -F -IM Avastsvc.exe -T")
                    if KillCMD == "y":
                        print("TASKKILL -F -IM CMD.exe -T")
                    if KillRundll32 == "y":
                        print("TASKKILL -F -IM Rundll32.exe -T")
                    if KillWScript == "y":
                        print("TASKKILL -F -IM WScript.exe -T")
                    
                case "EnterDebugMode":
                    log_file_path = os.path.abspath('.') + os.sep + 'KVTA75Log.kvtl'
                    if not os.path.exists(log_file_path):
                        try:
                            with open(log_file_path, 'w') as f:
                                f.write("")  # 创建空文件
                        except Exception as e:
                            print(f"无法创建日志文件: {e}")
                            return
        
                    NVT7Logger = setup_logger('NVT7Logger', log_file_path, level=logging.DEBUG)

                    # 重定向 stdout 和 stderr 到日志文件
                    sys.stdout = ConsoleToLogger(NVT7Logger, logging.INFO)
                    sys.stderr = ConsoleToLogger(NVT7Logger, logging.ERROR)

                    NVT7Logger.debug("工程模式已启用，开始记录详细日志...")
                    print("Start Logging...")
                case "ForceKill":
                    print("请注意：强行查杀仅在还原卡状态正常时生效！")
                    input("如果您已保存好您的工作，请按下<Enter>键")
                    # 构造需要执行的命令，注意这里的命令是直接作为字符串传递
                    command = "-c \"import os; os.system('taskkill /f /im wininit.exe /t')\""
                    request_uac_and_execute(command) 
                case "BackgroundProt":
                    print("NFLS Virus Trainer Alpha 7.5 RC2 Background Protection Setting Process")
                    print("-----------------------------------------------------------------------")
                    KBPSSettingCommand = "BackgroundProtV3.exe"
                    BlockRundll32 = input("Block Rundll32.exe?(y/N)>")
                    BlockAvastSvc = input("Block AvastSvc.exe?>(y/N)")
                    BlockAutolt3 = input("Block Autolt3.exe>(y/N)>")
                    BlockCMD = input("Block CMD.exe?(y/N)>")
                    BlockWScript = input("Block WScript.exe?(y/N)>")
                    if BlockAutolt3 == "y":
                        KBPSSettingCommand = KBPSSettingCommand + " -u"
                    if BlockAvastSvc == "y":
                        KBPSSettingCommand = KBPSSettingCommand + " -a"
                    if BlockCMD == "y":
                        KBPSSettingCommand = KBPSSettingCommand + " -c"
                    if BlockRundll32 == "y":
                        KBPSSettingCommand = KBPSSettingCommand + " -r"
                    if BlockWScript == "y":
                        KBPSSettingCommand = KBPSSettingCommand + " -w"
                    print(KBPSSettingCommand)
                case "h" :
                    print("--------NFLS Virus Trainer Alpha 7.5 RC5 CommandLine Mode Help--------- ")
                    print("      Commands      |                       Uses                        ")
                    print("----------------------------------------------------------------------- ")
                    print("      Autokill      | Kill All Viruses and Show Files Hidden By Viruses ")
                    print("    KillVirOnly     |               Only Kill All Viruses               ")
                    print("ShowHiddenFilesOnly |         Only Show Files Hidden By Viruses         ")
                    print("  KillSelectedVir   |            Only Kill Selected Viruses             ")
                    print("  EnterDebugMode    |                    Record Log                     ")
                    print("     ForceKill      |         Kill Viruses In Some Special Ways         ")
                    print("  BackgroundProt    |       Launch Background Protection Service        ")
                    print("       Quit         |              Quit NFLS Virus Trainer              ")
                    print("       help         |                  Show This Page                   ")
                    print("----------------------------------------------------------------------- ")
                    print("[WARNING]IF YOU ARE USING CMD,DO NOT USE AUTOKILL.\n AUTOKILL WILL KILL CMD.EXE,SO YOU WON'T BE ABLE TO FINISH OTHER OPTIONS")
                    #print("         h          |                  Show This Page                   ")
                case "help":
                    print("--------NFLS Virus Trainer Alpha 7.5 RC4 CommandLine Mode Help--------- ")
                    print("      Commands      |                       Uses                        ")
                    print("----------------------------------------------------------------------- ")
                    print("      Autokill      | Kill All Viruses and Show Files Hidden By Viruses ")
                    print("    KillVirOnly     |               Only Kill All Viruses               ")
                    print("ShowHiddenFilesOnly |         Only Show Files Hidden By Viruses         ")
                    print("  KillSelectedVir   |            Only Kill Selected Viruses             ")
                    print("  EnterDebugMode    |                    Record Log                     ")
                    print("     ForceKill      |         Kill Viruses In Some Special Ways         ")
                    print("  BackgroundProt    |       Launch Background Protection Service        ")
                    print("       Quit         |              Quit NFLS Virus Trainer              ")
                    print("       help         |                  Show This Page                   ")
                    print("----------------------------------------------------------------------- ")
                    print("[WARNING]IF YOU ARE USING CMD,DO NOT USE AUTOKILL.\n AUTOKILL WILL KILL CMD.EXE,SO YOU WON'T BE ABLE TO FINISH OTHER OPTIONS")
                case "Quit":
                    print("Thank for using NVT Alpha 7.5 RC2")
                    halt = input("Press <Enter> to continue......")
                    sys.exit(0)
                case _:
                    print("Unknown Command!!!")
    elif Command.TUI:
        print("进入TUI模式...")
        print("开发中！")
    elif Command.ForceKill:
        print("请注意：强行查杀仅在还原卡状态正常时生效！")
        input("如果您已保存好您的工作，请按下<Enter>键")
        # 构造需要执行的命令，注意这里的命令是直接作为字符串传递
        command = "-c \"import os; os.system('taskkill /f /im wininit.exe /t')\""
    
        # 请求UAC提升权限并执行命令
        request_uac_and_execute(command)   

    elif Command.KillSelectedProc:
                    KillRundll32 = input("Kill Rundll32.exe?(y/N)>")
                    KillAvastSvc = input("Kill AvastSvc.exe?>(y/N)")
                    KillAutolt3 = input("Kill Autolt3.exe>(y/N)>")
                    KillCMD = input("Kill CMD.exe?(y/N)>")
                    KillWScript = input("Kill WScript.exe?(y/N)>")
                    if KillAutolt3 == "y":
                        print("TASKKILL -F -IM Autolt3.exe -T")
                    if KillAvastSvc == "y":
                        print("TASKKILL -F -IM Avastsvc.exe -T")
                    if KillCMD == "y":
                        print("TASKKILL -F -IM CMD.exe -T")
                    if KillRundll32 == "y":
                        print("TASKKILL -F -IM Rundll32.exe -T")
                    if KillWScript == "y":
                        print("TASKKILL -F -IM WScript.exe -T")

    elif Command.EnableDebugMode and not Command.AutoKill:
        # 在这里初始化日志记录器
        log_file_path = os.path.abspath('.') + os.sep + 'KVTA75Log.kvtl'
        if not os.path.exists(log_file_path):
            try:
                with open(log_file_path, 'w') as f:
                    f.write("")  # 创建空文件
            except Exception as e:
                print(f"无法创建日志文件: {e}")
                return
        
        NVT7Logger = setup_logger('NVT7Logger', log_file_path, level=logging.DEBUG)

        # 重定向 stdout 和 stderr 到日志文件
        sys.stdout = ConsoleToLogger(NVT7Logger, logging.INFO)
        sys.stderr = ConsoleToLogger(NVT7Logger, logging.ERROR)

        NVT7Logger.debug("工程模式已启用，开始记录详细日志...")
        print("Start Logging...")
    elif Command.Upgrade:
        KVTVerison = 0.750129
        try:
            UpgraderData = convert_kvtie_to_array(Command.Upgrade)
            Version_in_upgrade_pack = get_base64_value_by_key(UpgraderData,"Version")
            if Version_in_upgrade_pack is not None:
                try:
                    Version_in_upgrade_pack = float(Version_in_upgrade_pack)
                except ValueError:
                    print(f"Error: The value for key '{Version_in_upgrade_pack}' cannot be converted to a float.")
                    sys.exit(1)
            else:
                print(f"Key '{Version_in_upgrade_pack}' not found.")
            UpgradeFiledataPath = get_base64_value_by_key(UpgraderData,"UpgradeFilePath")
            ReplaceMainFileOrNot = get_base64_value_by_key(UpgraderData,"ReplaceAll")
            UpgradeFileStorgePath = os.path.abspath('.') + os.sep + "TMP"
            if Version_in_upgrade_pack > KVTVerison:
                UpgradeFinalCheck = input("Upgrade Aviliable,upgrade?(y/N)>")
                if UpgradeFinalCheck == 'y' or UpgradeFinalCheck == 'Y':
                    if ReplaceMainFileOrNot == "True":
                        os.system("mkdir TMP")
                        print("copy",UpgradeFiledataPath,UpgradeFileStorgePath)
                        print("Upgrade prepared finished.")
                        print("This programme will quit to finish upgrade.")
                        print("Press <Enter> to continue......")
                        os.system("start",UpgradeFileStorgePath,"install.bat")
                        sys.exit(0);
                    else:
                        print("copy",UpgradeFiledataPath,os.path.abspath('.'))
                        print("Upgrade prepared finished.")
                        print("Press <Enter> to continue......")
                else:
                    print("Upgrade cancelled.")
                    print("Press <Enter> to continue......")
        except Exception as err:
            print("[Error]Upgrade Failure:%s" % err)
            halt = input("Upgrade Failed. Please check if there's something wrong with your upgrade config file or sth else.\n Press <Enter> to continue......")
            sys.exit(1)
        
    # 如果没有提供任何参数，则打印帮助信息
    #if len(sys.argv) == 1:
    #    StartCommand.print_help()
    
    #AI代码结束
    else:
        KVTMainForm()
        #StartCommand.print_help()
########################################################################################################################
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logging.error(f"主程序运行时发生错误: {e}")
        raise