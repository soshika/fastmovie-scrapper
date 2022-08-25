import os
import wget
import ffmpeg
import siaskynet as skynet

def convert_to_mp4(mkv_file):
    name, ext = os.path.splitext(mkv_file)
    out_name = name + ".mp4"
    os.system('ffmpeg -i {0} -vcodec libx264 -f mp4 {1}'.format(mkv_file, out_name))
    print("Finished converting {}".format(mkv_file))
    return out_name

if __name__ == "__main__":

    url = 'https://eu.cdn.cloudam.cc/download/2/4/825041/5986/12157/46.105.134.229/1661592553/307c8b2e76af92b10cc4b18756ffec0ea4f317c128/series/friends/Friends_S01E01_720p_BluRa>
    name = wget.download(url)

    mp4_file_name = convert_to_mp4(name)

    directory = os.getcwd()
    file_path = directory + '/' + mp4_file_name

    client = skynet.SkynetClient() 
    skylink = client.upload_file(file_path)
    print("File Uploaded successfully: link is {0} ".format( skylink))

    os.remove(file_path)
    print('File {0} deleted'.format(file_path))