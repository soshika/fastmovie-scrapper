#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from moviepy.editor import *
import wget

if __name__ == "__main__":

    file_name = wget.download("https://siasky.net/GADohxbY-BLhLJ0CIb3jo7yW3CynCtGfKfkQJnPSw9NuYA")
    
    
    clip = VideoFileClip(file_name)
    clip.write_videofile('./otest.mp4', fps=30)