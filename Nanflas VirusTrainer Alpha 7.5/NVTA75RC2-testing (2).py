"""
About this programmme
-------------------------------------------------------
NFLS Virus Trainer Alpha 7.5 RC2
Build Time:2025-Jan-28th
Developer:Yusulif
Copyleft CS2B Studio 2022-2025 No rights reserved
"""
import tkinter,os,sys,argparse,subprocess,ctypes,logging
import tkinter.messagebox
import tkinter as tk
##########
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
##########
########################################################################################################################

def get_res_path(relative_path):                 #动态处理路径
    if getattr(sys, "frozen", False):            #是否绑定资源
        base_path = sys._MEIPASS                 #获取应用临时路径
    else:                                        #否则
        base_path = os.path.abspath(".")         #手动拼接路径
    return os.path.join(base_path,relative_path) #返回处理后路径
ICON_PATH = get_res_path(os.path.join("resources","ProjectYSFIcon.ico"))
LOGO_PATH = get_res_path(os.path.join("resources","ProjectYSFBackground2.png"))
########################################################################################################################

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

def KillerMain(): #杀毒的主函数
    ProcessNames = ["avastsvc.exe","autolt3.exe","rundll32.exe","cmd.exe","wscript.exe"] #刺杀名单
    LocateVirProcName = 0 #用来辨别刺杀哪个进程的变量
    while LocateVirProcName <= 4:#循环操作，直至列表尾
        print(f"Killing process {ProcessNames[LocateVirProcName]}")
        os.system(f"taskkill -f -im {ProcessNames[LocateVirProcName]} -t") #拼接进程名和taskkill的过程
        LocateVirProcName += 1 #移到下个进程名
    return 0

def ShowHiddenFilesMain(): #显示文件的主函数
    ProcessNames = ["E:\\*","F:\\*","G:\\*","H:\\*","I:\\*"] #恢复名单
    LocateVirProcName = 0 #用来辨别从哪个盘显示文件的变量
    try:
        # 使用ctypes的WinDLL加载Shell32.dll
        shell32 = ctypes.windll.shell32

        # 调用ShellExecute函数执行命令并要求UAC提升权限
        shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 0)
        while LocateVirProcName <= 4:#循环操作，直至列表尾
            print(f"Revealing hidden files on drive {ProcessNames[LocateVirProcName]}")
            os.system(f"attrib -s -h {ProcessNames[LocateVirProcName]} -l -d") #拼接进程名和taskkill的过程
            LocateVirProcName += 1 #移到下个进程名
    except Exception as e:
        # 如果请求UAC提升权限失败，可以根据需要进行处理
        print(f"无法请求UAC提升权限: {e}")
    return 0

