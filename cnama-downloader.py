import requests
import movieDB
import os
import wget
import siaskynet as skynet

def download_upload(link,file_name):
    print('download is about start  {0}'.format(file_name))
    movie_name = wget.download(link)
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

    movieDB.InsertTableEmi(skylink, file_name)
    print("Inserted into DB Successfully")
    print('-'*50)

if __name__ == "__main__":
   
    dp = dict()
    rows = movieDB.selectTable()

    for row in rows:
        link = row[1]
        info = requests.head(link)
        print(info)
        try:
            size = int(info.headers['Content-Length'])/ 1000000000
            print(info.headers['Content-Type'])

            print('size of file is : ', size)
        except Exception as err:
            print(err)
        
        size = 2.2
        if size <= 2.50:
            print(row)
            if '1080' in info.headers['Content-Disposition'] and '{0}-1080'.format(row[2]) not in dp:
                dp['{0}-1080'.format(row[2])] = True
                download_upload(link, row[2])
                movieDB.delete_task(row[0])
            
            elif '720' in info.headers['Content-Disposition'] and '{0}-720'.format(row[2]) not in dp:
                dp['{0}-720'.format(row[2])] = True
                download_upload(link, row[2])
                movieDB.delete_task(row[0])

            elif '480' in info.headers['Content-Disposition'] and '{0}-480'.format(row[2]) not in dp:
                dp['{0}-480'.format(row[2])] = True
                download_upload(link, row[2])
                movieDB.delete_task(row[0])

                
            
