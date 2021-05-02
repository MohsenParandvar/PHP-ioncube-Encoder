#mhsn_root

import sys
import requests
import validators
import zipfile
import shutil
import os
import ntpath

if (len(sys.argv) <= 1):
    print('use: encoder.py [fileName].php destination(default copy on here)')
    exit()
if (len(sys.argv) == 3):
    destinationPath = sys.argv[2]
    phpFilePath = sys.argv[1]
if (len(sys.argv) == 2):
    destinationPath = '.'
    phpFilePath = sys.argv[1]

phpFileName = ntpath.basename(phpFilePath)
def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        zf.extractall(dest_dir)

url = "http://piman.ir/codephp/72/upload.php"
myFile = open(phpFilePath,"rb")
req = requests.post(url,files={'fileToUpload':myFile})
response = req.text
if (validators.url(response)):
    print('(log)success to upload and link recived')
    print(response)
    download = requests.get(response,allow_redirects=True)

    encodedFile = open('downloaded.zip','wb').write(download.content)
    unzip('downloaded.zip','.')
    extractedFile = os.listdir('./encoded/')[0]
    shutil.move(f'./encoded/{extractedFile}',f'./{phpFileName}') #Move and rename file to default name

    #remove useless file and dir
    if os.path.exists("downloaded.zip"):
        os.remove("downloaded.zip")
    else:
        print("The file does not exist")
    shutil.rmtree('encoded')
else:
    print('(log)Error when uploading File:',response)

