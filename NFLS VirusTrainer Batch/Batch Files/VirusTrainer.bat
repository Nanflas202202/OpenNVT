echo off
cls
color 02
title NFLS Virus Trainer
echo Welcome to Virus Trainer Insider Preview!
echo Killing Viruses...
taskkill -f -im Rundll32.exe -t
taskkill -f -im Avastsvc.exe -t
echo Showing Hidden Files...
attrib -s -h E:\* /d /l
attrib -s -h F:\* /d /l
attrib -s -h G:\* /d /l
attrib -s -h H:\* /d /l
attrib -s -h I:\* /d /l
attrib -s -h J:\* /d /l
attrib -s -h K:\* /d /l
echo Renaming Virus Files
ren E:\*.lnk *.vir
ren F:\*.lnk *.vir
ren G:\*.lnk *.vir
ren H:\*.lnk *.vir
ren I:\*.lnk *.vir
ren J:\*.lnk *.vir
ren K:\*.lnk *.vir
ren E:\RECYCLER.BIN VirusMainFiles
ren F:\RECYCLER.BIN VirusMainFiles
ren G:\RECYCLER.BIN VirusMainFiles
ren H:\RECYCLER.BIN VirusMainFiles
ren I:\RECYCLER.BIN VirusMainFiles
ren J:\RECYCLER.BIN VirusMainFiles
ren K:\RECYCLER.BIN VirusMainFiles
echo Disabling Autorun
cd "C:\ProgramData\AvastSvcpCP"
ren "C:\ProgramData\AvastSvcpCP\Avastsvc.exe" Avastsvc.exe.vf
ren "C:\ProgramData\AvastSvcpCP\Avastsvc.dat" Avastsvc.dat.vf
ren "C:\ProgramData\AvastSvcpCP\wsc.dll" wsc.dll.vf
ren "C:\Users\Administrator\AppData\Roaming\Microsoft\Office\rundll32.exe" Rundll32.dll.vf
echo FINISH!
pause