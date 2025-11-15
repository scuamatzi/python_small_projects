#/bin/bash
#This script converts a video to an mp3 file.

#Make the directory if it doesn't exist.
if [ ! -d "audios" ]; then
	mkdir "audios";
fi

IFSORIGINAL=$IFS
IFS=$(echo -en "\n\b")

#extension=$1
extension="mp4"

for i in `ls *$extension`
do
	nombre_original="$i"
	nombre_sin_extension="$(basename $i .$extension)"
	#echo ""
	#echo "iniciando proceso sobre el archivo $nombre_original"
	#echo ""
	# THIS IS FOR THE CREATION OF THE MP3 FILE
	nombre_nuevo="$nombre_sin_extension.mp3"
	sleep 1
	
	#THIS COMMAND MAKE AN MP3 FILE FROM THE VIDEO GIVEN
	#avconv -i "$nombre_original" -b:a 128k -acodec libmp3lame -ar 44100 videos/"$nombre_nuevo"
	ffmpeg -i "$nombre_original" -b:a 128k -acodec libmp3lame -ar 44100 audios/"$nombre_nuevo"
	# !!!!DON'T FORGET TO CHANGE THE EXTENSION IN THE CORRECT LINE AT THE BEGINING OF THE SCRIPT!!!!

	#echo ""
	#echo "archivo $nombre_original terminado..."
	#echo ""
	sleep 1
done

IFS=$IFSORIGINAL
