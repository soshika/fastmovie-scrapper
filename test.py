#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from moviepy.editor import VideoFileClip
from time import sleep

if __name__ == "__main__":
    full_video = "./itest.mp4"
    current_duration = VideoFileClip(full_video).duration
    divide_into_count = 5
    single_duration = current_duration/divide_into_count
    current_video = f"{current_duration}.mp4"

    while current_duration > single_duration:
        clip = VideoFileClip(full_video).subclip(current_duration-single_duration, current_duration)
        current_duration -= single_duration
        current_video = f"{current_duration}.mp4"
        clip.to_videofile(current_video, codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')

        print("-----------------###-----------------")
