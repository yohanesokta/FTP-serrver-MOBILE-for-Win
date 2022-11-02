import subprocess
import os
os.system('cls')
os.system('title = FTP SERVER-Hanzsoft Creative')

print("\nPROGRAM FTP SERVER\n")
print("======================")
print("=    Make : YhanzC   =")
print("======================")
print("=  Default : 192.168 =")
print("=  Port    : 2221    =")
print("======================")
print("\n")
ip = str(input("Masukan IP Ke 3 dan 4: "))
G_ip = str("ftp://192.168." + ip + ":2221" )
subprocess.run(["explorer.exe",G_ip])
print("\n")
print("Coba run atau di cmd jika tidak berhasil")
print(G_ip)
print("======================")
os.system("pause")

