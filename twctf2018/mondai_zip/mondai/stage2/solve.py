import zipfile

z = zipfile.ZipFile("mondai.zip")
for p in open("list.txt"):
	try:
		z.open("1c9ed78bab3f2d33140cbce7ea223894", pwd=p[:-1]).read()
		print p[:-1]
	except:
		pass
# eVjbtTpvkU
