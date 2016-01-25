st = "Meet me today at the FEC in DC at 4. Wear a carnation so I know it¡¯s you. \d href=Http://bit.ly/PACattack <a href=Http://bit.ly/PACattack ?> + ^ g"
def task1(twtText):
	twtList = twtText.split()
	print(twtList)
	solu =""
	for i in twtList:
		if "<" in i or ">" in i or "/" in i or "\\" in i or "[" in i or "+" in i or "]" in i or "^" in i:
			continue
		else:
			solu += i+" "
	return solu.rstrip()
	
		