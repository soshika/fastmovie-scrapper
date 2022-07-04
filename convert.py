import os
import wget
import siaskynet as skynet

if __name__ == "__main__":

    url = 'http://siasky.net/GAARGZ0tTTSjf0bFwtFcIJlmuWSGdBAaccyLbNQZ7M-zbw'
    name = wget.download(url)
    print('file {0} downloaded successfully'.format(name))

    os.system('ffmpeg -i {0} -vcodec libx264 -f mp4 test.mp4'.format(name))

    directory = os.getcwd()
    file_path = directory + '/test.mp4' 

    client = skynet.SkynetClient() 
    skylink = client.upload_file(file_path)
    print("File Uploaded successfully: link is {0} ".format( skylink))