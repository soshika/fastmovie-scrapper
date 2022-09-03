#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from moviepy.editor import *
import wget
import siaskynet as skynet

if __name__ == "__main__":

    output = 'otest.mp4'
    file_name = wget.download("https://siasky.net/GADohxbY-BLhLJ0CIb3jo7yW3CynCtGfKfkQJnPSw9NuYA")
    
    
    clip = VideoFileClip(file_name)
    clip.write_videofile(output, fps=30)

     # get current directory
    directory = os.getcwd()
    file_path = directory + '/' + output

    # link to skynet
    client = skynet.SkynetClient() 
    skylink = client.upload_file(file_path)
    print("File {0} Uploaded successfully: link is {1} ".format(file_name, skylink))

