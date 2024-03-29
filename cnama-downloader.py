import requests
import movieDB
import os
import wget
import siaskynet as skynet
import urllib.request as ur

def download_upload(link, file_name, size, quality):
    print('download is about start  {0}'.format(file_name))
    try:
        movie_name = wget.download(link)
    except Exception as err :
        print(err)
        return 

    print('\nFile {0} Downloaded Successfully'.format(movie_name))

    # get current directory
    directory = os.getcwd()
    file_path = directory + '/' + movie_name

    # link to skynet
    client = skynet.SkynetClient() 
    skylink = client.upload_file(file_path)
    print("File {0} Uploaded successfully: link is {1} ".format(movie_name, skylink))

    # remove file
    os.remove(file_path)
    print("File {0} deleted from server successfully".format(movie_name))

    movieDB.InsertTableEmi(skylink, file_name, size, quality)
    print("Inserted into DB Successfully")
    print('-'*50)

if __name__ == "__main__":
   
    dp = dict()
    rows = movieDB.selectTable()

    for row in rows:
        if '720' in row[1]:
            link = row[1]
            info = ur.urlopen(link)
            try:
                size = int(info.headers['Content-Length'])/ 1000000000
                print('size of file is : ', size)
            except Exception as err:
                print(err)
            
            if size <= 1.079:
                if '720' in info.headers['Content-Disposition'] and '{0}-720'.format(row[2]) not in dp:
                    dp['{0}-720'.format(row[2])] = True
                    quality = '720p-'
                    if 'x265' in row[1]:
                        quality = quality + 'x265-'
                    if '10bit' in row[1]:
                        quality = quality + '10bkt-'
                    if 'BrRip' in row[1]:
                        quality = quality + 'BrRip-'
                    if 'DVDRip' in row[1]:
                        quality = quality + 'DVDRip-'
                    if 'BluRay' in row[1]:
                        quality = quality + 'BluRay-'
                    
                    if quality == '720p-':
                        quality = '720p-webDL'
                    
                    print(link, row[2], size, quality)
                    download_upload(link, row[2], size, quality)
                    movieDB.delete_task(row[0])
                
            
