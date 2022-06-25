import requests
import movieDB
import os
import wget
import siaskynet as skynet

if __name__ == "__main__":
   

    rows = movieDB.selectTable()

    for row in rows:
        link = row[1]
        info = requests.head(link)
        size = int(info.headers['Content-Length'])/ 1000000000

        if size <= 3.00:
            print('download is about start from page {0}'.format(row[2]))
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

            movieDB.InsertTableEmi(skylink, link)
            print("Inserted into DB Successfully")
            print('-'*50)
