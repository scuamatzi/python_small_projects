import os
import subprocess

def convert_video_to_mp3(input_filename, output_filename):
    ffmpeg_cmd=[
        "ffmpeg",
        "-i", input_filename,
        "-b:a", "128k",
        "-acodec", "libmp3lame",
        "-ar", "44100",
        output_filename
    ]

    try:
        subprocess.run(ffmpeg_cmd,check=True)
        print("Succesfully converted.")
    except subprocess.CalledProcessError as e:
        print("Conversion Failed")

extension=input("Write extension of video: ")
videos_list=[]
for filename in os.listdir("."):
    if filename.endswith(extension):
        videos_list.append(filename)

if not videos_list:
    print(f"No videos found with extension {extension}")
else:
    audios_list=[x.replace("mp4","mp3") for x in videos_list]

    for i, video in enumerate(videos_list):
        convert_video_to_mp3(video,audios_list[i])
