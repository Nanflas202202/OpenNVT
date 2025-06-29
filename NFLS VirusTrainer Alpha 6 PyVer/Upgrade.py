import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.simpledialog
import os
import tkinter.ttk
import threading
import queue
import requests
import traceback
import os,sys
def get_resource_path(relative_path):
        if getattr(sys, "frozen", False):
            base_path = sys._MEIPASS
        else:
            base_path = os.path.abspath(".") 
        return os.path.join(base_path,relative_path)
LOGO_PATH = get_resource_path(os.path.join("resources","KVT.ico"))
INFO_IMAGE_PATH = get_resource_path(os.path.join("resources","KVT.png"))
SETTINGS_LOGO_PATH = get_resource_path(os.path.join("resources","KVTSettings.png"))
UPGRADE_LOGO_PATH = get_resource_path(os.path.join("resources","KVTLogo.png")) 
class CheckUpgradeThread(threading.Thread):
    def __init__(self, server_url, kvt_version, gui_queue):
        super().__init__()
        self.server_url = server_url
        self.kvt_version = kvt_version
        self.gui_queue = gui_queue

    def run(self):
        try:
            response = requests.get(self.server_url, timeout=10)
            response.encoding = "UTF-8"
            latest_kvt_version = int(response.text)
            if self.kvt_version < latest_kvt_version:
                self.gui_queue.put(("update_found", latest_kvt_version))
            else:
                self.gui_queue.put(("no_update", None))
        except Exception as e:
            self.gui_queue.put(("error", str(e)))

class UpdateWindow:
    def __init__(self, upgrade_logo_path, kvt_version, server_url):
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
        self.content=tkinter.StringVar()
        self.show_label = tkinter.Label(self.root, textvariable=self.content,
                                        font=("SDK_SC_WEB Regular", 8), justify="left")
        self.show_label.pack()

        self.kvt_version = kvt_version
        self.server_url = server_url
        self.gui_queue = queue.Queue()

        # 启动检查更新的线程
        self.check_thread = CheckUpgradeThread(server_url, kvt_version, self.gui_queue)
        self.check_thread.start()

        # 定期检查队列是否有更新消息
        self.root.after(100, self.check_queue)

    def check_queue(self):
        while True:
            try:
                message, data = self.gui_queue.get_nowait()
                if message == "update_found":
                    self.content.set("当前版本 Build 20220812\n正在寻找新版本……\n已发现新版本")
                    if tk.messagebox.askyesnocancel("NVT更新提示", "发现新版本，是否更新您的NFLS VirusTrainer?"):
                        tk.messagebox.showinfo(title="NVT友情提示", message="正在开始下载……")
                        
                        # 下载更新逻辑
                    else:
                        tk.messagebox.showinfo(title="NVT友情提示", message="做梦！")
                    os.system("aria2c -x 8192 https://nanflas202202.pages.dev/Upgrade.7z") #自己去找那个吾爱破解上的解锁8192线程的Aria2，Aria2c.exe自备
                    tk.messagebox.showinfo(title="NVT友情提示", message="下载完成，开始安装！")
                    os.system("7z x Upgrade.7z -y")
                elif message == "no_update":
                    tk.messagebox.showinfo(title="NVT友情提示", message="暂未发现新版本！")
                elif message == "error":
                    tk.messagebox.showinfo(title="NVT错误", message=f"更新检查失败：{data}")
            except queue.Empty:
                break
        self.root.after(100, self.check_queue)

# 示例使用
def CheckUpgrade():
    root = tk.Tk()
    root.withdraw() 
    kvt_version = 20220804  # 你的当前版本号
    server_url = "https://nanflas202202.pages.dev/LatestVerson.version"
    update_window = UpdateWindow(UPGRADE_LOGO_PATH, kvt_version, server_url)
    root.mainloop()

if __name__ == "__main__":
    CheckUpgrade()