from pytube import YouTube
from sys import argv

def Download(link):
	yt = YouTube(link)
	yd=yt.streams.get_highest_resolution()

	print("Title: ", yt.title)

	try:
		yd.download("/home/diablo/Downloads/youtubeVideos/")

	except:
		print("An error has ocurred while downloading.")

	print("Download was successful. File was downloaded in Downloads/youtubeVideos.")
	

link = argv[1]
Download(link)


#yd.download()
