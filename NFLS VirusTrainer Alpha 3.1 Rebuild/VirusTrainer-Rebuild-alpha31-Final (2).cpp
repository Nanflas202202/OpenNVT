#include<windows.h>
#include<bits/stdc++.h>
using namespace std;
int main(){
	cout<<"-----------------------------------------------------------------"<<endl;
	cout<<"|                   Welcome To Virus Trainer                    |"<<endl;
	cout<<"|                 Version Alpha 3.1 SP1 Rebuild                 |"<<endl;
	cout<<"|                     Build 202211081107                        |"<<endl;
	cout<<"-----------------------------------------------------------------"<<endl;
	system("title New NFLS Virus Trainer Alpha 3.1");
	system("Color 02");
	while(true){
		cout<<"#1 Kill Viruses"<<endl;
		cout<<"#2 Fix What Viruses Make"<<endl;
		cout<<"#3 Auto Kill(Do #1 And #2)"<<endl;
		cout<<"#4 Select What Virus You Want To Kill"<<endl;
		cout<<"#5 Quit"<<endl;
		int CommandVar;
		cin>>CommandVar;
		switch(CommandVar){
			#include<windows.h>
			case 1: cout<<"----------------Killing Viruses----------------"<<endl;
				cout<<"---------------Killing Processes---------------"<<endl;
				std::system("TASKKILL -F -IM Rundll32.exe -T");
			    std::system("TASKKILL -F -IM AvastSvc.exe -T");
				std::system("TASKKILL -F -IM wscript.exe -T");
				std::system("TASKKILL -F -IM Autolt3.exe -T");
				std::system("TASKKILL -F -IM cmd.exe -T");
				cout<<"----------------------FINISH-------------------"<<endl;
				cout<<"-------------Showing Hidden Files--------------"<<endl;
		    	std::system("ATTRIB -S -H E:\ /d /l");
				std::system("ATTRIB -S -H F:\ /d /l");
				std::system("ATTRIB -S -H G:\ /d /l");	
				std::system("ATTRIB -S -H I:\ /d /l");
				std::system("ATTRIB -S -H J:\ /d /l");
				std::system("ATTRIB -S -H K:\ /d /l");
				cout<<"----------------------FINSIH-------------------"<<endl;
				std::system("ren E:\*.lnk *.vir");
				std::system("ren F:\*.lnk *.vir");
				std::system("ren G:\*.lnk *.vir");
				std::system("ren H:\*.lnk *.vir");
				std::system("ren I:\*.lnk *.vir");
				std::system("ren J:\*.lnk *.vir");
				std::system("ren K:\*.lnk *.vir");
				std::system("ren E:\RECYCLER.BIN VirusMainFiles");
				std::system("ren F:\RECYCLER.BIN VirusMainFiles");
				std::system("ren G:\RECYCLER.BIN VirusMainFiles");
				std::system("ren H:\RECYCLER.BIN VirusMainFiles");
				std::system("ren I:\RECYCLER.BIN VirusMainFiles");
				std::system("ren J:\RECYCLER.BIN VirusMainFiles");
				std::system("ren K:\RECYCLER.BIN VirusMainFiles");
				std::system("echo Disabling Autorun");
				std::system("cd "C:\ProgramData\AvastSvcpCP");
				std::system("ren "C:\ProgramData\AvastSvcpCP\Avastsvc.exe" Avastsvc.exe.vf");
				std::system("ren "C:\ProgramData\AvastSvcpCP\Avastsvc.dat" Avastsvc.dat.vf");
				std::system("ren "C:\ProgramData\AvastSvcpCP\wsc.dll" wsc.dll.vf");
				std::system("ren ");
				std::system("");
				cout<<"----------------------FINSIH-------------------"<<endl;
			case 2: cout<<"-------------Showing Hidden Files--------------"<<endl;
				system("ATTRIB -S -H E:\ /d /l");
				system("ATTRIB -S -H F:\ /d /l");
				system("ATTRIB -S -H G:\ /d /l");	
				system("ATTRIB -S -H I:\ /d /l");
				system("ATTRIB -S -H J:\ /d /l");
				system("ATTRIB -S -H K:\ /d /l");
				  cout<<"----------------------FINSIH-------------------"<<endl;
			case 3:cout<<"-------------Showing Hidden Files--------------"<<endl;
			system("ATTRIB -S -H E:\ /d /l");
			system("ATTRIB -S -H F:\ /d /l");
			system("ATTRIB -S -H G:\ /d /l");	
			system("ATTRIB -S -H I:\ /d /l");
			system("ATTRIB -S -H J:\ /d /l");
			system("ATTRIB -S -H K:\ /d /l");
			cout<<"----------------------FINSIH-------------------"<<endl;
			case 4:
				cout<<"Develping,Please choose another one ;-)"<<endl;
			case 5:
				cout<<"----------------------FINSIH-------------------"<<endl;
				cout<<"Press <Enter> to continue..."<<endl;
				getchar();
				return 0;
			default:cout<<"Command Not Found!"<<endl;
		}
	}
}
