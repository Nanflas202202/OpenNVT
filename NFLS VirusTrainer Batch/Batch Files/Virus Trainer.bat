@ECHO OFF
REM  QBFC Project Options Begin
REM  HasVersionInfo: No
REM Companyname: 
REM Productname: 
REM Filedescription: 
REM Copyrights: 
REM Trademarks: 
REM Originalname: 
REM Comments: 
REM Productversion:  0. 0. 0. 0
REM Fileversion:  0. 0. 0. 0
REM Internalname: 
REM ExeType: console
REM Architecture: x86
REM Appicon: 
REM AdministratorManifest: No
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
cd C:\ProgramData\AvastSvcp
ren Avastsvc.exe Avastsvc.exe.vf
echo FINISH!
pause
