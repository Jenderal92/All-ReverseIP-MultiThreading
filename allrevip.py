#All Reverse MultiThread Unlimited 
#!/usr/bin/python
# -*- coding: utf-8 -*
#JametKNTLS - h0d3_g4n - Moslem - Jenderal92 -Kiddenta
# Blog : https://www.blog-gan.org          
#DONATE ME :(
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614
##############################
#####################################
import requests, re, urllib2, os, sys, codecs, random				
from multiprocessing.dummy import Pool					     	
from time import time as timer	
import time
import socket
import json				   		
from platform import system	
from random import sample
from colorama import Fore								
from colorama import Style								
from pprint import pprint								
from colorama import init
from urlparse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
reload(sys)  
sys.setdefaultencoding('utf8')
init(autoreset=True)
##########################################################################################
##########################################################################################
abang = '\033[31m'
ijo = '\033[32m'
kuning = '\033[33m'
birtu = '\033[34m'
ungu = '\033[35m'
biru = '\033[36m'
abu = '\033[37m'
putih = '\033[0m' 
year = time.strftime("%y")
month = time.strftime("%m")
#####################################
##########################################################################################

def logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
          \033[31m\   \033[31m/
   \033[34m----- (9\033[31m"-_-\033[34m)9  \033[37mVs  \033[34m6(\033[31mx_x"\033[34m6) -----
   
   \033[32m>--------------------------------<
   - Jamet Crew aka KNTL Megalodon - 
      - All Reverse IP - Jenderal92 -
   
   
   \033[41m\033[1;33m[Blog : https://www.blog-gan.org\033[0m
   \033[41m\033[1;33m[Online Tools : http://secpriv8.com\033[0m
   \033[41m\033[1;33m[ICQ : https://icq.im/Shin403\033[0m
   \033[32m>----------------------------------<
   [-] 1. Api From threatcrowd.org
   [-] 2. Api From reverse-ip.org
   [-] 3. Api From networksdb.io with (Apikey)
   [-] 4. Api From tools.helixs.id
   [-] 5. Api From ipinfo.io with (Apikey)
   [-] 6. Api From soulapizy.000webhostapp.com
   [-] 7. Api From api.viewdns.info with (Apikey)
   [-] 8. Api From sonar.omnisint.io
   [-] 9. Api From tools.webservertalk.com
   [-] 10. Api From osint.sh
   [-] 11. COOMING SOON !!! 'if this tools Error U Can Contact Me'

   \033[32m>---------------------------------<  
   
"""
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)


logo()

pilihmas = raw_input(':~# \033[34mChoose\033[32m Number : ')

########JANCOKSURAIMU####


def revsip1(url):
	try:
		grab = requests.get('https://www.threatcrowd.org/searchApi/v2/ip/report/?ip='+url, timeout=10,headers={'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}).text
		if 'response_code' in grab:
			res = re.findall('"domain":"(.*?)"',grab)
			for rr in res:
				resk = rr.replace('cpanel.','').replace('cpcalendars.','').replace('cpcontacts.','').replace('webmail.','').replace('webdisk.','').replace('hostmaster.','').replace('mail.','').replace('ns1.','').replace('ns2.','')
				print(kuning+'[+]' + str(resk) + ijo +' '+  '>' +'OK')
				open('Results_domain.txt', 'a').write('http://'+resk+'\n')
			else:
				print(kuning+"[+]" + str(url) + abang + " " + ">" +" error can't reslove domain")
				
	except:
		pass

def revsip2(url):
	try:
		state = ['us1', 'us2', 'us3', 'us4', 'us5', 'us6', 'us7', 'us8', 'us9', 'us10', 'us11', 'us12', 'us13', 'us14', 'us15', 'eu1', 'eu2', 'eu3', 'eu4', 'eu5', 'eu6', 'eu7', 'eu8', 'eu9', 'eu10']
		proxy = random.choice(state)
		ua = {'Origin': 'https://' + proxy + '.proxysite.com',
		'Upgrade-Insecure-Requests': '1',
		'Referer': 'https://' + proxy + '.proxysite.com/process.php?d=R504l92agDy3wRhPu4IesGEo67D4t5AA%2BitKoPp6K8HVxDzLtUqvsNt8zXdca6jbbHveLLWHUAtv9Xc34YubFXyjhOn6rJcYr1e3cacdpvrVkIRG&b=1&f=norefer',
		'Content-Type': 'application/x-www-form-urlencoded',
		'User-Agent': 'Mozilla/5.0 (Linux; Android 11; Redmi Note 9 Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/87.0.4280.141 Mobile Safari/537.36',
		'Cookies': '_ga=GA1.2.589987225.1610038351; __gads=ID=bffe8a3c85dbe9de-228786b28fc5007f:T=1610038351:RT=1610038351:S=ALNI_Mbo8XuMGTbG0cfECZhdrpKMLkcBLA; __ssid=36d6510dd2039cb1842ad209a230178; c[doubleclick.net][/][IDE]=AHWqTUn08p1P3g_WBOyIDUI3USSsOCdzShvtgIaVlejsV6DBIwLhPQha2Sg9XKGREjs; c[email-checker.net][/][rack%2Esession]=BAh7B0kiD3Nlc3Npb25faWQGOgZFVG86HVJhY2s6OlNlc3Npb246OlNlc3Npb25JZAY6D0BwdWJsaWNfaWRJIkU0NGNhYzkyMWRmYTUyZTgxYTk5OWRhMzBiYzFkNTJiNjZjN2JmMGMyMzQzYjMyMjczYjU0YTY3MDBkNDkwY2MwBjsARkkiD2NzcmYudG9rZW4GOwBUSSIweDRQVU1YdWItaHNhdTJNY0VHTEZhejl4TkFEai1QYjZIQnpuTXpaalZVcwY7AEY%253D--03ae8f32969ba86bdc2e0704b80075b16c10ccc6; _gid=GA1.2.1830710139.1632497290; _gat=1; PHPSESSID=bo3lh3ojv4hbb74nlrgd6lvpe5'
		}
		data = {'d': 'https://reverse-ip.org/wp-content/plugins/wp-iplookup/ajax/get.php?request='+url,
		'allowCookies': 'on'
		}
		test = requests.post('https://' + proxy + '.proxysite.com/includes/process.php?action=update', data=data, headers=ua, timeout=10).content
		if '{' in test:
			hehe = re.findall('":"(.*?)"' ,test)
			for xixi in hehe:
				print(ijo+' Hasile : '+kuning+' http://'+str(xixi))
				open('Results_domain.txt', 'a').write('http://'+str(xixi)+'\n')
			else:
				print(abang+' Dah Abis Jink :v ')
	except:
		pass

def revsip3(url):
	try:
		head = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
		'X-Api-Key': 'e9aae243-e603-40fc-804d-4aa9db64408c'}
		grab = requests.post('https://networksdb.io/api/reverse-dns', data={'ip': url}, headers=head, timeout=10).json()
		for resnya in grab['results']:
			print(kuning+'[+]' + str(resnya) + ijo +' '+  '>' +'OK')
			open('Results_domain.txt', 'a').write('http://'+resnya+'\n')
		else:
			print(kuning+"[+]" + str(url) + abang + " " + ">" +" BAD")
	except:
		pass

def revsip4(url):
	try:
		head = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}
		grab = requests.get('https://tools.helixs.id//API/revip.php?ip='+url, headers=head, timeout=10).json()
		for cc in grab["result"]:
			print(kuning+'[+]' + str(cc) + ijo +' '+  '>' +'OK')
			open('Results_domain.txt', 'a').write('http://'+cc+ '\n' )
		else:
			print(kuning+"[+]" + str(url) + abang + " " + ">" +" BAD")
	except:
		pass

def revsip5(url):
	try:
		res = requests.get("https://ipinfo.io/domains/"+url+"?token=000ea8e44a08af", timeout=10,headers={'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}).json()
		for ceks in res["domains"]:
			print(len(str(res["total"])+biru+' Total Found' +url))
			print(ceks+ijo+' > Result Dari '+url)
			open('Results_domain.txt', 'a').write('http://'+ceks+'\n')
		else:
			print(abang+'Error !!!')
	except:
		pass

def revsip6(url):
	try:
		grab = requests.get('https://soulapizy.000webhostapp.com/zerorev/?ip='+url).content
		if 'null' in grab:
			print(kuning+'[+]' + str(url) + ijo +' '+  '>' +'OK')
		else:
			print(kuning+"[+]" + str(url) + abang + " " + ">" +" BAD"),len(grab)
			open('Results_domain.txt', 'a').write(grab+'\n')
	except:
		pass

def revsip7(url):
    try:
        yo = requests.get("https://api.viewdns.info/reverseip/?host="+ url +"&apikey="+ Apikey +"&output=json", timeout=10,headers={'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'})
        domen = json.loads(yo.text)
        for jancok in domen["response"]["domain_count"]:
            print(jancok["name"]+ ijo + '[!] View Dns . . .')
            open('Results_domain.txt', 'a').write('http://'+jancok["name"] + '\n')
    except:
        pass

def revsip8(url):
	try:
		grab = requests.get('https://sonar.omnisint.io/reverse/'+url, timeout=10,headers={'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'})
		if 'null' in grab.text:
			print(kuning+'[+]' + url + abang + '>' +'Failed')
		else:
			result = json.loads(grab.text)
			print(kuning+'[+]' + birtu+'IP :'+' ' +ijo + str(url) +' '+'Total Domain =>' ), len(result)
			for domain in result: 
				ASU = domain.replace('cpanel.','').replace('cpcalendars.','').replace('cpcontacts.','').replace('webmail.','').replace('webdisk.','').replace('hostmaster.','').replace('mail.','').replace('ns1.','').replace('ns2.','')
				open('Results_domain.txt', 'a').write('http://' + ASU + "\n")
	except:
			pass

def revsip9(url):
	try:
		grab = requests.get('https://tools.webservertalk.com/?tool=reverseip&host='+url).content
		if 'Domain/IP:' in grab:
			regx = reg('<td class="text-left">(.*?)<', grab)
			for ckk in regx:
				mek = ckk.replace("Domain","")
				print(kuning+'[+]' + str(mek) + ijo +' '+  '>' +'OK')
				open('Results_domain.txt', 'a').write('http://'+mek+'\n')
			else:
				print(kuning+"[+]" + str(url) + abang + " " + ">" +" BAD")
	except:
		pass

def revsip10(url):
	try:
		head = {'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36'}
		ress = requests.post("https://osint.sh/reverseip/",data={"domain": url } ,timeout=10,headers=head).text
		if 'Domain' in ress:
			ajg = re.findall('<td data-th="Domain">\n(.*?)<',ress)
			for asu in ajg:
				mek = asu.replace(" ","")
				print(mek + ijo + ' [!] LAGI GRAB SLUR . . .')
				open('Results_domain.txt', 'a').write('http://'+mek+'\n')
			else:
				print(abang+'ERROR!!!')
	except:
		pass

######MENGONTOL#####
def Main():
	try:
		if pilihmas =='1':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev1 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(revsip1, rev1)
		if pilihmas =='2':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev2 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(revsip2, rev2)
		if pilihmas =='3':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev3 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(revsip3, rev3)
		if pilihmas =='4':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev4 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(revsip4, rev4)
		if pilihmas =='5':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev5 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(revsip5, rev5)
		if pilihmas =='6':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev6 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(revsip6, rev6)
		if pilihmas =='7':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev7 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(revsip7, rev7)
		if pilihmas =='8':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev8 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(revsip8, rev8)
		if pilihmas =='9':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev9 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(revsip9, rev9)
		if pilihmas =='10':
			list = raw_input("\n\033[91mGive Me List \033[97m:~# \033[97m")
			crownes = raw_input("\033[91mthread \033[97m\033[97m:~# \033[97m")
			rev10 = open(list, 'r').read().splitlines()
			pp = Pool(int(crownes))
			pr = pp.map(revsip10, rev10)
		
		
	except:
		pass

if __name__ == '__main__':
	Main()