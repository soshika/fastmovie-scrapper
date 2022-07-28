import os
import wget
import siaskynet as skynet

if __name__ == "__main__":

    url = 'https://eu.cdn.cloudam.cc/download/2/4/825041/5986/12157/46.105.134.229/1661592553/307c8b2e76af92b10cc4b18756ffec0ea4f317c128/series/friends/Friends_S01E01_720p_BluRay_PaHe_30NAMA.mkv'
    name = wget.download(url)
    print('file {0} downloaded successfully'.format(name))

    os.system('ffmpeg -i {0} -vcodec libx264 -f mp4 test.mp4'.format(name))

    directory = os.getcwd()
    file_path = directory + '/test.mp4'

    # file_path = "/Users/soshika/Desktop/logo.png"

    client = skynet.SkynetClient() 
    skylink = client.upload_file(file_path)
    print("File Uploaded successfully: link is {0} ".format( skylink))