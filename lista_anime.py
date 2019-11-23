import os

os.chdir("Anime")

for anime in os.listdir():
	os.chdir(anime)
	for cap in os.listdir():
		print(cap.split(".")[0][-2:])
	os.chdir("..")
