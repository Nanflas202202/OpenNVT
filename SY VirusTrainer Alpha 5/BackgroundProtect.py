def getChildrenPidsOfPid():
    """Returns the children pids of a pid"""
    newpidcnt = 0
    pid = 0
    wmi = win32com.client.GetObject('winmgmts:')
    for win32_process_instance in wmi.InstancesOf('win32_process'):
            if win32_process_instance.Name and win32_process_instance.Name.upper() == "NotePad.exe".upper():
                pTime = win32_process_instance.Properties_('CreationDate').Value
                processId = int(win32_process_instance.Properties_('ProcessId'))
                if pTime > 1:
                    newpidcnt = newpidcnt + 1
                    pid = processId
    if newpidcnt > 2:
        raise RuntimeError("error")
    print(pid);
    return pid

def kill(pid):
    try:
        # command = 'taskkill /F /IM %d' %pid
        # print type(command)
        # os.system(command) #1111
        import subprocess  
        subprocess.Popen("cmd.exe /k taskkill /F /T /PID %i"%pid , shell=True)  
    except OSError:
        print('no process')
#From https://www.jianshu.com/p/f8a650e7aeb7

def BGPT():
     while True:
            VPID=getChildrenPidsOfPid();
            os.system("Taskkill -f -im",VPID,"-T");
        
if __name__ == "__main__":
     BGPT();
