from pytube import YouTube

yt=YouTube("https://www.youtube.com/watch?v=Pt3TRLHgh84")

print(yt.title)

streamfile=yt.streams.filter(file_extension='mp4')