class KVTMainForm():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Nanflas Virus Trainer V0.7.5 RC-1")
        self.root.iconbitmap(ICON_PATH)
        self.root.geometry("328x648")
        self.root.minsize(328, 648)
        self.root["background"] = "white"
        
        self.photo = tk.PhotoImage(file=LOGO_PATH)
        self.label = tk.Label(self.root, image=self.photo)
        self.label.grid(row=0, column=0, pady=(10, 10))

        button1 = tk.Button(self.root, text="Auto Kill(Kill Viruses + Show Files)", fg="black", width=30,
                            font=("Segoe UI", 10))
        button1.bind("<Button-1>", lambda WhenOnClick: self.button1_event_handle(WhenOnClick))
        button1.grid(row=1, column=0, pady=2)

        button2 = tk.Button(self.root, text="Show Files only", fg="black", width=30,
                            font=("Segoe UI", 10))
        button2.bind("<Button-1>", lambda WhenOnClick: self.button2_event_handle(WhenOnClick))
        button2.grid(row=2, column=0, pady=2)

        button3 = tk.Button(self.root, text="Kill Viruses only", fg="black", width=30,
                            font=("Segoe UI", 10))
        button3.bind("<Button-1>", lambda WhenOnClick: self.button3_event_handle(WhenOnClick))
        button3.grid(row=3, column=0, pady=2)

        button4 = tk.Button(self.root, text="Kill Selected Viruses", fg="black", width=30,
                            font=("Segoe UI", 10))
        button4.bind("<Button-1>", lambda WhenOnClick: self.button4_event_handle(WhenOnClick))
        button4.grid(row=4, column=0, pady=2)

        button5 = tk.Button(self.root, text="Record Log", fg="black", width=30,
                            font=("Segoe UI", 10))
        button5.bind("<Button-1>", lambda WhenOnClick: self.button5_event_handle(WhenOnClick))
        button5.grid(row=5, column=0, pady=2)
             
        button6 = tk.Button(self.root, text="Start/Close Background Protect", fg="black", width=30,
                            font=("Segoe UI", 10))
        button6.bind("<Button-1>", lambda WhenOnClick: self.button6_event_handle(WhenOnClick))
        button6.grid(row=6, column=0, pady=2)

        button7 = tk.Button(self.root, text="Force Kill", fg="black", width=30,
                            font=("Segoe UI", 10))
        button7.bind("<Button-1>", lambda WhenOnClick: self.button7_event_handle(WhenOnClick))
        button7.grid(row=7, column=0, pady=2)

        self.root.mainloop()   

    def button1_event_handle(self, WhenOnClick):
        #KillerMain()
        #ShowHiddenFilesMain()
        tk.messagebox.showinfo(title="NVT7消息提示", message="杀毒并恢复被隐藏的文件完毕！\n 如果没有反应，请以管理员身份运行重试！")

    def button2_event_handle(self, WhenOnClick):
        #KillerMain()
        tk.messagebox.showinfo(title="NVT7消息提示", message="杀毒完毕！\n 如果没有反应，请以管理员身份运行重试！")

    def button3_event_handle(self, WhenOnClick):
        ShowHiddenFilesMain()
        tk.messagebox.showinfo(title="NVT7消息提示", message="恢复被隐藏的文件完毕！\n 如果没有反应，请以管理员身份运行重试！")

    def button4_event_handle(self, WhenOnClick):
        tk.messagebox.showinfo(title="NVT7消息提示", message="开发中！将在后续版本集成")

    def button5_event_handle(self, WhenOnClick):
        log_file_path = 'D:\\KVTA75Log.kvtl'
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
        tk.messagebox.showinfo(title="NVT7消息提示", message="已开启日志记录！")

    def button6_event_handle(self, WhenOnClick):
        tk.messagebox.showinfo(title="NVT7消息提示", message="开发中！将在后续版本集成")

    def button7_event_handle(self, WhenOnClick):
        
        if tk.messagebox.askyesnocancel("NVT7警告", "请确保您的所有工作已保存。\n保存后请点击确定……"):
            try:
                # 使用ctypes的WinDLL加载Shell32.dll
                shell32 = ctypes.windll.shell32

                # 调用ShellExecute函数执行命令并要求UAC提升权限
                result = shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 0)
            
                if result <= 32:  # ShellExecuteW 返回值小于等于32表示失败
                    raise Exception(f"ShellExecuteW failed with error code: {result}")

                # 执行 taskkill 命令
                command_result = os.system("taskkill -f -im wininit.exe -t")  # 使用 notepad.exe 测试
            
                if command_result != 0:
                    raise Exception(f"taskkill command failed with error code: {command_result}")

                print("Force kill operation completed successfully.")
            except Exception as e:
                print(f"An error occurred during the force kill operation: {e}")
                tk.messagebox.showerror(title="NVT7错误", message=f"发生错误: {e}")
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
            print("开启工程模式，记录日志...")

    elif Command.CommandLine:
        print("进入命令行模式...")

    elif Command.TUI:
        print("进入TUI模式...")

    elif Command.ForceKill:
        print("强行查杀已激活，请谨慎使用！")
        input("如果您已保存好您的工作，请按下<Enter>键");
        try:
            # 使用ctypes的WinDLL加载Shell32.dll
            shell32 = ctypes.windll.shell32

            # 调用ShellExecute函数执行命令并要求UAC提升权限
            shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 0)
            os.system("taskkill -f -im wininit.exe -t")
        except:
            # 如果请求UAC提升权限失败，可以根据需要进行处理
            print("无法请求UAC提升权限。")

    elif Command.KillSelectedProc:
        print(f"准备查杀指定进程: {Command.KillSelectedProc}")
        for proc in Command.KillSelectedProc:
            os.system(f"taskkill /F /IM {proc} /T")

    elif Command.EnableDebugMode and not Command.AutoKill:
        # 在这里初始化日志记录器
        NVT7Logger = setup_logger('NVT7Logger', '%Appdata%\KVTA75Log.kvtl', level=logging.DEBUG)
        NVT7Logger.setLevel(logging.DEBUG)
        NVT7Logger.debug("工程模式已启用，开始记录详细日志...")
    elif Command.Upgrade:
        print(f"导入升级文件: {Command.Upgrade}")
        """
    # 如果没有提供任何参数，则打印帮助信息
    if len(sys.argv) == 1:
    StartCommand.print_help()
        """
    #AI代码结束
    else:
        KVTMainForm()
########################################################################################################################
if __name__ == "__main__":
    main()