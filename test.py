#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from moviepy.editor import VideoFileClip
from time import sleep
from apify_client import ApifyClient

import os, ffmpeg

def compress_video(video_full_path, output_file_name, target_size):
    # Reference: https://en.wikipedia.org/wiki/Bit_rate#Encoding_bit_rate
    min_audio_bitrate = 32000
    max_audio_bitrate = 256000

    probe = ffmpeg.probe(video_full_path)
    # Video duration, in s.
    duration = float(probe['format']['duration'])
    # Audio bitrate, in bps.
    audio_bitrate = float(next((s for s in probe['streams'] if s['codec_type'] == 'audio'), None)['bit_rate'])
    # Target total bitrate, in bps.
    target_total_bitrate = (target_size * 1024 * 8) / (1.073741824 * duration)

    # Target audio bitrate, in bps
    if 10 * audio_bitrate > target_total_bitrate:
        audio_bitrate = target_total_bitrate / 10
        if audio_bitrate < min_audio_bitrate < target_total_bitrate:
            audio_bitrate = min_audio_bitrate
        elif audio_bitrate > max_audio_bitrate:
            audio_bitrate = max_audio_bitrate
    # Target video bitrate, in bps.
    video_bitrate = target_total_bitrate - audio_bitrate

    i = ffmpeg.input(video_full_path)
    ffmpeg.output(i, os.devnull,
                  **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 1, 'f': 'mp4'}
                  ).overwrite_output().run()
    ffmpeg.output(i, output_file_name,
                  **{'c:v': 'libx264', 'b:v': video_bitrate, 'pass': 2, 'c:a': 'aac', 'b:a': audio_bitrate}
                  ).overwrite_output().run()

if __name__ == "__main__":

    # compress_video('4176.312.mp4', 'output.mp4', 50 * 1000)

    # Initialize the ApifyClient with your API token
    client = ApifyClient("apify_api_5GYrjsJrvSEpSZxmaQx2bqoSMRRyg74sHobe")

    # Prepare the actor input
    run_input = { "outputFormat": "mp4" }

    # Run the actor and wait for it to finish
    run = client.actor("lukaskrivka/audio-video-converter").call(run_input=run_input)

    # Fetch and print actor results from the run's dataset (if there are any)
    for item in client.dataset(run["defaultDatasetId"]).iterate_items():
        print(item)

    

    # full_video = "./itest.mp4"
    # current_duration = VideoFileClip(full_video).duration
    # divide_into_count = 5
    # single_duration = current_duration/divide_into_count
    # current_video = f"{current_duration}.mp4"

    # while current_duration > single_duration:
    #     clip = VideoFileClip(full_video).subclip(current_duration-single_duration, current_duration)
    #     current_duration -= single_duration
    #     current_video = f"{current_duration}.mp4"
    #     clip.to_videofile(current_video, codec="libx264", temp_audiofile='temp-audio.m4a', remove_temp=True, audio_codec='aac')

    #     print("-----------------###-----------------")
