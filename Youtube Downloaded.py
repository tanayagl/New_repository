import os
import subprocess

file = open("Hindi Songs.txt")
temp = file.readlines()
lines = temp[0].split("\r")


for line in lines[1:]:
	# try:
	name = line.split("\t")[0]
	artist = line.split("\t")[1]
	print name, artist
	command = 'youtube-dl --output "'+name+' - '+artist+'.%(ext)s" --extract-audio --audio-format mp3 --audio-quality 0 '+'"ytsearch1:'+name+' '+artist+'\"'
	print command
	os.system(command)
	# except Exception as e:
	# 	raise e
# youtube-dl --extract-audio --audio-format mp3 --audio-quality 0 "ytsearch1"+name+" "+""
#!/bin/bash
# YOUTUBEDLAUDIO='youtube-dl --output "%(title)s.%(ext)s" --extract-audio --audio-format mp3 --audio-quality 0'
# while IFS='' read -r line || [[ -n "$line" ]] && [[ ! -z "$line" ]]; do
#   $YOUTUBEDLAUDIO "gvsearch1:$line"
# done < "$1"
