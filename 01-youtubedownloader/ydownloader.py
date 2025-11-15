from pytube import YouTube

def Download(link):
	youtube_object=YouTube(link)
	youtube_object=youtube_object=youtube_object.streams.get_highest_resolution()

	print ("Title: ", youtube_object.title)
	try:
		youtube_object.download()
	except:
		print("An error has ocurred")
	
	print("Download was successful")

link=input("Enter the Youtube video URL: ")
Download(link)
