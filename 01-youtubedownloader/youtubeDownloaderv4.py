from pytube import YouTube
import os
import time
import re


def Download(fileName):
	file=open(fileName,"r")
	links=file.readlines()

	os.system("mkdir audios")

	for link in links:
		youtube_object=YouTube(link)
		stream=youtube_object.streams.get_highest_resolution()

		print ("Title: ", youtube_object.title)
		try:
			stream.download()
			print("Download was successful")
		except:
			print("An error has ocurred")


def  convert():
	print("Converting to mp3 file....")
	time.sleep(1)
	videos=os.listdir(".")
	#print(videos)
	r=re.compile(".*mp4$")
	videos=list(filter(r.match, videos))
	#print(videos)
	for video in videos:
		#cmd=f'echo {video}'
		audio_name=video[:-3]+"mp3"
		#print(audio_name)
		cmd=f'ffmpeg -i "{video}" -b:a 128k -acodec libmp3lame -ar 44100 audios/"{audio_name}"'
		#print(cmd)
		os.system(cmd)
		cmd2=f"rm -rf '{video}'"
		#print(cmd2)
		time.sleep(2)
		os.system(cmd2)
		

file=input("Enter filename withe Youtube video URL: ")
Download(file)

time.sleep(1)
convert()
