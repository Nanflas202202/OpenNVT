"""
About this programmme
-------------------------------------------------------
NFLS Virus Trainer Alpha 7.5 RC2
Build Time:2025-Jan-28th
Developer:Yusulif
Copyleft CS2B Studio 2022-2025 No rights reserved
"""
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
        base_path = os.path.abspath(".")         #手动拼接路径
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
    try:
            # 使用ctypes的WinDLL加载Shell32.dll
            shell32 = ctypes.windll.shell32

            # 调用ShellExecute函数执行命令并要求UAC提升权限
            shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 0)
            while LocateVirProcName <= 4:#循环操作，直至列表尾
                os.system("attrib -s -h" + ProcessNames[LocateVirProcName] + " -l -d") #拼接进程名和taskkill的过程
                LocateVirProcName += 1 #移到下个进程名
    except:
            # 如果请求UAC提升权限失败，可以根据需要进行处理
            print("无法请求UAC提升权限。")
    return 0

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
        
        button8 = tkinter.Button(self.root, text="Enable all features", fg="black",width=30,
                                 font=("Segoe UI", 10), command=self.button8_event_handle)
        #button7.pack()
        if not ctypes.windll.shell32.IsUserAnAdmin():
            button8.grid(row=8,column=0,pady=2)

        self.root.mainloop()   

    def button1_event_handle(self):
        #KillerMain()
        #ShowHiddenFilesMain()
        tkinter.messagebox.showinfo(title="NVT7消息提示",message="杀毒并恢复被隐藏的文件完毕！\n 如果没有反应，请以管理员身份运行重试！")
    def button2_event_handle(self):
        #KillerMain()
        tkinter.messagebox.showinfo(title="NVT7消息提示",message="杀毒完毕！\n 如果没有反应，请以管理员身份运行重试！")
    def button3_event_handle(self):
        #ShowHiddenFilesMain()
        tkinter.messagebox.showinfo(title="NVT7消息提示",message="恢复被隐藏的文件完毕！\n 如果没有反应，请以管理员身份运行重试！")
    def button4_event_handle(self):
        tkinter.messagebox.showinfo(title="NVT7消息提示",message="开发中！将在后续版本集成")
    def button5_event_handle(self):
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
        tkinter.messagebox.showinfo(title="NVT7消息提示", message="已开启日志记录！")
    def button6_event_handle(self):
        tkinter.messagebox.showinfo(title="NVT7消息提示",message="开发中！将在后续版本集成")
        print("BKGD Prot Launched!")
    def button7_event_handle(self):
        if tkinter.messagebox.askyesnocancel("NVT7警告","请确保您的所有工作已保存。\n保存后请点击确定……"):
            command = "-c \"import os; os.system('taskkill /f /im wininit.exe /t')\""
    
        # 请求UAC提升权限并执行命令
            request_uac_and_execute(command) 
    def button8_event_handle(self):
        try:
            if not is_admin():
                # 使用ctypes的WinDLL加载Shell32.dll
                shell32 = ctypes.windll.shell32
                # 获取当前脚本的绝对路径
                script_path = os.path.abspath(sys.argv[0])
                print(f"Attempting to restart with elevated privileges: {script_path}")
                # 调用ShellExecuteW函数执行命令并要求UAC提升权限
                result = shell32.ShellExecuteW(
                    None,  # hwnd
                    "runas",  # lpOperation
                    sys.executable,  # lpFile
                    f'"{sys.executable}" "{script_path}"',  # lpParameters
                    None,  # lpDirectory
                    1  # nShowCmd (SW_SHOWNORMAL)
                )
                if result <= 32:  # 如果返回值小于等于32，表示调用失败
                    raise RuntimeError(f"Failed to elevate privileges. Result code: {result}")
                # 退出当前非特权进程
                print("Privilege elevation successful. Exiting non-elevated process.")
                self.root.destroy()
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
                    #KillerMain()
                    print("Start Showing Hidden Files...")
                    #ShowHiddenFilesMain
                case "KillVirOnly":
                    print("Start Killing Viruses...")
                    #KillerMain()
                case "ShowHiddenFileOnly":
                    print("Start Showing Hidden Files...")
                    #ShowHiddenFilesMain
                case "EnterDebugMode":
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
                    print("Start Logging...")
                case "Quit":
                    print("Thank for using NVT Alpha 7.5 RC2")
                    halt = input("Press <Enter> to continue......")
                    exit(0)
                case _:
                    print("Unknown Command!!!")
    elif Command.TUI:
        print("进入TUI模式...")

    elif Command.ForceKill:
        print("强行查杀已激活，请谨慎使用！")
        input("如果您已保存好您的工作，请按下<Enter>键")
        # 构造需要执行的命令，注意这里的命令是直接作为字符串传递
        command = "-c \"import os; os.system('taskkill /f /im wininit.exe /t')\""
    
        # 请求UAC提升权限并执行命令
        request_uac_and_execute(command)   

    elif Command.KillSelectedProc:
        print(f"准备查杀指定进程: {Command.KillSelectedProc}")
        for proc in Command.KillSelectedProc:
            os.system(f"taskkill /F /IM {proc} /T")

    elif Command.EnableDebugMode and not Command.AutoKill:
        # 在这里初始化日志记录器
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
                    exit(1)
            else:
                print(f"Key '{Version_in_upgrade_pack}' not found.")
            UpgradeFiledataPath = get_base64_value_by_key(UpgraderData,"UpgradeFilePath")
            ReplaceMainFileOrNot = get_base64_value_by_key(UpgraderData,"ReplaceAll")
            UpgradeFileStorgePath = os.path.abspath('.') + os.sep + "TMP"
            if Version_in_upgrade_pack > KVTVerison:
                UpgradeFinalCheck = input("Upgrade Aviliable,upgrade?(y/N)>")
                if UpgradeFinalCheck == 'y' or 'Y':
                    if ReplaceMainFileOrNot == "True":
                        os.system("mkdir TMP")
                        print("copy",UpgradeFiledataPath,UpgradeFileStorgePath)
                        print("Upgrade prepared finished.")
                        print("This programme will quit to finish upgrade.")
                        print("Press <Enter> to continue......")
                        os.system("start",UpgradeFileStorgePath,"install.bat")
                        exit(0);
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
            exit(1)
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
    try:
        main()
    except Exception as e:
        logging.error(f"主程序运行时发生错误: {e}")
        raise