import requests
import os
import siaskynet as skynet

if __name__ == "__main__":
    
    url = 'https://siasky.net/EABTfUXaKxBIokvJqTxnIWLau-phIsbmLSuQdZyHOdsBMQ'

    r = requests.get(url)

    movie_name = 'test.mp4'

    with open(movie_name, 'wb') as f:
        f.write(r.content)

    print('File {0} Downloaded Successfully'.format(movie_name))

    directory = directory = os.getcwd()
    file_path = directory + '/' + movie_name
    
    client = skynet.SkynetClient() # link to skynet
    skylink = client.upload_file(file_path)
    print("File {0} Uploaded successfully: link is {1} ".format(movie_name, skylink))

    os.remove(file_path)
    print("File {0} deleted from server successfully".format(movie_name))

    #update db