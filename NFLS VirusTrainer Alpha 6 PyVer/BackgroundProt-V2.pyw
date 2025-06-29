#coding:UTF-8
import psutil,tkinter,traceback,time,KVTI_options
from tkinter import messagebox
def main():
    while True: # 万 恶 之 源 （但反正是在学校里用的……优化？管他呢！）
        time.sleep(1)
        Rundll32Block = str(KVTI_options.ReadKVTIFiles("Settings.kvti","BlockRundll32"))
        Autolt3Block = KVTI_options.ReadKVTIFiles("Settings.kvti","BlockAutolt3")
        CMDBlock = KVTI_options.ReadKVTIFiles("Settings.kvti","BlockCMD")
        WscriptBlock = KVTI_options.ReadKVTIFiles("Settings.kvti","BlockWscript")
        AvastSvcBlock = KVTI_options.ReadKVTIFiles("Settings.kvti","BlockAvastSvc")
        Debugger = KVTI_options.ReadKVTIFiles("Settings.kvti","BlockNotepadSvc")
        for proc in psutil.process_iter():
            try:
                #debug用的
                if proc.name() == "Notepad.exe" and Debugger == "True":
                        proc.suspend()
                        if tkinter.messagebox.askyesnocancel("程序关闭确认","你确定要关闭Rundll32.exe吗？"): #询问是否要关闭窗口
                            proc.terminate()
                        proc.resume()
                if proc.name() == "Rundll32.exe" and Rundll32Block == "True":
                        proc.suspend()
                        if tkinter.messagebox.askyesnocancel("程序关闭确认","你确定要关闭Rundll32.exe吗？"): #询问是否要关闭窗口
                            proc.terminate()
                        proc.resume()
                elif proc.name() == "Avastsvc.exe" and AvastSvcBlock == "True":
                    proc.suspend()
                    if tkinter.messagebox.askyesnocancel("程序关闭确认","你确定要关闭Avastsvc.exe吗？"): #询问是否要关闭窗口
                        proc.terminate()
                    proc.resume()
                elif proc.name() == "CMD.exe" and CMDBlock == "True":
                    proc.suspend()
                    if tkinter.messagebox.askyesnocancel("程序关闭确认","你确定要关闭CMD.exe吗？"): #询问是否要关闭窗口
                        proc.terminate()
                    proc.resume()
                elif proc.name() == "Wscript.exe" and WscriptBlock == "True":
                    proc.suspend()
                    if tkinter.messagebox.askyesnocancel("程序关闭确认","你确定要关闭Wscript.exe吗？"): #询问是否要关闭窗口
                        proc.terminate()
                    proc.resume()
                elif proc.name() == "Autolt3.exe" and Autolt3Block == "True":
                    proc.suspend()
                    if tkinter.messagebox.askyesnocancel("程序关闭确认","你确定要关闭Autolt3.exe吗？"): #询问是否要关闭窗口
                        proc.terminate()
                    proc.resume()
                else:
                    pass
            except psutil.NoSuchProcess:
                pass
            except Exception:
                tkinter.messagebox.showinfo(title="错误代码全文", message="%s" % traceback.format_exc())
                print(traceback.format_exc())
if __name__ == "__main__":
    main()