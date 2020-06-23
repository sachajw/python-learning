#pip install pytube3


import pytube
import os
from pytube import Playlist
from moviepy.editor import VideoFileClip

# print(
#       'What do you want?\n'
#       '(1) Download YouTube Videos manually\n'
#       '(2) Download a YouTube Playlist\n'
#       '(3) Download YouTube Videos and Convert Into MP3\n'
#       'I am not responsible for your downloads! Go at your own risk!\n'
#       'Copyright (c) NeuralNine 2019\n')

choice = input("Choice: ")

if choice == '2':
    link = input("Enter the link of the playlist: ")
    playlist = Playlist(link)
    print("Downloading Playlist...")
    playlist.download_all()
    print("DOWNLOAD DONE!")
elif choice == '1' or choice == '3':
    print("Enter the links of the videos (end by entering 'STOP'):")

    links = []
    link = ""

    while link != "STOP":
        link = input()
        links.append(link)

    links.pop()

    for l in links:
        yt = pytube.YouTube(l)
        stream = yt.streams.get_by_itag(18)
        print("Downloading: ", stream.default_filename)
        stream.download()
        print("DOWNLOAD DONE!")
        if choice == '3':
            print("Converting: ", stream.default_filename)
            clip = VideoFileClip(stream.default_filename)
            clip.audio.write_audiofile(stream.default_filename[:-4] + ".mp3")
            print("CONVERSION DONE!")
            clip.close()
            os.remove(stream.default_filename)
else:
    print("Invalid Input")
