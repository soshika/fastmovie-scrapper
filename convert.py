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

    url = 'https://eu.cdn.cloudam.cc/download/2/4/825041/5986/12157/212.103.48.92/1664025491/30d1648027a3160e2411cdf04d7749f450fd666f0c/series/friends/Friends_S01E01_720p_BluRay_PaHe_30NAMA.mkv'
    name = wget.download(url)

    mp4_file_name = convert_to_mp4(name)

    directory = os.getcwd()
    file_path = directory + '/' + mp4_file_name

    client = skynet.SkynetClient() 
    skylink = client.upload_file(file_path)
    print("File Uploaded successfully: link is {0} ".format( skylink))

    os.remove(file_path)
    print('File {0} deleted'.format(file_path))