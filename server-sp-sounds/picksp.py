import pickle
import glob
import requests
from zipfile import ZipFile
from tqdm import tqdm
import os
import pprint
'''
pickleme = {}
pickleme[0] = {}
pickleme[0]["files"] = []
pickleme[0]["url"] = "https://github.com/plowsof/sof1maps/raw/main/server-sp-sounds/sp1.zip"
for x in glob.glob("*"):
	if x[-3:] != ".py":
		pickleme[0]["files"].append(x)

with open("sp-sound-list", 'wb+') as f:
	pickle.dump(pickleme,f)
'''
pickled_sp_sounds = "https://github.com/plowsof/sof1maps/raw/main/server-sp-sounds/sp-sound-list"

new_zip_link = "https://github.com/plowsof/sof1maps/raw/main/server-sp-sounds/sp2.zip"

sp_sounds = {}


def download_sp_sounds(url: str, fname: str):
	resp = requests.get(url, stream=True)
	fdesc = "sp-sound-list"
	if resp.status_code != 404:
		total = int(resp.headers.get('content-length', 0))
		with open(fname, 'wb') as file, tqdm(
			desc=fdesc,
			total=total,
			unit='iB',
			unit_scale=True,
			unit_divisor=1024,
		) as bar:
			for data in resp.iter_content(chunk_size=1024):
				size = file.write(data)
				bar.update(size)
		return True
	else:
		return False

def check_sp_sounds():
	global pickled_sp_sounds
	if download_sp_sounds(pickled_sp_sounds,"http_pickled_sounds"):
		with open("http_pickled_sounds", 'rb') as f:
			sp_sounds = pickle.load(f)
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(sp_sounds)
	for x in sp_sounds:
		for y in sp_sounds[x]["files"]:
			sfile = os.path.join("user","sound","sp",y)
			if not os.path.isfile(sfile):
				print(f"not a file:{sfile}")
				if download_sp_sounds(sp_sounds[x]["url"],"sp_sounds.zip"):
					with ZipFile('sp_sounds.zip', 'r') as zipObj:
						# Extract all the contents of zip file in different directory
						zipObj.extractall('user')
					break

def add_new_sounds():
	global new_zip_link
	global sp_sounds
	#get online pickled list (we'll be appending to it, then saving the new list)
	if download_sp_sounds(pickled_sp_sounds,"http_pickled_sounds"):
		with open("http_pickled_sounds", 'rb') as f:
			sp_sounds = pickle.load(f)
	#we have zipped the sounds, and know the url for the zip already
	new_sp_sounds = {}
	new_sp_sounds = {}
	new_sp_sounds["files"] = []
	new_sp_sounds["url"] = new_zip_link
	for x in glob.glob("*"):
		if x[-3:] == "wav":
			new_sp_sounds["files"].append(x)
	print(len(sp_sounds))
	append_new = len(sp_sounds)
	sp_sounds[append_new] = new_sp_sounds

	with open("sp-sound-list-Git", 'wb+') as f:
		pickle.dump(sp_sounds,f)
	pp = pprint.PrettyPrinter(indent=4)
	pp.pprint(sp_sounds)

#add_new_sounds()
check_sp_sounds()

