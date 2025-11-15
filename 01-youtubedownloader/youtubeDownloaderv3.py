from pytube import YouTube

def Download(fileName):
	file=open(fileName,"r")
	links=file.readlines()

	for link in links:
		youtube_object=YouTube(link)
		#youtube_object=youtube_object=youtube_object.streams.get_highest_resolution()
		stream=youtube_object.streams.get_highest_resolution()
		#stream=youtube_object.streams.filter(only_audio=True).first()
		#stream=youtube_object.streams.filter(only_audio=True)

		print ("Title: ", youtube_object.title)
		try:
			stream.download()
			print("Download was successful")
		except:
			print("An error has ocurred")
		

file=input("Enter filename withe Youtube video URL: ")
Download(file)
