@ECHO OFF
REM  QBFC Project Options Begin
REM HasVersionInfo: Yes
REM Companyname: NFLS 202202
REM Productname: VirtsTrainer Alpha 3 SP1
REM Filedescription: ����д�ļ�����
REM Copyrights: û��
REM Trademarks: Ҳû��
REM Originalname: ���
REM Comments: Ҳ������д
REM Productversion:  0. 0. 0. 1
REM Fileversion:  0. 0. 0. 3
REM Internalname: VTA3.1 build20221026
REM ExeType: console
REM Architecture: x64
REM Appicon: ֣һ�� �����Ŀs\sdrj\Icon6.ico
REM AdministratorManifest: Yes
REM  QBFC Project Options End
@ECHO ON
echo off
cls
color 02
title NFLS Virus Trainer
echo Welcome to Virus Trainer Insider Preview!
echo Killing Viruses...
taskkill -f -im Rundll32.exe -t
taskkill -f -im Avastsvc.exe -t
taskkill -f -im Autolt3.exe -t
taskkill -f -im wscript.exe -t
taskkill -f -im cmd.exe -t
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
ren E:\RECYCLER.BIN ����վ
ren F:\RECYCLER.BIN ����վ
ren G:\RECYCLER.BIN ����վ
ren H:\RECYCLER.BIN ����վ
ren I:\RECYCLER.BIN ����վ
ren J:\RECYCLER.BIN ����վ
ren K:\RECYCLER.BIN ����վ
ren E:\Skypee\*.lnk *.vir
ren F:\Skypee\*.lnk *.vir
ren G:\Skypee\*.lnk *.vir
ren H:\Skypee\*.lnk *.vir
ren I:\Skypee\*.lnk *.vir
ren J:\Skypee\*.lnk *.vir
ren K:\Skypee\*.lnk *.vir
echo Disabling Autorun
cd "C:\ProgramData\AvastSvcpCP"
ren "C:\ProgramData\AvastSvcpCP\Avastsvc.exe" Avastsvc.exe.vf
ren "C:\ProgramData\AvastSvcpCP\Avastsvc.dat" Avastsvc.dat.vf
ren "C:\ProgramData\AvastSvcpCP\wsc.dll" wsc.dll.vf
ren "C:\Users\Administrator\AppData\Roaming\Microsoft\Office\rundll32.exe" Rundll32.dll.vf
ren C:\Google\Autolt3.exe Autolt3.exe.Scriptrunner
echo FINISH!
pause
taskkill -f -im console.exe -t
