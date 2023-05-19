'''
Takes a list of return sep snumbers in a text file(argv1) 
and downloads them to the output folder (argv2)

Called like this... dont put any slashes on the file or folder names.
Run it from the directory the snumbers.txt file is in
python3 image_downloader.py snumbers.txt outfolder
'''

import sys
import os
import requests

SNUMBER_FILE = sys.argv[1]
OUT_FOLDER   = sys.argv[2]

REQUEST_TIMEOUT = 300

# check to see if the out_folder is present
if not os.path.isdir('./' + OUT_FOLDER):
    os.makedirs('./' + OUT_FOLDER)

lines = []

with open(SNUMBER_FILE, 'r', encoding="utf-8") as f:
    lines = f.readlines()

print('Starting...')

# print(lines)

for snumber in lines:

    snumber_clean = snumber.strip()

    my_url = snumber_clean

    try:
        img_data = requests.get('https://thePasquino.com/ui/images/' + my_url, timeout=REQUEST_TIMEOUT).content
        with open('./' + OUT_FOLDER + '/' + snumber_clean, 'wb') as handler:
            handler.write(img_data)
    except Exception as e:
        print('Error downloading:' + snumber_clean + ' Error: ' + e )
    else:
        print('Downloaded: ' + snumber_clean + '.jpg' )

print('Done!')
